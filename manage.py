#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from environs import Env
import config


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'playme_chatbot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Используем порт из config.py
    if len(sys.argv) == 2 and sys.argv[1] == "runserver":
        sys.argv.append(f"0.0.0.0:{getattr(config, 'DJANGO_PORT', 8000)}")

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
