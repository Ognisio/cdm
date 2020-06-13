from rest_framework import serializers, fields
# from .models import Nation
from cdmapp.models import (
  Nation,
  State,
  District,
  Panchayat,
  Ward,
  Gender,
  Customer,
  Customer_document,
  Checkin,
  Checkout,
  Company_master,
  Pricing_plan,
  Settings,
  User_role,
  Role_permission,
  User
)

class NationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Nation
    fields =  "__all__"
    
class StateSerializer(serializers.ModelSerializer):
  class Meta:
    model = State
    fields =  "__all__"

class DistrictSerializer(serializers.ModelSerializer):
  class Meta:
    model = District
    fields =  "__all__"

class PanchayatSerializer(serializers.ModelSerializer):
  class Meta:
    model = Panchayat
    fields =  "__all__"

class WardSerializer(serializers.ModelSerializer):
  class Meta:
    model = Ward
    fields =  "__all__"

class GenderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Gender
    fields =  "__all__"

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields =  "__all__"

class CustomerDocumentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer_document
    fields =  "__all__"

class CheckinMasterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Checkin
    fields =  "__all__"

class CheckoutMasterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Checkout
    fields =  "__all__"

class CompanyMasterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Company_master
    fields =  "__all__"

class PricingPlanSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pricing_plan
    fields =  "__all__"

class SettingsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Settings
    fields =  "__all__"

class UserRoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = User_role
    fields =  "__all__"

class RolePermissionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Role_permission
    fields =  "__all__"

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields =  "__all__"