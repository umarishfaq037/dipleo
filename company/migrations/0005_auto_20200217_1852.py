# Generated by Django 3.0 on 2020-02-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_job_skill_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_skill',
            name='experience',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='job_skill',
            name='skill',
            field=models.CharField(default='Skill1', max_length=50),
        ),
    ]