from __future__ import unicode_literals

from django.db import models
<<<<<<< HEAD
from django.contrib.sites.models import Site
from django_countries.fields import CountryField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
=======
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266


class Approval(models.Model):
    approved = models.BooleanField(default=False)

    class Meta:
        permissions = (
            ('view_approval', 'Can view approval'),
        )
