# Generated by Django 3.2.5 on 2021-07-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jh', '0011_auto_20210728_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(blank=True, upload_to='About'),
        ),
    ]
