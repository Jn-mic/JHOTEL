# Generated by Django 3.2.5 on 2021-07-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jh', '0013_auto_20210729_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='select',
            field=models.PositiveSmallIntegerField(choices=[('Superior_room', 'Superior room'), ('executive_room', 'Executive room'), ('junior_room', 'Junior room'), ('presidential_room', 'Presidential Suite')], default='Superior_room'),
        ),
    ]