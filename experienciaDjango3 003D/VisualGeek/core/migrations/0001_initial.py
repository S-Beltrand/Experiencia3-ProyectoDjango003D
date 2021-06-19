# Generated by Django 3.2.4 on 2021-06-19 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id categoria')),
                ('nombreCategoria', models.CharField(max_length=15, verbose_name='Nombre categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Emisor',
            fields=[
                ('nombre', models.CharField(max_length=15, verbose_name='Nombre emisor')),
                ('apellido', models.CharField(max_length=15, verbose_name='Apellido emisor')),
                ('edad', models.IntegerField(verbose_name='Edad emisor')),
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Email emisor')),
                ('resumen', models.TextField(max_length=300, verbose_name='Resumen noticia')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]