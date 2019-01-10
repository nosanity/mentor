from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from mentor.utils.roles import tags_mapper


class Role(models.Model):
    slug = models.SlugField(unique=True)

    @classmethod
    def get_role(cls, role):
        return cls.objects.get_or_create(slug=role)[0]

    @classmethod
    def get_role_for_tag(cls, tag):
        role_slug = tags_mapper.get(tag)
        if role_slug:
            return cls.get_role(role_slug)

    def __str__(self):
        return self.slug


class User(AbstractUser):
    second_name = models.CharField(max_length=50)
    unti_id = models.PositiveIntegerField(null=True, db_index=True)
    leader_id = models.CharField(max_length=255, default='')
    role = models.ManyToManyField(Role, blank=True)

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')

    def __str__(self):
        return '%s %s' % (self.unti_id, self.get_full_name())


class HomePage(Page):
    subpage_types = ['mentor.EventsIndexPage', 'mentor.SimplePage']
    max_count = 1

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = _('Главная страница')


class EventsIndexPage(Page):
    subpage_types = ['mentor.EventPage']
    max_count = 1

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = _('Список событий')


class EventPage(Page):
    parent_page_types = ['mentor.EventsIndexPage']
    subpage_types = []

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = _('Событие')
        verbose_name_plural = _('События')


class SimplePage(Page):
    parent_page_types = ['mentor.HomePage']
    subpage_types = []

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = _('Простая страница')
