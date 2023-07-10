from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.messages.storage.fallback import FallbackStorage
from django.contrib import messages

from app.views import register_user
from app.forms import RegistrationForm

User = get_user_model()

class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_register_user_success(self):
        pass