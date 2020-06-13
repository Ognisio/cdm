from django.contrib import admin
from .models import Nation, State, District, Panchayat, Ward, Gender, Customer, Customer_document, Checkin, Checkout, Company_master, Pricing_plan, Settings, User_role, Role_permission, User
# Register your models here.

cdmModels = [Nation, State, District, Panchayat, Ward, Gender, Customer, Customer_document, Checkin, Checkout, Company_master, Pricing_plan, Settings, User_role, Role_permission, User]

admin.site.register(cdmModels)

