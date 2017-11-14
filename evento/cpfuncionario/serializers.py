from rest_framework import routers, serializers, viewsets

## Linha que não estava no Slide
from django.contrib.auth.models import User
from cpfuncionario.models import *

# Serializers define the API representation.

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ( 'url', 'username', 'email', 'is_staff')

class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    usuario=UserSerializer(many=False)
    class Meta:
        model = Pessoa
        fields = ('nome', 'end', 'fone', 'usuario', 'HoraDeInicioManha', 'HoraDeSaidaManha', 'HoraDeInicioTarde', 'HoraDeSaidaTarde', 'chefe')


    def create(self, dados):
      dados_user = dados.pop('usuario')
      u=User.objects.create(**dados_user)
      p=Pessoa.objects.create(usuario=u, **dados)
      return p




class EventoSerializer(serializers.HyperlinkedModelSerializer):
  #relacionamento de chave estrangeira
  #usuario=UserSerializer(many=False)
  class Meta:
    model = Evento
    fields = ('nome')


class TicketSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Ticket
    fields = ('nome', 'desc', 'valor', 'evento', 'validacao')


class InscricaoSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Inscricao
    fields = ('TipoDeRegistro', 'Funcionario', 'validacao', 'HoraDeRegistro', 'ipMaquina')
