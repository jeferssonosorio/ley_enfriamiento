from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models.enfriamiento import LeyEnfriamiento
from ..serializers.enfriamiento import (
    EnfriamientoInputSerializer,
    RespuestaEnfriamientoSerializer,
)


class LeyEnfriamientoView(APIView):
    """
    API para la evaluación de la Ley de Enfriamiento de Newton.
    
    No requiere autenticación.
    """

    permission_classes = [AllowAny]
    authentication_classes = []

    def _procesar_calculo(self, data):
        serializer = EnfriamientoInputSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        parametros = serializer.validated_data
        modelo = LeyEnfriamiento(
            temperatura_medio_ambiente=parametros["temperatura_medio_ambiente"],
            temperatura_inicial=parametros["temperatura_inicial"],
            temperatura_momento_n=parametros["temperatura_momento_n"],
            tiempo_momento_n=parametros["tiempo_momento_n"],
            tiempo_total=parametros.get("tiempo_total"),
            paso_tiempo=parametros.get("paso_tiempo"),
            decimales=parametros.get("decimales"),
        )
        
        try:
            resultado = modelo.calcular()
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        salida_serializer = RespuestaEnfriamientoSerializer(resultado)
        return Response(salida_serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Calcula el enfriamiento a partir de los datos en el cuerpo de la petición (JSON)."""
        return self._procesar_calculo(request.data)

    def get(self, request, *args, **kwargs):
        """Calcula el enfriamiento a partir de los query parameters."""
        # Convertir query_params a dict simple
        datos = request.query_params.dict()
        return self._procesar_calculo(datos)
