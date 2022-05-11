from django.contrib import admin
from django.urls import path,include
from apiNovatus.views import User, Product
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]
