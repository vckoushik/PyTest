
from django.contrib import admin
from django.urls import include, path
from . import views

# urls
urlpatterns = [
    path('',views.index),
    path('api/v1/movies/', include('movies.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]