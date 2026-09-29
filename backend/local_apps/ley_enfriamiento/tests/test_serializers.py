import pytest
from local_apps.ley_enfriamiento.models.enfriamiento import ItemEnfriamiento
from local_apps.ley_enfriamiento.serializers.enfriamiento import (
    EnfriamientoInputSerializer,
    ItemEnfriamientoSerializer,
    RespuestaEnfriamientoSerializer,
)


def test_input_serializer_valido():
    data = {
        "temperatura_medio_ambiente": 30.0,
        "temperatura_inicial": 80.0,
        "temperatura_momento_n": 72.0,
        "tiempo_momento_n": 3.0,
    }
    serializer = EnfriamientoInputSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    assert serializer.validated_data["temperatura_inicial"] == 80.0
    assert serializer.validated_data["temperatura_medio_ambiente"] == 30.0
    assert serializer.validated_data["temperatura_momento_n"] == 72.0
    assert serializer.validated_data["tiempo_momento_n"] == 3.0
    assert serializer.validated_data["tiempo_total"] == 60.0
    assert serializer.validated_data["paso_tiempo"] == 3.0
    assert serializer.validated_data["decimales"] == 4


def test_input_serializer_logica_temperatura_invalida():
    # T0 > Tm pero Tt <= Tm (enfriamiento se pasa del ambiente)
    data = {
        "temperatura_medio_ambiente": 30.0,
        "temperatura_inicial": 80.0,
        "temperatura_momento_n": 25.0,
        "tiempo_momento_n": 3.0,
    }
    serializer = EnfriamientoInputSerializer(data=data)
    assert not serializer.is_valid()
    assert "temperatura_momento_n" in serializer.errors

    # T0 == Tm (No hay transferencia de calor)
    data2 = {
        "temperatura_medio_ambiente": 50.0,
        "temperatura_inicial": 50.0,
        "temperatura_momento_n": 40.0,
        "tiempo_momento_n": 3.0,
    }
    serializer2 = EnfriamientoInputSerializer(data=data2)
    assert not serializer2.is_valid()
    assert "temperatura_inicial" in serializer2.errors


def test_input_serializer_faltan_campos_requeridos():
    serializer1 = EnfriamientoInputSerializer(data={"temperatura_medio_ambiente": 25.0})
    assert not serializer1.is_valid()
    assert "temperatura_inicial" in serializer1.errors
    assert "temperatura_momento_n" in serializer1.errors
    assert "tiempo_momento_n" in serializer1.errors


def test_input_serializer_paso_mayor_a_tiempo_total():
    data = {
        "temperatura_medio_ambiente": 30.0,
        "temperatura_inicial": 80.0,
        "temperatura_momento_n": 75.0,
        "tiempo_momento_n": 3.0,
        "tiempo_total": 10.0,
        "paso_tiempo": 20.0,
    }
    serializer = EnfriamientoInputSerializer(data=data)
    assert not serializer.is_valid()
    assert "paso_tiempo" in serializer.errors


def test_item_serializer_formato():
    item = ItemEnfriamiento(
        posicion=2,
        tiempo=6.0,
        temperatura=71.2185,
        diferencial_temperatura=8.7815,
        diferencial_medio=41.2185,
    )
    serializer = ItemEnfriamientoSerializer(item)
    data = serializer.data
    assert data["posicion"] == 2
    assert data["tiempo"] == 6.0
    assert data["temperatura"] == 71.2185
    assert data["diferencial_temperatura"] == 8.7815
    assert data["diferencial_medio"] == 41.2185


def test_respuesta_serializer_formato():
    item = ItemEnfriamiento(
        posicion=0,
        tiempo=0.0,
        temperatura=80.0,
        diferencial_temperatura=0.0,
        diferencial_medio=30.0,
    )
    
    data = {
        "constante_k": -0.05,
        "items": [item]
    }
    serializer = RespuestaEnfriamientoSerializer(data)
    d = serializer.data
    assert "constante_k" in d
    assert d["constante_k"] == -0.05
    assert "items" in d
    assert len(d["items"]) == 1
