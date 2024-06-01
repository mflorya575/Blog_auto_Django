# Generated by Django 4.2.8 on 2024-05-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0008_cardealership'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cardealership',
            options={'verbose_name': 'авто дилер', 'verbose_name_plural': 'Авто дилеры'},
        ),
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='tel',
            field=models.CharField(default=False, max_length=20),
        ),
    ]