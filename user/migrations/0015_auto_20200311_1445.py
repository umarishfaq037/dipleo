# Generated by Django 3.0 on 2020-03-11 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20200311_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='appointment_date',
            field=models.TextField(default=None, null=True),
        ),
    ]
