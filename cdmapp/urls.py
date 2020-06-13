from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
  NationViewSet,
  StateViewSet,
  DistrictViewSet,
  PanchayatViewSet,
  WardViewSet,
  GenderViewSet,
  CustomerViewSet,
  CustomerDocumentViewSet,
  CheckinMasterViewSet,
  CheckoutMasterViewSet,
  CompanyMasterViewSet,
  PricingPlanViewSet,
  SettingsViewSet,
  UserRoleViewSet,
  RolePermissionViewSet,
  UserViewSet,
)

router = DefaultRouter()
router.register('nation', NationViewSet)
router.register('state', StateViewSet)
router.register('district', DistrictViewSet)
router.register('panchayath', PanchayatViewSet)
router.register('ward', WardViewSet)
router.register('gender', GenderViewSet)
router.register('customer', CustomerViewSet)
router.register('customerdocument', CustomerDocumentViewSet)
router.register('checkin', CheckinMasterViewSet)
router.register('checkout', CheckoutMasterViewSet)
router.register('company', CompanyMasterViewSet)
router.register('plans', PricingPlanViewSet)
router.register('settings', SettingsViewSet)
router.register('userrole', UserRoleViewSet)
router.register('rolepermission', RolePermissionViewSet)
router.register('user', UserViewSet)

urlpatterns = [
  path('', include(router.urls)),
]