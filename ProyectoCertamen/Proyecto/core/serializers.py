from rest_framework.serializers import ModelSerializer
from core.models import Equipo

class EquipoSerializer(ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['Codigo', 'Marca', 'recibido', 'matrona']