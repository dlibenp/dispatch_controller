from django.apps import AppConfig


class DroneApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drone_api'

    def ready(self) -> None:
        print('Start scheduler')
        from . import battery_level_task
        battery_level_task.background_task()
