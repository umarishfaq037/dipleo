# Generated by Django 3.0 on 2020-03-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_applyjob_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='appointment_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
