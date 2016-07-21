from rest_framework_json_api import serializers
<<<<<<< HEAD
from rest_framework.reverse import reverse

from approvals.models import Approval
from django.contrib.auth.models import User

class ApprovalSerializer(serializers.ModelSerializer):
=======
from approvals.models import Approval


class ApprovalSerializer(serializers.ModelSerializer):

>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266
    class Meta:
        model = Approval
