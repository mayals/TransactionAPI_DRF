from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),

    # exchange app
    path('', include('exchange.urls')),
] 

