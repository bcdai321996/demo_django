from django.apps import AppConfig
from utils import global_func_load
import sys


class AppGlobalConfig(AppConfig):
    name = 'ProjectChatBot'

    def ready(self):
        try:
            print('<<<<<-------------------------- StartUp --------------------------->>>>>')
            print('========================================================================')


            print('<<<<<--------------------------- Done ----------------------------->>>>>')
            print('========================================================================')

        except Exception as e:
            print('ProjectChatBot.apps.AppGlobalConfig -> ready -> ex: ', e)
            sys.exit(0)

