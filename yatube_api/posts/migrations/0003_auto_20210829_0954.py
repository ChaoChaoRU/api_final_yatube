# Generated by Django 2.2.16 on 2021-08-29 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210827_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='user',
        ),
    ]
