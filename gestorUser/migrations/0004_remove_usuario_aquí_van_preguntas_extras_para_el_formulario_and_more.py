# Generated by Django 4.2.4 on 2023-11-29 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestorUser', '0003_remove_usuario_nombre_empresa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='Aquí_van_preguntas_extras_para_el_formulario',
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
    ]
