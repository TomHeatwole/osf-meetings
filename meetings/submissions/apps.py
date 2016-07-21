from __future__ import unicode_literals

from django.apps import AppConfig


class SubmissionAppConfig(AppConfig):
    name = 'submissions'

    def ready(self):
<<<<<<< HEAD
        import submissions.signals
=======
        import submissions.signals  # noqa
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266
