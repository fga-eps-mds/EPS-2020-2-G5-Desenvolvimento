from rest_framework import viewsets
from . import models
from . import serializers


class CadProfissionaisViewset(viewsets.ModelViewSet):
    queryset = models.CadProfissionais.objects.all()
    serializer_class = serializers.CadProfissionaisSerializer

class LevantamentoViolenciaViewset(viewsets.ModelViewSet):
    queryset = models.LevantamentoViolencia.objects.all()
    serializer_class = serializers.LevantamentoViolenciaSerializer


class CadProfissionaisViewset(viewsets.ModelViewSet):
    queryset = models.CadProfissionais.objects.all()
    serializer_class = serializers.CadProfissionaisSerializer
    
class CategoriaViolenciaViewset(viewsets.ModelViewSet):
    queryset = models.CategoriaViolencia.objects.all()
    serializer_class = serializers.CategoriaViolenciaSerializer


class ContatoViolenciaViewset(viewsets.ModelViewSet):
    queryset = models.ContatoViolencia.objects.all()
    serializer_class = serializers.ContatoViolenciaSerializer


class QuestionarioViewset(viewsets.ModelViewSet):
    queryset = models.Questionario.objects.all()
    serializer_class = serializers.QuestionarioSerializer


class ContatoQuestionarioViewset(viewsets.ModelViewSet):
    queryset = models.ContatoQuestionario.objects.all()
    serializer_class = serializers.ContatoQuestionarioSerializer
