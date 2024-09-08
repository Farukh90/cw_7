import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from users.models import User

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv("SU_EMAIL"),
            first_name="admin",
            last_name="test",
            is_staff=True,
            is_superuser=True,
        )

        user.set_password(os.getenv("SU_PASS"))
        user.save()
