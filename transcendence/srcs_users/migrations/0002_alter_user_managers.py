# Generated by Django 4.2.8 on 2023-12-12 18:25

from django.db import migrations
import srcs_users.managers


class Migration(migrations.Migration):

    dependencies = [
        ('srcs_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', srcs_users.managers.IntraUserOAuth2Manager()),
            ],
        ),
    ]
