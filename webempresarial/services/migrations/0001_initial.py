# Generated by Django 5.1 on 2024-08-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=200, verbose_name='sibtitulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='servic', verbose_name='Imagen')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
        ),
    ]
