# Generated by Django 5.1.2 on 2024-11-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_hod'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='User', max_length=100),
        ),
    ]