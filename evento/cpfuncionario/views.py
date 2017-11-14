from django.shortcuts import render
from cpfuncionario.models import *
# import para API
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from cpfuncionario.serializers import UserSerializer
from cpfuncionario.serializers import EventoSerializer
from cpfuncionario.serializers import InscricaoSerializer
from cpfuncionario.serializers import PessoaSerializer
from cpfuncionario.serializers import TicketSerializer



# Create your views here.

#ViewSets define the view behavior
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class PessoaViewSet(viewsets.ModelViewSet):
  queryset = Pessoa.objects.all()
  serializer_class = PessoaSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class InscricaoViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# Create your views here.
