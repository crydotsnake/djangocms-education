# Generated by Django 3.2.12 on 2022-04-11 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_education', '0002_remove_education_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start date'),
        ),
    ]
