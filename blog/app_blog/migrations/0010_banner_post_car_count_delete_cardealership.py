# Generated by Django 4.2.8 on 2024-06-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0009_alter_cardealership_options_post_address_post_tel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='banners/', verbose_name='Изображение')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
                'ordering': ['-published_at'],
            },
        ),
        migrations.AddField(
            model_name='post',
            name='car_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='CarDealership',
        ),
    ]