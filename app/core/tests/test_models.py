"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """ Testing models """

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = 'email@example.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        """ Test if the email is normalized for new users. """
        sample_email = [
            ['email1@EXAMPLE.com', 'email1@example.com'],
            ['Email2@Example.com', 'Email2@example.com'],
        ]

        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email,'example123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """ Test that creating a user without an emal raises a ValueError. """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','NonUserValueError')

    