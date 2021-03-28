import os

from django.conf import settings
from django.core import management
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Loads initial data required for a new database.'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('app', type=str)

    def handle(self, *args, **options):
        app = options.get('app')
        fixtures_path = os.path.join(settings.BASE_DIR, app, 'fixtures')
        fixtures = os.listdir(fixtures_path)

        if fixtures:
            for i in range(len(fixtures)):
                absolute_path = os.path.join(fixtures_path, fixtures[i])
                fixtures[i] = absolute_path

            management.call_command('loaddata', *fixtures)
        else:
            self.stdout.write(
                    self.style.ERROR(
                            f'No fixtures detected under {app}/fixtures/'
                            )
                    )
