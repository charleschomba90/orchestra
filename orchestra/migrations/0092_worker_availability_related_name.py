# Generated by Django 2.2.13 on 2020-11-21 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orchestra', '0091_worker_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workeravailability',
            name='worker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='availabilities', to='orchestra.Worker'),
        ),
    ]
