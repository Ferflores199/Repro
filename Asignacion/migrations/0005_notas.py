# Generated by Django 4.2.5 on 2023-10-24 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_estudiantes_first_name_and_more'),
        ('Asignacion', '0004_horario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(decimal_places=2, max_digits=5)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asignacion.curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.estudiantes')),
            ],
        ),
    ]
