from django.contrib import admin
from django.urls import path
from .views import register_user, login, payments

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register_user, name='register_user'),
    path('api/login/', login, name='login'),
    path('api/payments/', payments, name='payments')
]
