from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from conferences.models import Conference
<<<<<<< HEAD
import uuid
=======
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266


class Submission(models.Model):
#    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    node_id = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
<<<<<<< HEAD
    contributor = models.ForeignKey(User, related_name='submission_contributor')
    description = models.TextField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    approval = models.OneToOneField('approvals.Approval')
    #conference = models.ForeignKey(Conference, related_name="conference", on_delete=models.CASCADE)
=======
    contributor = models.ForeignKey(
        User, blank=True, related_name="contributor")
    description = models.TextField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    approval = models.OneToOneField('approvals.Approval')
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266

    class Meta:
        ordering = ('date_created',)
        permissions = (
<<<<<<< HEAD
            ('can_set_contributor', 'Can set the contributor for a submission'),
=======
            ('can_set_contributor',
             'Can set the contributor for a submission'),
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266
            ('view_submission', 'Can view submission'),
        )
