# Generated by Django 5.0.6 on 2024-06-11 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marcala_place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='cover_image',
            field=models.ImageField(upload_to='vendors.jpg'),
        ),
    ]
