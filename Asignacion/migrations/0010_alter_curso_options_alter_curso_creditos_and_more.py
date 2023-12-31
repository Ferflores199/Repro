# Generated by Django 4.2.5 on 2023-10-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asignacion', '0009_delete_docente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterField(
            model_name='curso',
            name='creditos',
            field=models.IntegerField(verbose_name='Créditos'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='descripcion',
            field=models.TextField(verbose_name='Descripción'),
        ),
    ]
