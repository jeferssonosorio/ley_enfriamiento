import math
import pytest
from local_apps.ley_enfriamiento.models.enfriamiento import ItemEnfriamiento, LeyEnfriamiento


def test_item_enfriamiento_creacion_y_dict():
    item = ItemEnfriamiento(
        posicion=0,
        tiempo=0.0,
        temperatura=80.0,
        diferencial_temperatura=0.0,
        diferencial_medio=50.0,
    )
    assert item.posicion == 0
    assert item.tiempo == 0.0
    assert item.temperatura == 80.0
    assert item.diferencial_temperatura == 0.0
    assert item.diferencial_medio == 50.0

    d = item.to_dict()
    assert d["posicion"] == 0
    assert d["tiempo"] == 0.0
    assert d["temperatura"] == 80.0
    assert d["diferencial_temperatura"] == 0.0
    assert d["diferencial_medio"] == 50.0


def test_ley_enfriamiento_valores_defecto():
    modelo = LeyEnfriamiento(
        temperatura_inicial=80.0,
        temperatura_medio_ambiente=30.0,
        temperatura_momento_n=75.4232,
        tiempo_momento_n=3.0,
    )
    assert modelo.temperatura_inicial == 80.0
    assert modelo.temperatura_medio_ambiente == 30.0
    assert modelo.tiempo_total == 60.0
    assert modelo.paso_tiempo == 3.0
    assert modelo.decimales == 4
    # k debe ser cercano a -0.032
    assert modelo.k == pytest.approx(-0.032, rel=1e-3)


def test_ley_enfriamiento_evaluacion_tiempo_cero():
    modelo = LeyEnfriamiento(
        temperatura_inicial=80.0,
        temperatura_medio_ambiente=30.0,
        temperatura_momento_n=72.0,
        tiempo_momento_n=2.0,
    )
    temp_0 = modelo.evaluar_temperatura(0)
    assert temp_0 == 80.0

    dif_temp = modelo.calcular_diferencial_temperatura(temp_0)
    dif_medio = modelo.calcular_diferencial_medio(temp_0)

    assert dif_temp == 0.0
    assert dif_medio == 50.0


def test_ley_enfriamiento_calculo_tabla_documento():
    # Basado en los valores del documento: T0 = 80, Tm = 30, t=3, Tt=75.4232 => k = -0.032
    modelo = LeyEnfriamiento(
        temperatura_inicial=80.0,
        temperatura_medio_ambiente=30.0,
        temperatura_momento_n=75.4232,
        tiempo_momento_n=3.0,
        tiempo_total=60.0,
        paso_tiempo=3.0,
        decimales=4,
    )
    resultado = modelo.calcular()
    items = resultado["items"]
    
    # De 0 a 60 en pasos de 3 son 21 puntos (0, 3, 6, ..., 60)
    assert len(items) == 21
    assert resultado["constante_k"] == pytest.approx(-0.032, rel=1e-3)

    # Verificar primer punto (t=0)
    item_0 = items[0]
    assert item_0.posicion == 0
    assert item_0.tiempo == 0.0
    assert item_0.temperatura == 80.0
    assert item_0.diferencial_temperatura == 0.0
    assert item_0.diferencial_medio == 50.0

    # Verificar segundo punto (t=3)
    # T(3) = (80 - 30)*e^(-0.032*3) + 30 ≈ 75.4232
    item_1 = items[1]
    assert item_1.posicion == 1
    assert item_1.tiempo == 3.0
    assert item_1.temperatura == pytest.approx(75.4232, rel=1e-3)


def test_ley_enfriamiento_calentamiento_objeto_frio():
    # Caso donde el objeto está más frío que el ambiente (T0 < Tm)
    modelo = LeyEnfriamiento(
        temperatura_inicial=10.0,
        temperatura_medio_ambiente=25.0,
        temperatura_momento_n=15.0,
        tiempo_momento_n=5.0,
        tiempo_total=20.0,
        paso_tiempo=5.0,
    )
    items = modelo.calcular()["items"]
    assert len(items) == 5

    # La temperatura debe aumentar hacia Tm
    assert items[0].temperatura == 10.0
    assert items[-1].temperatura > items[0].temperatura
    assert items[-1].temperatura <= 25.0


def test_ley_enfriamiento_validaciones_tiempo():
    # probar error con paso_tiempo invalido
    with pytest.raises(ValueError, match="El paso de tiempo debe ser mayor a 0"):
        m1 = LeyEnfriamiento(80, 30, 70, 3, paso_tiempo=0)
        m1.calcular()

    with pytest.raises(ValueError, match="El tiempo total no puede ser negativo"):
        m2 = LeyEnfriamiento(80, 30, 70, 3, tiempo_total=-10)
        m2.calcular()
        
    with pytest.raises(ValueError, match="Las temperaturas indican un comportamiento imposible"):
        # Tt debe estar entre T0 y Tm, si no arroja error. Si T0=80, Tm=30, t=3, pero Tt = 20 (baja más del ambiente) -> Error
        LeyEnfriamiento(80, 30, 20, 3)
