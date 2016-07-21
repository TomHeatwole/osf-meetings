<<<<<<< HEAD
from django.shortcuts import render
from rest_framework import viewsets, filters, permissions
=======
from rest_framework import viewsets, filters
>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266
from approvals.models import Approval
from approvals.serializers import ApprovalSerializer
from approvals.permissions import ApprovalPermissions

# Create your views here.

<<<<<<< HEAD
=======

>>>>>>> cb7e5d34aa161ab329f7fcedcbe5f511bbb34266
class ApprovalViewSet(viewsets.ModelViewSet):
    resource_name = 'approvals'
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer
    filter_backends = (filters.DjangoObjectPermissionsFilter,)
    permission_classes = (ApprovalPermissions,)
