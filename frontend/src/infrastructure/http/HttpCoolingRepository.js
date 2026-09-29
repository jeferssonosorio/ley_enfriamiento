import { API_BASE_URL } from '../../shared/constants/config.js';
import { CoolingResult } from '../../domain/Cooling.js';
import { CoolingApiRepository } from '../../application/ports/CoolingRepository.js';

export class HttpCoolingRepository extends CoolingApiRepository {
  async calculateCooling(params) {
    const payload = {
      temperatura_medio_ambiente: params.ambientTemp,
      temperatura_inicial: params.initialTemp,
      temperatura_momento_n: params.momentTemp,
      tiempo_momento_n: params.momentTime,
    };

    if (params.totalTime) payload.tiempo_total = params.totalTime;
    if (params.timeStep) payload.paso_tiempo = params.timeStep;

    const response = await fetch(`${API_BASE_URL}/ley-enfriamiento/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || errorData.temperatura_momento_n || 'Failed to calculate cooling');
    }

    const data = await response.json();
    return this._mapToDomain(data);
  }

  _mapToDomain(apiData) {
    return new CoolingResult({
      constantK: apiData.constante_k,
      items: apiData.items.map(item => ({
        position: item.posicion,
        time: item.tiempo,
        temperature: item.temperatura,
        tempDifferential: item.diferencial_temperatura,
        ambientDifferential: item.diferencial_medio,
      })),
    });
  }
}
