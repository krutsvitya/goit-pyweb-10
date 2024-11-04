from django.urls import path
from . import views
from .views import register_view, login_view, my_logout
from django.contrib.auth.views import LogoutView

app_name = 'authorsapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', my_logout, name='logout'),
    path('add_author/', views.add_author, name='add_author'),
    path('author_info/<str:fullname>/', views.author_info, name='author_info'),
    path('add_quote/', views.add_quote, name='add_quote'),
]
