# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.9.7 on 2016-07-21 16:54
=======
# Generated by Django 1.9.7 on 2016-07-20 20:06
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conferences', '0001_initial'),
        ('approvals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('node_id', models.CharField(max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('approval', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='approvals.Approval')),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.Conference')),
<<<<<<< HEAD
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_contributor', to=settings.AUTH_USER_MODEL)),
=======
                ('contributor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='contributor', to=settings.AUTH_USER_MODEL)),
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266
            ],
            options={
                'ordering': ('date_created',),
                'permissions': (('can_set_contributor', 'Can set the contributor for a submission'), ('view_submission', 'Can view submission')),
            },
        ),
    ]
