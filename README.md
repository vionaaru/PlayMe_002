# PlayMe Chatbot

PlayMe Chatbot — это проект Django с интеграцией интерфейса Bolt, созданного с использованием React, Vite и TailwindCSS.

## Структура проекта
PlayMe_002/
├── BoltInterface/           # Исходный код интерфейса Bolt
├── chatbot/                 # Django-приложение для обработки логики
├── playme_chatbot/          # Настройки Django
├── static/                  # Статические файлы для Django
└── templates/               # Шаблоны HTML для рендеринга

Запуск проекта
Требования:
Python 3.13
Node.js (рекомендуемая версия: 18.x или выше)
Django 5.1.x
Poetry (для управления зависимостями)

Установка проекта
Клонирование репозитория

bash
Копировать код
git clone https://github.com/vionaaru/PlayMe_002.git
cd PlayMe_002
Настройка виртуального окружения Python

bash
Копировать код
poetry install
poetry shell
Установка зависимостей Bolt Перейдите в папку BoltInterface:

bash
Копировать код
cd BoltInterface
npm install
npm run build
cd ..
Запуск Django-сервера Выполните миграции и запустите сервер:

bash
Копировать код
python manage.py migrate
python manage.py runserver
Особенности
Статические файлы: Интерфейс Bolt собирается в папке BoltInterface/dist и автоматически подключается к Django.
Логи: Все логи сервера записываются в папку logs с таймстемпами.