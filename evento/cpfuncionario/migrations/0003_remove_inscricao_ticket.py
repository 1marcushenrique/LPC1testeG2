# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 00:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cpfuncionario', '0002_auto_20171113_2149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscricao',
            name='ticket',
        ),
    ]