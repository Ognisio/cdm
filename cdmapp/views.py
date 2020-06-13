from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from cdmapp import models
from cdmapp import serializers
 
class NationViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.NationSerializer
  queryset = {}
  queryset = models.Nation.objects.filter().order_by(('id'))

class StateViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.StateSerializer
  queryset = {}
  queryset = models.State.objects.filter().order_by(('id'))

class DistrictViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.DistrictSerializer
  queryset = {}
  queryset = models.District.objects.filter().order_by(('id'))

class PanchayatViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.PanchayatSerializer
  queryset = {}
  queryset = models.Panchayat.objects.filter().order_by(('id'))

class WardViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.WardSerializer
  queryset = {}
  queryset = models.Ward.objects.filter().order_by(('id'))

class GenderViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.GenderSerializer
  queryset = {}
  queryset = models.Gender.objects.filter().order_by(('id'))

class CustomerViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.CustomerSerializer
  queryset = {}
  queryset = models.Customer.objects.filter().order_by(('id'))

class CustomerDocumentViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.CustomerDocumentSerializer
  queryset = {}
  queryset = models.Customer_document.objects.filter().order_by(('id'))

class CheckinMasterViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.CheckinMasterSerializer
  queryset = {}
  queryset = models.Checkin.objects.filter().order_by(('id'))

class CheckoutMasterViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.CheckoutMasterSerializer
  queryset = {}
  queryset = models.Checkout.objects.filter().order_by(('id'))

class CompanyMasterViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.CompanyMasterSerializer
  queryset = {}
  queryset = models.Company_master.objects.filter().order_by(('id'))

class PricingPlanViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.PricingPlanSerializer
  queryset = {}
  queryset = models.Pricing_plan.objects.filter().order_by(('id'))

class SettingsViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.SettingsSerializer
  queryset = {}
  queryset = models.Settings.objects.filter().order_by(('id'))

class UserRoleViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UserRoleSerializer
  queryset = {}
  queryset = models.User_role.objects.filter().order_by(('id'))

class RolePermissionViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.RolePermissionSerializer
  queryset = {}
  queryset = models.Role_permission.objects.filter().order_by(('id'))

class UserViewSet(viewsets.ModelViewSet):
  serializer_class = serializers.UserSerializer
  queryset = {}
  queryset = models.User.objects.filter().order_by(('id'))