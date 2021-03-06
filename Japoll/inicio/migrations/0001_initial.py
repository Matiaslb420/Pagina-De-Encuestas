# Generated by Django 3.1.1 on 2020-12-17 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('clave', models.CharField(max_length=4, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=40)),
                ('res_1', models.CharField(max_length=40)),
                ('res_2', models.CharField(max_length=40)),
                ('res_3', models.CharField(blank=True, max_length=40)),
                ('res_4', models.CharField(blank=True, max_length=40)),
                ('res_5', models.CharField(blank=True, max_length=40)),
                ('res_6', models.CharField(blank=True, max_length=40)),
                ('res_7', models.CharField(blank=True, max_length=40)),
                ('res_8', models.CharField(blank=True, max_length=40)),
                ('res_9', models.CharField(blank=True, max_length=40)),
                ('res_10', models.CharField(blank=True, max_length=40)),
                ('autor', models.CharField(max_length=25)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('abierto', models.BooleanField()),
            ],
        ),
    ]
