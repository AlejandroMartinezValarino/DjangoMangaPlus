from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('manga/<int:title_id>/', views.title_detail, name='title_detail'),
    path('<int:manga_id>/', views.homepage, name='manga_info'),
    path('chapter/<int:chapter_id>/', views.manga_detail, name='manga_detail'),
]

