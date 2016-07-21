from __future__ import unicode_literals

from django.apps import AppConfig


class ApprovalsConfig(AppConfig):
    name = 'approvals'

    def ready(self):
<<<<<<< HEAD
        import approvals.signals
=======
        import approvals.signals  # noqa
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266
