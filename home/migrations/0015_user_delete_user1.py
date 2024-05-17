# Generated by Django 5.0.2 on 2024-05-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_user1_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(default='email', max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='User1',
        ),
    ]