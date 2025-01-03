# Generated by Django 5.1.2 on 2024-11-05 09:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('department_name', models.CharField(blank=True, max_length=100, null=True)),
                ('dept_id', models.IntegerField(primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
