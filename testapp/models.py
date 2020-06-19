from django.db import models

# Create your models here.
class TestTable(models.Model):
  name = models.CharField(max_length=10)

  def __self__(self):
    return self.name
