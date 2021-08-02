# Generated by Django 3.2.5 on 2021-07-28 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jh', '0006_auto_20210728_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='booK',
        ),
        migrations.AddField(
            model_name='room',
            name='booK',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jh.booking'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'First class'), (2, 'Business class'), (3, 'Events')], default=1),
        ),
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Superior room'), (2, 'Executive room'), (3, 'Junior room'), (4, 'Presidential Suite')], default=1),
        ),
    ]
