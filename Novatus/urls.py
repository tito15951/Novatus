from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('api/',include('apiNovatus.urls'))
]
