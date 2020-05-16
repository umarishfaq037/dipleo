# Generated by Django 2.2.11 on 2020-05-16 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_notifications_settings'),
    ]

    operations = [
        
        migrations.CreateModel(
            name='SavedApplyJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ApplyJob')),
            ],
        ),
        
    ]
