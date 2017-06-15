from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to = "test")
    

class Event(models.Model):
    JOURNAL = 'jrl'
    EVENT_TYPE = 'evt'
    EVENT_TYPES = (
        ('jrl', 'Journal'),
        ('evt', 'Event'),
    )

    event_name = models.CharField(max_length=200)
    event_description = models.TextField()
    event_type = models.CharField(
        max_length = 2,
        choices = EVENT_TYPES,
        default = EVENT_TYPE,
    )
    event_confidential = models.BooleanField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
