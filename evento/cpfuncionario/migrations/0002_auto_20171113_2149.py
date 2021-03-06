# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 00:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpfuncionario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricao',
            name='ticket',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='cpfuncionario.Ticket'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='validacao',
            field=models.BooleanField(default=False, verbose_name='Situação do pagamento de tickets'),
        ),
    ]
