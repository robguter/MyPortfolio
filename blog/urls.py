from django.urls import path
from .views import rndr_psts, post_detail

app_name = 'blog'
urlpatterns = [
    path('', rndr_psts, name='posts'),
    path('<int:post_id>', post_detail, name='post_detail'),
]