# Generated by Django 5.0.2 on 2024-04-30 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landmarks', models.TextField()),
                ('face_descriptor', models.TextField()),
            ],
        ),
    ]
