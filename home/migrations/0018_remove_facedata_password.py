# Generated by Django 5.0.2 on 2024-05-06 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_userlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facedata',
            name='password',
        ),
    ]