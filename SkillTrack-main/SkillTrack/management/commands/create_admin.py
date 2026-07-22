from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create an admin account for the SkillTrack application'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Admin username')
        parser.add_argument('--email', type=str, help='Admin email')
        parser.add_argument('--password', type=str, help='Admin password')

    def handle(self, *args, **options):
        self.stdout.write('Creating admin account...')

        # Get user input from arguments or prompt
        username = options.get('username') or input('Enter username: ')
        email = options.get('email') or input('Enter email: ')
        password = options.get('password')

        if not password:
            from getpass import getpass
            password = getpass('Enter password: ')
            confirm_password = getpass('Confirm password: ')
            if password != confirm_password:
                self.stdout.write(self.style.ERROR('Passwords do not match.'))
                return

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR('Username already exists.'))
            return

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR('Email already exists.'))
            return

        # Create admin user
        try:
            admin_user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                role=User.Role.ADMIN,
                is_staff=True,
                is_superuser=True
            )
            admin_user.save()
            self.stdout.write(self.style.SUCCESS(f'Admin account "{username}" created successfully!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating admin account: {str(e)}'))
