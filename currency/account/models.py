import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static

from .managers import UserManager


def user_directory_path(instance, filename):
    return f'avatars/user_{instance.id}/{filename}'


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.FileField(_('Avatar'), default=None, blank=True, null=True, upload_to=user_directory_path)
    phone = models.CharField(_('Phone number'), max_length=15, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    @property
    def avatar_url(self) -> str:
        if self.avatar:
            return self.avatar.url
        return static('anon_user.jpg')

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = uuid.uuid4()
        self.email = self.email.lower()
        instance = super().save(*args, **kwargs)

        return instance
