# Generated by Django 3.0.3 on 2020-02-07 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20200207_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_skill',
            name='job',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.DO_NOTHING, to='company.Jobs'),
        ),
    ]
