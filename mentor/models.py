from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    second_name = models.CharField(max_length=50)
    unti_id = models.PositiveIntegerField(null=True, db_index=True)
    leader_id = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name = _(u'Пользователь')
        verbose_name_plural = _(u'Пользователи')

    def __str__(self):
        return '%s %s' % (self.unti_id, self.get_full_name())
