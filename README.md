# Ex02 Django ORM Web Application
## Date:26.10.24



## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![alt text](<Screenshot (5).png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from Django.contrib import admin
from .models import bankloan,bankloanAdmin
admin.site.register(bankloan,bankloanAdmin)

models.py
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
```



## OUTPUT
![alt text](<Screenshot (4).png>)



Include the screenshot of your admin page.


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
