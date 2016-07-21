from __future__ import unicode_literals

from django.apps import AppConfig


class ConferenceAppConfig(AppConfig):
    name = 'conferences'

    def ready(self):
<<<<<<< HEAD
        import conferences.signals
=======
        import conferences.signals  # noqa
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266
