from django.urls import path

from .views import detail, home_page_view, update_data, delete_date

urlpatterns = [
    path('', home_page_view, name='home'),
    path('register/', detail, name='detail'),
    path('user/<int:pk>/', update_data, name='user'),
    path('user/<int:pk>/delete/', delete_date, name='delete'),
]
