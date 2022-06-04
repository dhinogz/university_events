"""
Test for models.
"""

from django.test import TestCase
from django.contrib.auth import get_user_model

from core.models import Event, Area, Major, Tag

from datetime import date, datetime, time


class ModelTests(TestCase):
    """Test models"""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test3@example.COM", "test3@example.com"],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email(self):
        """Test that creating a user without an email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        """test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_event(self):
        """Test creating an event is successful."""
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpass123',
        )
        event = Event.objects.create(
            user=user,
            title='IT World',
            description='An event for technology enthusiast.',
            location='Tec de Monterrey',
            date=date(2022, 5, 10),
            start_time=time(15, 30, 0),
            end_time=time(17, 0, 0),
            is_online=False,
            zoom_link='',
            on_sale_date=datetime(2022, 5, 5),
            venue='Centro de Congresos',
            capacity=100,
        )
        self.assertEqual(str(event), 'IT World')

    def test_create_major(self):
        """Test creating a major is successful."""
        major = Major.objects.create(
            name='ITC',
            slug='itc',
        )

        self.assertEqual(major.name, str(major))

    def test_create_tag(self):
        """Test creating a tag is successful."""
        tag = Tag.objects.create(name='Tag1')

        self.assertEqual(str(tag), tag.name)

        