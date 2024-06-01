from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse
from django.core.validators import FileExtensionValidator


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    address = models.CharField(max_length=100, default=False)
    tel = models.CharField(max_length=20, default=False)
    city = models.CharField(max_length=100, default=False)
    car_count = models.PositiveIntegerField(default=0)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)

    objects = models.Manager()  # менеджер, применяемый по умолчанию
    published = PublishedManager()  # конкретно-прикладной менеджер

    # tags = TaggableManager()

    map_html = models.TextField(blank=True, null=True)  # Поле для HTML-кода карты

    thumbnail = models.ImageField(
        verbose_name='Изображение записи',
        blank=True,
        upload_to='images/thumbnails/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    )
    upload_to = 'images/thumbnails/%Y/%m/%d/',

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'Посты'
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    def __str__(self):
        return self.title


# class CarDealership(models.Model):
#     class Status(models.TextChoices):
#         DRAFT = 'DF', 'Draft'
#         PUBLISHED = 'PB', 'Published'
#
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(max_length=250, unique_for_date='publish')
#     address = models.CharField(max_length=255)
#     photo = models.ImageField(upload_to='dealership_photos/')
#     car_count = models.PositiveIntegerField()
#     description = models.TextField()
#     map_html = models.TextField(blank=True, null=True)  # Поле для HTML-кода карты
#     approved = models.BooleanField(default=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     tel = models.CharField(max_length=20, default=False)
#
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=2,
#                               choices=Status.choices,
#                               default=Status.DRAFT)
#
#     objects = models.Manager()  # менеджер, применяемый по умолчанию
#     published = PublishedManager()  # конкретно-прикладной менеджер
#
#     class Meta:
#         verbose_name = 'Авто-дилер'
#         verbose_name_plural = 'Авто-дилеры'
#         ordering = ['-publish']
#         indexes = [
#             models.Index(fields=['-publish']),
#         ]
#
#     def get_absolute_url(self):
#         return reverse('blog:post_detail',
#                        args=[self.publish.year,
#                              self.publish.month,
#                              self.publish.day,
#                              self.slug])
#
#     def __str__(self):
#         return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    # email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Комментарий {self.name} на публикацию {self.post}'


class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    image = models.ImageField(upload_to='banners/', verbose_name="Изображение")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"
        ordering = ['-published_at']

    def __str__(self):
        return self.title
