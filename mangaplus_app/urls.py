from django.urls import path
from . import views

app_name = 'mangaplus_app'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('manga/<int:title_id>/', views.title_detail, name='title_detail'),
    path('<str:manga_lang>/', views.homepage, name='manga_info'),
    path('chapter/<int:chapter_id>/', views.manga_detail, name='manga_detail'),
    path('manga_overview/<int:title_id>/', views.manga_overview),
]

