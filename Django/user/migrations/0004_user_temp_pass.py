# Generated by Django 5.1.2 on 2024-11-06 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='temp_pass',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
