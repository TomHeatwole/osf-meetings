# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-02 14:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('submissions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('osf_id', models.CharField(blank=True, max_length=100)),
                ('osf_path', models.URLField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('submission', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='submissions.Submission')),
            ],
        ),
    ]
