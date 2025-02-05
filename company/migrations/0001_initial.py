# Generated by Django 2.2 on 2019-12-03 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.TextField()),
                ('min_salary', models.IntegerField()),
                ('max_salary', models.IntegerField()),
                ('qualification', models.TextField()),
                ('description', models.TextField()),
                ('expiry', models.TextField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.Company')),
            ],
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.Applicants')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.Jobs')),
            ],
        ),
    ]
