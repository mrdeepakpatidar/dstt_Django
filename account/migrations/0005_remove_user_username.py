# Generated by Django 3.0.7 on 2021-02-08 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]