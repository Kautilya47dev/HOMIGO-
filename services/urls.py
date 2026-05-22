from django.urls import path
from . import views
from .views import home, book_service


urlpatterns = [

    path('', home, name='home'),

    path(
    'register/',
    views.register,
    name='register'
),

    path(
        'book/<int:service_id>/',
        book_service,
        name='book_service'
    ),

    path('amc/', views.amc, name='amc'),

    path(
        'book-amc/',
        views.book_amc,
        name='book_amc'
    ),
    path('dashboard/', views.dashboard, name='dashboard'),
]