# Generated by Django 3.2.5 on 2021-07-28 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jh', '0007_auto_20210728_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='booK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jh.booking'),
        ),
    ]
