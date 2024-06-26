# Generated by Django 5.0.4 on 2024-05-08 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0001_initial'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commission',
            options={'ordering': ['status', '-created_on']},
        ),
        migrations.RemoveField(
            model_name='commission',
            name='people_required',
        ),
        migrations.AddField(
            model_name='commission',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='authored_commission', to='user_management.profile'),
        ),
        migrations.AddField(
            model_name='commission',
            name='status',
            field=models.CharField(choices=[('a', 'Open'), ('b', 'Full'), ('c', 'Completed'), ('d', 'Discontinued')], default='Open', max_length=255),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('manpower_required', models.IntegerField()),
                ('status', models.CharField(choices=[('a', 'Open'), ('b', 'Full')], default='Open', max_length=255)),
                ('commission', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job', to='commissions.commission')),
            ],
            options={
                'ordering': ['status', '-manpower_required', 'role'],
            },
        ),
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('a', 'Pending'), ('b', 'Accepted'), ('c', 'Rejected')], default='Pending', max_length=255)),
                ('applied_on', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicantprofile', to='user_management.profile')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobapplication', to='commissions.job')),
            ],
            options={
                'ordering': ['status', '-applied_on'],
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
