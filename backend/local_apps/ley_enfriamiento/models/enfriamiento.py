import math


class ItemEnfriamiento:
    """
    Representa un punto evaluado en el tiempo dentro del proceso de enfriamiento de Newton.
    """

    def __init__(self, posicion, tiempo, temperatura, diferencial_temperatura, diferencial_medio):
        self.posicion = posicion
        self.tiempo = tiempo
        self.temperatura = temperatura
        self.diferencial_temperatura = diferencial_temperatura
        self.diferencial_medio = diferencial_medio

    def to_dict(self):
        return {
            "posicion": self.posicion,
            "tiempo": self.tiempo,
            "temperatura": self.temperatura,
            "diferencial_temperatura": self.diferencial_temperatura,
            "diferencial_medio": self.diferencial_medio,
        }


class LeyEnfriamiento:
    """
    Modelo matemático basado en la Ley de Enfriamiento de Newton:
    """

    DEFAULT_TIEMPO_TOTAL = 60.0
    DEFAULT_PASO_TIEMPO = 3.0
    DEFAULT_DECIMALES = 4

    def __init__(
        self,
        temperatura_inicial,
        temperatura_medio_ambiente,
        temperatura_momento_n,
        tiempo_momento_n,
        tiempo_total=None,
        paso_tiempo=None,
        decimales=None,
    ):
        self.temperatura_inicial = float(temperatura_inicial)
        self.temperatura_medio_ambiente = float(temperatura_medio_ambiente)
        self.temperatura_momento_n = float(temperatura_momento_n)
        self.tiempo_momento_n = float(tiempo_momento_n)
        
        self.tiempo_total = float(tiempo_total) if tiempo_total is not None else self.DEFAULT_TIEMPO_TOTAL
        self.paso_tiempo = float(paso_tiempo) if paso_tiempo is not None else self.DEFAULT_PASO_TIEMPO
        self.decimales = int(decimales) if decimales is not None else self.DEFAULT_DECIMALES

        self.k = self._calcular_constante_k()

    def _calcular_constante_k(self):
        """
        Calcula la constante K a partir de los datos dados.
        k = (1 / t) * ln((T(t) - Tm) / (T0 - Tm))
        Nota: math.log en Python calcula el logaritmo natural.
        """
        t = self.tiempo_momento_n
        tt = self.temperatura_momento_n
        tm = self.temperatura_medio_ambiente
        t0 = self.temperatura_inicial
        
        # Validaciones de seguridad matemática ya controladas por el serializer
        # Pero es buena práctica evitar errores matemáticos aquí:
        razon = (tt - tm) / (t0 - tm)
        
        if razon <= 0:
            raise ValueError("Las temperaturas indican un comportamiento imposible termodinámicamente o asintótico.")
            
        k = (1.0 / t) * math.log(razon)
        return k

    def evaluar_temperatura(self, t):
        t0 = self.temperatura_inicial
        tm = self.temperatura_medio_ambiente
        temp = (t0 - tm) * math.exp(self.k * t) + tm
        return temp

    def calcular_diferencial_temperatura(self, temperatura_evaluada):
        return self.temperatura_inicial - temperatura_evaluada

    def calcular_diferencial_medio(self, temperatura_evaluada):
        return temperatura_evaluada - self.temperatura_medio_ambiente

    def _redondear(self, valor):
        if self.decimales is not None and self.decimales >= 0:
            return round(valor, self.decimales)
        return valor

    def calcular(self):
        items = []
        if self.paso_tiempo <= 0:
            raise ValueError("El paso de tiempo debe ser mayor a 0.")
        if self.tiempo_total < 0:
            raise ValueError("El tiempo total no puede ser negativo.")

        num_pasos = int(round(self.tiempo_total / self.paso_tiempo))

        for pos in range(num_pasos + 1):
            t = round(pos * self.paso_tiempo, 6)
            if t > self.tiempo_total and pos > 0:
                t = self.tiempo_total

            temp = self.evaluar_temperatura(t)
            dif_temp = self.calcular_diferencial_temperatura(temp)
            dif_medio = self.calcular_diferencial_medio(temp)

            item = ItemEnfriamiento(
                posicion=pos,
                tiempo=self._redondear(t),
                temperatura=self._redondear(temp),
                diferencial_temperatura=self._redondear(dif_temp),
                diferencial_medio=self._redondear(dif_medio),
            )
            items.append(item)

        return {
            "constante_k": self._redondear(self.k),
            "items": items
        }
