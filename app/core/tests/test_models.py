from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

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

def sample_user(email='test@londonappdev.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

def test_tag_str(self):
    """Test the tag string representation"""
    tag = models.Tag.objects.create(
        user=sample_user(),
        name='Vegan'
    )

    self.assertEqual(str(tag), tag.name)

def test_ingredient_str(self):
    """Test the ingredient string representation"""
    ingredient = models.Ingredient.objects.create(
        user=sample_user(),
        name='Cucumber'
    )

    self.assertEqual(str(ingredient), ingredient.name)

def test_recipe_str(self):
    """Test the recipe string representation"""
    recipe = models.Recipe.objects.create(
        user=sample_user(),
        title='Steak and mushroom sauce',
        time_minutes=5,
        price=5.00
    )

    self.assertEqual(str(recipe), recipe.title)
