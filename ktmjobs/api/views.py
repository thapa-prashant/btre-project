from rest_framework import  viewsets,permissions
from rest_framework.permissions import DjangoObjectPermissions

from realtors.models import Realtor
from listings.models import Listing
from .serializers import  ListingSerializer,RealtorSerializer

class ListingView(viewsets.ModelViewSet):
    queryset=Listing.objects.all()
    serializer_class = ListingSerializer
   # permission_classes = (permissions.IsAuthenticatedOrReadOnly,permissions.DjangoModelPermissionsOrAnonReadOnly)

class RealtorView(viewsets.ModelViewSet):
    queryset=Realtor.objects.all()
    serializer_class = RealtorSerializer

class DjangoObjectPermissionsOrAnonReadOnly(DjangoObjectPermissions):
    authenticated_users_only = False