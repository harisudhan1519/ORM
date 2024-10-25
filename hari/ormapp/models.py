from django.db import models
from django.contrib import admin
class bankloan(models.Model):
          name=models.CharField(max_length=10)
          loanno=models.IntegerField(primary_key="Loanno")
          loanamnt=models.IntegerField()
          dob=models.DateField()
          phone=models.IntegerField()         
class bankloanAdmin(admin.ModelAdmin):
          list_display=("name","loanno","loanamnt","dob","phone")