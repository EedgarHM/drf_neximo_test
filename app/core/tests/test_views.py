from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.contrib.messages.storage.fallback import FallbackStorage

User = get_user_model()


class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_register_user_success(self):
        pass
