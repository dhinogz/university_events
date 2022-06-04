"""
Event app tests
"""
from datetime import datetime
from django.test import TestCase
from .models import Area, Major, Event


class EventTestCase(TestCase):
    def setup(self):
        """Set up relevant event date"""
        area = Area.objects.create(
            name="Ingenieria",
            slug="ingenieria",
        )

        major = Major.objects.create(
            name="ITC",
            slug="itc",
            area=area,
        )

        Event.objects.create(
            title="IT World",
            location="Tecnologico de Monterrey",
            start_date=datetime.date(2022, 5, 16),
            end_date=datetime.date(2022, 5, 18),
            on_sale_date=datetime.date(2022, 5, 10),
            start_time=datetime.time(hour=15, minute=30),
            end_time=datetime.time(hour=19, minute=15),
            is_online=False,
            description="Congreso de tecnologia: conoce mas sobre tu carrera",
            venue="Centro de congresos",
            capacity=100,
            is_over=False,
            major=major,
        )

    def test_event(self):
        """Test basic event data"""
        area_ingenieria = Area.objects.get(name="Ingenieria")
        major_itc = Major.objects.get(name="ITC")
        event_it_world = Event.objects.get(name="IT World")
