# Generated by Django 5.1.2 on 2024-11-05 09:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('school_id', models.IntegerField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('dept_name', models.ManyToManyField(related_name='school_department', to='department.department')),
            ],
        ),
    ]
