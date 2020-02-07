# Generated by Django 3.0.3 on 2020-02-07 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20200207_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='expiry',
            new_name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='max_salary',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='min_salary',
        ),
        migrations.AddField(
            model_name='jobs',
            name='city',
            field=models.CharField(default='City', max_length=30),
        ),
        migrations.AddField(
            model_name='jobs',
            name='country',
            field=models.CharField(default='Country', max_length=30),
        ),
        migrations.AddField(
            model_name='jobs',
            name='create_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='jobs',
            name='industry',
            field=models.CharField(default='industry', max_length=30),
        ),
        migrations.AddField(
            model_name='jobs',
            name='job_type',
            field=models.CharField(default='Job Type', max_length=30),
        ),
        migrations.AddField(
            model_name='jobs',
            name='num_vacanices',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jobs',
            name='salary',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='jobs',
            name='total_exp',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jobs',
            name='work_days',
            field=models.CharField(default='Work_days', max_length=100),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='description',
            field=models.TextField(default='Description', max_length=500),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_title',
            field=models.CharField(default='Job Title', max_length=30),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='qualification',
            field=models.CharField(default='Qualification', max_length=30),
        ),
    ]
