from django.db import models

# Create your models here.

class Nation(models.Model):
  full_name = models.CharField(max_length=50)
  short_name = models.CharField(max_length=3)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=False)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)

  def __self__(self):
    return self.full_name

class State(models.Model):
  full_name = models.CharField(max_length=50)
  short_name = models.CharField(max_length=3)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)
  nation = models.ForeignKey('Nation', on_delete=models.CASCADE)

  def __self__(self):
    return self.full_name

class District(models.Model):
  full_name = models.CharField(max_length=50)
  short_name = models.CharField(max_length=3)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)
  state = models.ForeignKey('State', on_delete=models.CASCADE)

  def __self__(self):
    return self.full_name

class Panchayat(models.Model):
  full_name = models.CharField(max_length=50)
  short_name = models.CharField(max_length=3)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)
  district = models.ForeignKey('District', on_delete=models.CASCADE)

  def __self__(self):
    return self.full_name

class Ward(models.Model):
  full_name = models.CharField(max_length=50)
  short_name = models.CharField(max_length=3)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)
  panchayat = models.ForeignKey('Panchayat', on_delete=models.CASCADE)

  def __self__(self):
    return self.full_name

class Gender(models.Model):
  name = models.CharField(max_length=10)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)

  def __self__(self):
    return self.name

class Customer(models.Model):
  name = models.CharField(max_length=50)
  phone = models.CharField(max_length=10)
  email = models.CharField(max_length=50)
  street = models.CharField(max_length=50)
  house = models.CharField(max_length=50)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)
  gender = models.ForeignKey('Gender', on_delete=models.CASCADE)
  nation = models.ForeignKey('Nation', on_delete=models.CASCADE)
  state = models.ForeignKey('State', on_delete=models.CASCADE)
  district = models.ForeignKey('District', on_delete=models.CASCADE)
  panchayat = models.ForeignKey('Panchayat', on_delete=models.CASCADE)
  ward = models.ForeignKey('Ward', on_delete=models.CASCADE)

  def __self__(self):
    return self.name

class Customer_document(models.Model):
  document_name = models.CharField(max_length=10)
  document_file = models.FileField(upload_to='customers/documents/')
  document_type = models.CharField(max_length=10)
  document_size = models.CharField(max_length=10)
  customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)
  
  def __self__(self):
    return self.customer

class Checkin(models.Model):
  customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
  is_active = models.BooleanField(default=True)
  checkin = models.DateTimeField(auto_now_add=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)

  def __self__(self):
    return self.customer

class Checkout(models.Model):
  customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
  is_active = models.BooleanField(default=True)
  checkout = models.DateTimeField(auto_now_add=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)

  def __self__(self):
    return self.customer

class Company_master(models.Model):
  registred_name = models.CharField(max_length=75)
  brand_name = models.CharField(max_length=75)
  email = models.CharField(max_length=50)
  phone = models.CharField(max_length=10)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)

  def __self__(self):
    return self.registred_name

class Pricing_plan(models.Model):
  name = models.CharField(max_length=75)
  price = models.CharField(max_length=75)
  maximum_user = models.CharField(max_length=75)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)

  def __self__(self):
    return self.name

class Settings(models.Model):
  license_from = models.DateTimeField()
  license_to = models.DateTimeField()
  plan = models.ForeignKey('Pricing_plan', on_delete=models.CASCADE)
  is_active = models.BooleanField(default=True) 
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)

  def __self__(self):
    return self.license_from

class User_role(models.Model):
  name = models.CharField(max_length=75)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)

  def __self__(self):
    return self.name

class Role_permission(models.Model):
  name = models.CharField(max_length=75)
  role = models.ForeignKey('User_role', on_delete=models.CASCADE)
  is_allow = models.BooleanField(default=True)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)

  def __self__(self):
    return self.role
    
class User(models.Model):
  username = models.CharField(max_length=75)
  password = models.CharField(max_length=75)
  is_active = models.BooleanField(default=True)
  date_created =  models.DateTimeField(auto_now_add=True)
  date_created_by = models.CharField(max_length=10, default=0, blank=True)
  date_updated =  models.DateTimeField(auto_now_add=True)
  updated_by = models.CharField(max_length=10, default=0, blank=True)
  company = models.ForeignKey('Company_master', on_delete=models.CASCADE)
  role = models.ForeignKey('User_role', on_delete=models.CASCADE)


  def __self__(self):
    return self.username