from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class RecipePage(Page):
    description = RichTextField(blank=True, max_length=200, features=['bold', 'italic', 'link'])
    ingredients = RichTextField(features=['bold', 'italic', 'link', 'ul'])
    body = RichTextField(features=['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'ol'])

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
