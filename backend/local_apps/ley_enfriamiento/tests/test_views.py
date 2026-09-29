import pytest
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.mark.django_db
def test_api_post_calculo_exitoso_sin_autenticacion(client):
    url = "/api/ley-enfriamiento/"
    payload = {
        "temperatura_medio_ambiente": 50.0,
        "temperatura_inicial": 80.0,
        "temperatura_momento_n": 72.0,
        "tiempo_momento_n": 2.0,
    }
    response = client.post(url, data=payload, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert "constante_k" in response.data
    assert "items" in response.data
    
    items = response.data["items"]
    assert isinstance(items, list)
    assert len(items) == 21

    # k calculado para T0=80, Tm=50, T(2)=72 => k = (1/2)*ln(22/30) = -0.15515
    assert response.data["constante_k"] == pytest.approx(-0.1551, rel=1e-2)

    # Verificar estructura del primer item
    item_0 = items[0]
    assert "posicion" in item_0
    assert "tiempo" in item_0
    assert "temperatura" in item_0
    assert "diferencial_temperatura" in item_0
    assert "diferencial_medio" in item_0

    assert item_0["posicion"] == 0
    assert item_0["tiempo"] == 0.0
    assert item_0["temperatura"] == 80.0
    assert item_0["diferencial_temperatura"] == 0.0
    assert item_0["diferencial_medio"] == 30.0


@pytest.mark.django_db
def test_api_get_calculo_exitoso_query_params(client):
    url = "/api/ley-enfriamiento/"
    response = client.get(
        url,
        {
            "temperatura_medio_ambiente": "30",
            "temperatura_inicial": "80", 
            "temperatura_momento_n": "75.42",
            "tiempo_momento_n": "3",
        },
    )

    assert response.status_code == status.HTTP_200_OK
    assert "constante_k" in response.data
    assert "items" in response.data
    
    items = response.data["items"]
    assert isinstance(items, list)
    assert len(items) == 21
    assert items[0]["posicion"] == 0
    assert items[0]["temperatura"] == 80.0


@pytest.mark.django_db
def test_api_url_calcular(client):
    url = "/api/ley-enfriamiento/calcular/"
    payload = {
        "temperatura_medio_ambiente": 20.0,
        "temperatura_inicial": 90.0,
        "temperatura_momento_n": 80.0,
        "tiempo_momento_n": 5.0,
        "tiempo_total": 10.0,
        "paso_tiempo": 5.0,
    }
    response = client.post(url, data=payload, format="json")

    assert response.status_code == status.HTTP_200_OK
    items = response.data["items"]
    assert len(items) == 3  # t=0, t=5, t=10
    assert items[0]["posicion"] == 0
    assert items[0]["tiempo"] == 0.0
    assert items[0]["temperatura"] == 90.0
    assert items[0]["diferencial_medio"] == 70.0


@pytest.mark.django_db
def test_api_error_campos_faltantes(client):
    url = "/api/ley-enfriamiento/"
    response = client.post(url, data={"temperatura_inicial": 80.0}, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "temperatura_medio_ambiente" in response.data
    assert "temperatura_momento_n" in response.data
    assert "tiempo_momento_n" in response.data


@pytest.mark.django_db
def test_api_error_datos_invalidos(client):
    url = "/api/ley-enfriamiento/"
    response = client.post(
        url,
        data={
            "temperatura_inicial": "invalido",
            "temperatura_medio_ambiente": 30.0,
            "temperatura_momento_n": 25.0,
            "tiempo_momento_n": 5.0,
        },
        format="json",
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "temperatura_inicial" in response.data
