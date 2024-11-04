from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('authorsapp.urls')),
    path('admin/', admin.site.urls),

]
