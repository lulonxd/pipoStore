# Generated by Django 3.1.2 on 2020-11-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorDeProductos', '0004_producto_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]