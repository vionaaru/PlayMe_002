from django.shortcuts import render

def home(request):
    """Главная страница навигации"""
    return render(request, 'home.html')

def chatbot(request):
    """Страница чата"""
    return render(request, 'chatbot.html')

def logs_playme(request):
    """Страница логов"""
    # Открываем файл логов (например, playme_logs.log)
    try:
        with open('playme_logs.log', 'r') as log_file:
            logs = log_file.readlines()
    except FileNotFoundError:
        logs = ["Файл логов не найден."]

    return render(request, 'logs_playme.html', {'logs': logs})
