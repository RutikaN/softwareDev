# your_app/management/commands/create_default_user.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Ensure the default user exists'

    def handle(self, *args, **options):
        default_user, created = User.objects.get_or_create(pk=1, defaults={
            'username': 'admin',
            'email': 'admin@example.com',
            'is_superuser': True,
            'is_staff': True,
        })

        if created:
            self.stdout.write(self.style.SUCCESS('Default user created successfully!'))
        else:
            self.stdout.write(self.style.WARNING('Default user already exists!'))
