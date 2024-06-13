from .models import Post, Comment, Banner

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .forms import CommentForm, SearchForm, CarDealershipForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required


def post_list(request):
    form = SearchForm()
    query = None
    results = []
    post_list = Post.published.all()
    banners = Banner.objects.filter(is_active=True)

    # Извлекаем уникальные города из опубликованных постов
    all_cities = Post.objects.values_list('city', flat=True)
    unique_cities = list(set(all_cities))

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = Post.published.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(search=search_query).order_by('-rank')
            post_list = results  # Используем результаты поиска для постраничного вывода

    # Постраничная разбивка с 3 постами на страницу
    paginator = Paginator(post_list, 15)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page_number не целое число, то выдать первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если page_number находится вне диапазона, то выдать последнюю страницу результатов
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/list.html', {
        'posts': posts,
        'form': form,
        'query': query,
        'results': results,
        'banners': banners,
        'unique_cities': unique_cities,
    })


def filter_posts(request):
    city = request.GET.get('city')
    if city:
        filtered_posts = Post.published.filter(city=city)
    else:
        filtered_posts = Post.published.all()

    context = {
        'filtered_posts': filtered_posts,
        'selected_city': city  # Передаем выбранный город для отображения на странице
    }
    return render(request, 'filtered_posts.html', context)


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # Список активных комментариев к этому посту
    comments = post.comments.filter(active=True)
    # Форма для комментирования пользователями
    form = CommentForm()
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments, 'form': form})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post,
                             id=post_id,
                             status=Post.Status.PUBLISHED)
    comment = None
    # Комментарий был отправлен
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Создать объект класса Comment, не сохраняя его в базе данных
        comment = form.save(commit=False)
        # Назначить пост комментарию
        comment.post = post
        # Сохранить комментарий в базе данных
        comment.save()
    return render(request, 'blog/comment.html', {'post': post, 'form': form, 'comment': comment})


@login_required
def add_dealership(request):
    if request.method == 'POST':
        form = CarDealershipForm(request.POST, request.FILES)
        if form.is_valid():
            dealership = form.save(commit=False)
            dealership.user = request.user
            dealership.save()
            # Страница успешного добавления
            return render(request, 'blog/add_dealership.html', {'form': CarDealershipForm()})
    else:
        form = CarDealershipForm()
    return render(request, 'blog/add_dealership.html', {'form': form})


def rools(request):

    context = {
        'title': 'Правила сайта'
    }

    return render(request, 'rools/rools.html', context)


def policy(request):

    context = {
        'title': 'Политика конфиденциальности'
    }

    return render(request, 'rools/policy.html', context)
