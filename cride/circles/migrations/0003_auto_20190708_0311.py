# Generated by Django 2.2.3 on 2019-07-08 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0002_auto_20190708_0209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='remaining_invitation',
            new_name='remaining_invitations',
        ),
    ]
