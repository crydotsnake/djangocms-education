# Generated by Django 3.2.12 on 2022-04-10 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='title',
        ),
    ]
