from rest_framework import serializers
from .models import PerfilUsuario, Rutina, Ejercicio, RegistroRutina, EstadisticasUsuario, Comentario
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = '__all__'

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'

class RutinaSerializer(serializers.ModelSerializer):
    ejercicios = EjercicioSerializer(many=True, read_only=True)  # Relación inversa
    class Meta:
        model = Rutina
        fields = '__all__'

class RegistroRutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroRutina
        fields = '__all__'

class EstadisticasUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadisticasUsuario
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'