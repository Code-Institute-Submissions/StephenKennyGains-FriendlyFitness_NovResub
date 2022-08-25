""" Profiles App Apps section """
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """ Profile app settings """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
