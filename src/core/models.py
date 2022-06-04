"""
Database models.
"""

from config import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from datetime import date, datetime
from django.utils.translation import gettext as _


class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save, and return a new user"""
        if not email:
            raise ValueError("User requieres an email")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"


class Area(models.Model):
    """Area object. One area can have many majors."""

    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name = _("Area")
        verbose_name_plural = _("Areas")

    def __str__(self):
        return self.name


class Major(models.Model):
    """Major object. Many events can have many majors."""

    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name = _("Major")
        verbose_name_plural = _("Majors")

    def __str__(self):
        return self.name


class Event(models.Model):
    """Event object."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255, verbose_name=_("title"))
    description = models.TextField(verbose_name=_("description"))
    location = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("location"),
    )
    date = models.DateField(verbose_name=_("date"))
    start_time = models.TimeField(verbose_name=_("start time"))
    end_time = models.TimeField(verbose_name=_("end time"))
    is_online = models.BooleanField(
        verbose_name=_("online"),
        help_text=_("Is event online?"),
    )
    zoom_link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("zoom link"),
    )
    on_sale_date = models.DateField(verbose_name=_("on sale date"))
    venue = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("venue"),
    )
    capacity = models.IntegerField(verbose_name=_("capacity"))
    major = models.ManyToManyField(
        'Major',
        related_name="events",
        verbose_name=_("major"),
    )
    

    def is_ready_to_publish(self):
        """Return true if event is ready to be published."""
        return self.on_sale_date >= datetime.now()

    def days_left(self):
        """Returns days left for event."""
        return date.now() - self.date

    def is_over(self):
        """Returns true if the event is over."""
        return datetime.combine(self.date, self.end_time) < datetime.now()

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.title


# class EventTime(models.Model):
#     """Multiple EventTime tables are related to one event"""
#     date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.date}: {self.start_time} - {self.end_time}'
