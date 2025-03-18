from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):
    def setUp(self):
        self.User = get_user_model()

    def test_create_user(self):
        user = self.User.objects.create_user(
            username="michael", email="michael@gmail.com", password="greatSecurePassword123"
        )
        self.assertEqual(user.username, "michael")
        self.assertEqual(user.email, "michael@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        # Custom fields test If not set test default field values
        self.assertFalse(user.has_done)

    def test_create_superuser(self):
        admin_user = self.User.objects.create_superuser(
            username="michaelAdmin", email="michaelAdmin@gmail.com", password="EvengreaterSecurePassword123"
        )
        self.assertEqual(admin_user.username, "michaelAdmin")
        self.assertEqual(admin_user.email, "michaelAdmin@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        self.assertFalse(admin_user.has_done)


    def test_custom_user_fields(self):
        # Dedicated function for testing out the custom fields of the user model
        user = self.User.objects.create_user(
            username="CustomMichael", email="CustomMichael@gmail.com", password="CustomSecurePassword123",
            # Custom fields
            has_done=True
        )
        self.assertTrue(user.has_done)

