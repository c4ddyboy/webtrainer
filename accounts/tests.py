from django.test import TestCase

from django.contrib.auth import get_user_model
#from accounts.tests import add


class AccountsTests(TestCase):

    def test_create_user(self):
        """Test that user can be created"""
        username = 'testuser'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            username=username,
            password='password'
        )
        
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))