# Generated by Django 4.2.5 on 2023-10-24 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asignacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cursos',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]