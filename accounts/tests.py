from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from django.test import Client

from accounts.forms import CustomUserCreationForm
from accounts.views import SignupPageView


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


class SignUpPageTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_signup_template(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        self.assertContains(response, "Sign up")

    def signup_form(self):
        response = self.client.get("/accounts/signup/")
        form = response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
