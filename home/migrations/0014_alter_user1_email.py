# Generated by Django 5.0.2 on 2024-05-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_rename_email1_user1_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='email',
            field=models.EmailField(default='email', max_length=30),
        ),
    ]
