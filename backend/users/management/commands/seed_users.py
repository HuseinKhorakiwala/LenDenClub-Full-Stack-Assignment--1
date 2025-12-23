from django.core.management.base import BaseCommand
from users.models import User
from users.encryption import encrypt_value
import random

class Command(BaseCommand):
    help = "Seed database with dummy users and encrypted Aadhaar data"

    def handle(self, *args, **kwargs):
        for i in range(1, 51):
            username = f"user{i:02d}"
            email = f"user{i:02d}@test.com"
            aadhaar = f"{random.randint(100000000000, 999999999999)}"

            if User.objects.filter(username=username).exists():
                continue

            user = User.objects.create_user(
                username=username,
                email=email,
                password="test1234"
            )

            user.aadhaar_encrypted = encrypt_value(aadhaar)
            user.save()

        self.stdout.write(self.style.SUCCESS("50 dummy users created successfully"))
