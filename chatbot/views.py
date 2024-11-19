import os
from django.conf import settings
from django.shortcuts import render

def home(request):
    """Главная страница навигации"""
    return render(request, 'home.html')

def chatbot(request):
    """Страница чата"""
    return render(request, 'chatbot.html')

def logs_playme(request):
    log_dir = settings.BASE_DIR / 'logs'
    log_files = sorted(log_dir.glob('*.log'), reverse=True)  # Сортируем файлы логов по времени

    if log_files:
        latest_log = log_files[0]  # Берём последний файл
        with open(latest_log, 'r', encoding='utf-8') as f:
            logs = f.readlines()  # Считываем строки из файла
    else:
        logs = []  # Если файлов нет, возвращаем пустой список

    return render(request, 'logs_playme.html', {'logs': logs})
