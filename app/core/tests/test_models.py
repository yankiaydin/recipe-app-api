from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is susccessful"""
        email = "test@admin.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
        email = email,
        password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email= 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(email,'test123')
        self.assertEqual(user.email, email.lower())

    def test_user_have_no_email(self):
        """Test the error if user has no email"""
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(None,"test123")

    def test_create_superuser(self):
        """Test that creating a new superuser"""
        email = "test@admin.com"
        password = "testpass123"
        user = get_user_model().objects.create_superuser(email, password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
