# Generated by Django 5.0.2 on 2024-05-10 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_alter_presenty_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='presenty',
            unique_together={('name', 'subject', 'date')},
        ),
    ]