from django.core.management.base import BaseCommand, CommandError
from tcp.server import listen


class Command(BaseCommand):
    help = 'start tcp socket server'

    def handle(self, *args, **options):
        return listen()
