# Generated by Django 3.2.12 on 2022-04-10 20:25

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_education_education', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('company', models.CharField(max_length=255, verbose_name='Company')),
                ('job', models.CharField(max_length=255, verbose_name='Job')),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('description', djangocms_text_ckeditor.fields.HTMLField(blank=True, max_length=2048, null=True, verbose_name='Description')),
                ('website', models.CharField(blank=True, max_length=255, null=True, verbose_name='Website')),
                ('active_post', models.BooleanField(verbose_name='Active Position?')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]