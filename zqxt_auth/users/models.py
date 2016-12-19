# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)

from .conf import settings
from .managers import UserManager, UserInheritanceManager
from django.utils.encoding import python_2_unicode_compatible

from django.contrib.auth.models import Group


@python_2_unicode_compatible
class AbstractUser(AbstractBaseUser, PermissionsMixin):
    USERS_AUTO_ACTIVATE = not settings.USERS_VERIFY_EMAIL

    username = models.CharField(_('username'), unique=True, db_index=True, max_length=50)
    email = models.EmailField(_('email address'), unique=True, db_index=True)

    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))

    is_active = models.BooleanField(
        _('active'), default=USERS_AUTO_ACTIVATE,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    user_type = models.ForeignKey(ContentType, null=True, editable=False)

    objects = UserInheritanceManager()
    base_objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        abstract = True

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s (%s)' % (self.real_name, self.username)
        return full_name.strip()

    full_name = property(get_full_name)

    def get_short_name(self):
        "Returns the short name for the user."
        return self.real_name if self.real_name.strip() else self.username

    def email_user(self, subject, message, from_email=None):
        """ Send an email to this User."""
        send_mail(subject, message, from_email, [self.email])

    def activate(self):
        self.is_active = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.user_type_id:
            self.user_type = ContentType.objects.get_for_model(
                self, for_concrete_model=False)
        super(AbstractUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.real_name if (self.real_name and self.real_name.strip()) else self.username


class User(AbstractUser):

    """
    # @Date    : 2015-03-09 17:19:49
    # @Author  : Weizhong Tu (mail@tuweizhong.com)
    # @Link    : http://www.tuweizhong.com

    Concrete class of AbstractUser.
    Use this if you don't need to extend User.
    """
    real_name = models.CharField(_('real name'), max_length=60, blank=True)

    def in_group(self, *group_name):
        '''
        usage: inGroup(user,'Inputer',...)
        return: True or False
        '''
        usr_grps = set([g.name for g in self.groups.all()])
        if set(group_name) <= usr_grps:
            return True
        return False

    def change_to_group(self, group_name, create_group=False):
        if create_group:
            _group = Group.objects.get_or_create(name=group_name)[0]
        else:
            _group = Group.objects.get(name=group_name)
        self.groups.add(_group)
        self.save()

    @property
    def is_inputer(self):
        return self.in_group('Inputer')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
