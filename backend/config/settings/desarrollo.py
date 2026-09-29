from .base import *

DEBUG = True

PRODUCCION = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "quizdb",
        "USER": "quiz",
        "PASSWORD": "pspassword",
        "HOST": "db",
        "PORT": "3306",
    }
}

CORS_ORIGIN_ALLOW_ALL = True
#CORS_ALLOW_ALL_ORIGINS = True

# Opción 2: Especificar explícitamente el origen de tu app en Vue
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173", # Cambia al puerto donde corre tu Vue (Vite suele usar el 5173)
]