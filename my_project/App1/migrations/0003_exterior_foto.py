# Generated by Django 5.1.3 on 2024-12-08 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_interior_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='exterior',
            name='foto',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
