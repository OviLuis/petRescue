# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('raza', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=400)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=10)),
                ('ubicacion', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to=b'', verbose_name=b'foto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
