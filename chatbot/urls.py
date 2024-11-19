from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('chatbot/', views.chatbot, name='chatbot'),  # Страница чата
    path('logs_playme/', views.logs_playme, name='logs_playme'),  # Страница логов
]
