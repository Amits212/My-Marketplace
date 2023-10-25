from . import views
from django.urls import path

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('item/<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]