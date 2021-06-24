from django.db import models
from django.utils.translation import gettext as _


class Details(models.Model):

    name = models.CharField(_("name"), max_length=255)
    age = models.CharField(_("age"), max_length=255)
