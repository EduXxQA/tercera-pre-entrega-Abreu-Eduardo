# Generated by Django 4.2.4 on 2023-09-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompraVenta', '0002_camioneta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.IntegerField(max_length=4)),
            ],
        ),
    ]
