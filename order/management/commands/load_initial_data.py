import os

from django.conf import settings
from django.core import management
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Loads initial data required for a new database.'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('app', type=str)

        # Named (optional) arguments
        parser.add_argument(
                '--migrate',
                action='store_true',
                help="Create the required migration if it doesn't exists",
                )

    @staticmethod
    def make_migrations(path):
        os.makedirs(path)
        with open(f'{path}/__init__.py', mode='w') as f:
            f.write('')

        management.call_command('makemigrations')

    def handle(self, *args, **options):
        app = options.get('app')
        path_to_app = os.path.join(settings.BASE_DIR, app)

        if options.get('migrate'):
            if not os.path.exists(f'{app}/migrations'):
                self.make_migrations(f'{app}/migrations')
                management.call_command('migrate', app)

        fixtures = os.listdir(f'{path_to_app}/fixtures')
        if fixtures:
            fixtures = [f'{path_to_app}/fixtures/{fixture}' for fixture in fixtures]
            management.call_command('loaddata', *fixtures)
        else:
            self.stdout.write(self.style.ERROR(f'No fixtures detected under {app}/fixtures/'))
