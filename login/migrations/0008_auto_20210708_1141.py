# Generated by Django 3.1.7 on 2021-07-08 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20210419_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discorduser',
            name='room_access',
        ),
        migrations.RemoveField(
            model_name='discorduser',
            name='room_admin',
        ),
    ]