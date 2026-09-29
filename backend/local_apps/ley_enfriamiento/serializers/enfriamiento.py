from rest_framework import serializers


class EnfriamientoInputSerializer(serializers.Serializer):
    """
    Serializador de entrada para los parámetros del cálculo de la Ley de Enfriamiento.
    """

    temperatura_medio_ambiente = serializers.FloatField(
        required=True,
        help_text="Temperatura del medio ambiente (Tm)."
    )
    temperatura_inicial = serializers.FloatField(
        required=True,
        help_text="Temperatura inicial del objeto (T0) en t=0."
    )
    temperatura_momento_n = serializers.FloatField(
        required=True,
        help_text="Temperatura evaluada en el momento n (Tt)."
    )
    tiempo_momento_n = serializers.FloatField(
        required=True,
        min_value=0.0001,
        help_text="Tiempo exacto en el que ocurrió la medición de temperatura en el momento n (t)."
    )
    tiempo_total = serializers.FloatField(
        required=False,
        default=60.0,
        min_value=0.1,
        help_text="Tiempo total de evaluación en minutos (default: 60.0)."
    )
    paso_tiempo = serializers.FloatField(
        required=False,
        default=3.0,
        min_value=0.001,
        help_text="Paso o intervalo de tiempo de las iteraciones (default: 3.0)."
    )
    decimales = serializers.IntegerField(
        required=False,
        default=4,
        min_value=0,
        max_value=10,
        help_text="Precisión de redondeo de decimales (default: 4)."
    )

    def validate(self, attrs):
        t0 = attrs.get("temperatura_inicial")
        tm = attrs.get("temperatura_medio_ambiente")
        tt = attrs.get("temperatura_momento_n")
        
        tiempo_total = attrs.get("tiempo_total", 60.0)
        paso_tiempo = attrs.get("paso_tiempo", 3.0)

        if paso_tiempo > tiempo_total:
            raise serializers.ValidationError(
                {"paso_tiempo": "El paso de tiempo no puede ser mayor que el tiempo total."}
            )

        if t0 == tm:
            raise serializers.ValidationError(
                {"temperatura_inicial": "La temperatura inicial no puede ser exactamente igual a la del medio ambiente para que exista enfriamiento/calentamiento."}
            )
            
        if tt == tm:
            raise serializers.ValidationError(
                {"temperatura_momento_n": "La temperatura en el momento n no puede haber alcanzado exactamente la del ambiente (comportamiento asintótico), impediría calcular K."}
            )

        # Si el objeto inicia más caliente que el medio (enfriamiento)
        if t0 > tm:
            if tt >= t0:
                raise serializers.ValidationError({"temperatura_momento_n": "Para enfriamiento, la temperatura del objeto debe bajar en el momento n."})
            if tt < tm:
                raise serializers.ValidationError({"temperatura_momento_n": "Para enfriamiento, la temperatura no puede ser menor a la del ambiente."})
                
        # Si el objeto inicia más frío que el medio (calentamiento)
        if t0 < tm:
            if tt <= t0:
                raise serializers.ValidationError({"temperatura_momento_n": "Para calentamiento, la temperatura del objeto debe subir en el momento n."})
            if tt > tm:
                raise serializers.ValidationError({"temperatura_momento_n": "Para calentamiento, la temperatura no puede ser mayor a la del ambiente."})

        return attrs


class ItemEnfriamientoSerializer(serializers.Serializer):
    """
    Serializador de salida para un item del lista.
    """
    posicion = serializers.IntegerField(help_text="Posición del item en la secuencia.")
    tiempo = serializers.FloatField(help_text="Tiempo evaluado en el item.")
    temperatura = serializers.FloatField(help_text="Temperatura del objeto evaluada en el tiempo.")
    diferencial_temperatura = serializers.FloatField(
        help_text="Diferencial de temperatura (temperatura inicial - evaluada)."
    )
    diferencial_medio = serializers.FloatField(
        help_text="Diferencial con respecto al medio (temperatura evaluada - temperatura del medio)."
    )


class RespuestaEnfriamientoSerializer(serializers.Serializer):
    constante_k = serializers.FloatField(help_text="La constante K calculada a partir de los datos.")
    items = ItemEnfriamientoSerializer(many=True, help_text="Lista iterativa con los cálculos para cada elemento de tiempo.")
