from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Pessoa(models.Model):
    nome = models.CharField('Nome ', max_length=200)
    end = models.CharField('Endereço ', max_length=200)
    fone = models.CharField('Fone ', max_length=200)
    usuario=models.ForeignKey(User,  null=True, blank=False)
    HoraDeInicioManha = models.TimeField('Entrada da Manha ',blank=True, null=True)
    HoraDeSaidaManha = models.TimeField('ate Saida da Manha ',blank=True, null=True)
    HoraDeInicioTarde = models.TimeField('Entrada da Tarde ',blank=True, null=True)
    HoraDeSaidaTarde = models.TimeField('ate Saida da Tarde ',blank=True, null=True)
    chefe = models.CharField('Chefe ', max_length=200)



    def __str__(self):
        return self.nome



class Evento(models.Model):
    nome = models.CharField('Periodo de trabalho', max_length=100)
    #dataEHoraDeInicio = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nome


class Ticket(models.Model):
    nome = models.CharField('Nome: ', max_length=200)
    desc = models.CharField('Descrição: ', max_length=200)
    valor = models.FloatField('Valor: ', max_length=200)
    evento = models.ForeignKey(Evento, null=True, blank=False)
    validacao = models.BooleanField('Validação', default=True)
    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    TipoDeRegistro= models.ForeignKey(Evento, related_name="TipoDeRegistro", null=True, blank=False)
    Funcionario=models.ForeignKey(Pessoa, related_name="Funcionario", null=True, blank=False)

    HoraDeRegistro = models.TimeField('HoraDeRegistro ',blank=True, null=True)
    ipMaquina = models.CharField('ipMaquina: ', max_length=200)

    validacao = models.BooleanField("Consistente",default=False)
    def __str__(self):
        return self.Funcionario.nome
