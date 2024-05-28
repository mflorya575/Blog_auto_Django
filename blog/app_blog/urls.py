from django.urls import path
from . import views

from django.views.generic import TemplateView


app_name = 'blog'

urlpatterns = [
    # представления поста
    path('', views.post_list, name='post_list'),

    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),

    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),

    path('search/', views.post_list, name='post_search'),

    path('add-dealership/', views.add_dealership, name='add_dealership'),
    # path('dealership-success/', TemplateView.as_view(template_name='blog/dealership_success.html'),
    #      name='dealership_success'),
]
