# Generated by Django 4.2.8 on 2024-06-13 12:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0014_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(max_length=10000, verbose_name='Описание'),
        ),
    ]
