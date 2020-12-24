# Generated by Django 3.1.1 on 2020-12-22 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puntajes',
            fields=[
                ('clave', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='inicio.encuesta')),
                ('votos_1', models.PositiveIntegerField()),
                ('votos_2', models.PositiveIntegerField()),
                ('votos_3', models.PositiveIntegerField()),
                ('votos_4', models.PositiveIntegerField()),
                ('votos_5', models.PositiveIntegerField()),
                ('votos_6', models.PositiveIntegerField()),
                ('votos_7', models.PositiveIntegerField()),
                ('votos_8', models.PositiveIntegerField()),
                ('votos_9', models.PositiveIntegerField()),
                ('votos_10', models.PositiveIntegerField()),
            ],
        ),
    ]