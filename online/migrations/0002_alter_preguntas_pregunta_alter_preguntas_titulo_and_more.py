# Generated by Django 4.1 on 2022-11-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas',
            name='Pregunta',
            field=models.TextField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='Titulo',
            field=models.CharField(max_length=60, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='Respuesta',
            field=models.TextField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='respuesta',
            name='idRespuesta',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name=''),
        ),
    ]