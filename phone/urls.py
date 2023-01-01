from django.contrib import admin
from django.urls import path
from phone.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('delete/<int:pk>/', views.delete, name='delete-form'),
    path('api/phones/', views.ListPhones.as_view()),
    path('api/phones/<int:pk>/', views.DeletePhone.as_view())
]
