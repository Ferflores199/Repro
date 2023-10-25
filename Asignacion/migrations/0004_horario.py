# Generated by Django 4.2.5 on 2023-10-24 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asignacion', '0003_rename_cursos_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=10)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asignacion.curso')),
            ],
        ),
    ]