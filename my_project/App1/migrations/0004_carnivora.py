# Generated by Django 5.1.3 on 2024-12-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_exterior_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carnivora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cientifico', models.CharField(max_length=100)),
                ('nombre_comun', models.CharField(max_length=100)),
                ('tipo_de_clima', models.CharField(max_length=30)),
                ('riego_semanal', models.IntegerField()),
                ('ciudados_especiales', models.CharField(max_length=400)),
                ('alimentacion', models.CharField(max_length=100)),
                ('foto', models.ImageField(default='images/default.jpg', upload_to='images/')),
            ],
        ),
    ]
