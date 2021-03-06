# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 00:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Periodo de trabalho')),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HoraDeRegistro', models.TimeField(blank=True, null=True, verbose_name='HoraDeRegistro ')),
                ('ipMaquina', models.CharField(max_length=200, verbose_name='ipMaquina: ')),
                ('validacao', models.BooleanField(default=False, verbose_name='Situação')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome ')),
                ('end', models.CharField(max_length=200, verbose_name='Endereço ')),
                ('fone', models.CharField(max_length=200, verbose_name='Fone ')),
                ('HoraDeInicioManha', models.TimeField(blank=True, null=True, verbose_name='Entrada da Manha ')),
                ('HoraDeSaidaManha', models.TimeField(blank=True, null=True, verbose_name='ate Saida da Manha ')),
                ('HoraDeInicioTarde', models.TimeField(blank=True, null=True, verbose_name='Entrada da Tarde ')),
                ('HoraDeSaidaTarde', models.TimeField(blank=True, null=True, verbose_name='ate Saida da Tarde ')),
                ('chefe', models.CharField(max_length=200, verbose_name='Chefe ')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome: ')),
                ('desc', models.CharField(max_length=200, verbose_name='Descrição: ')),
                ('valor', models.FloatField(max_length=200, verbose_name='Valor: ')),
                ('validacao', models.BooleanField(default=True, verbose_name='Validação')),
                ('evento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cpfuncionario.Evento')),
            ],
        ),
        migrations.AddField(
            model_name='inscricao',
            name='Funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Funcionario', to='cpfuncionario.Pessoa'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='TipoDeRegistro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TipoDeRegistro', to='cpfuncionario.Evento'),
        ),
    ]
