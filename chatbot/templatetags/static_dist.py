import os
from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def dist_static(filename_prefix, file_ext):
    """
    Возвращает путь к последнему собранному файлу из BoltInterface/dist/assets
    на основе префикса имени файла (например, 'index') и расширения.
    """
    dist_path = os.path.join(settings.BASE_DIR, "BoltInterface", "dist", "assets")
    try:
        for file in os.listdir(dist_path):
            if file.startswith(filename_prefix) and file.endswith(file_ext):
                return f"/static/assets/{file}"
    except FileNotFoundError:
        return ""  # Возвращаем пустую строку, если путь недоступен
    return ""
