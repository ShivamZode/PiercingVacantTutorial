# Generated by Django 5.0.2 on 2024-05-05 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_user_email_alter_user_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='User1',
        ),
    ]
