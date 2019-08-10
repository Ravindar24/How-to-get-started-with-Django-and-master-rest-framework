from django.db import models

# Create your models here.

'''
@Author Ravindar Sharma

Description About models.py

A models.py is just a simple python file which basically
is created for each django application for ORM.

ORM is a paradigm to proceess and deal with objects and database with CRUD opertions.

All the fields defined in the class will act as columns of the table.
class name will be used as table name

'''
class CustomerInformation(models.Model):
    
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    gender = models.CharField(max_length = 10)
    address = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 50)
    contact_number = models.IntegerField()
    pin_code =  models.IntegerField()


    def __init__(self,\
                 first_name,\
                 last_name,\
                 gender,\
                 address,\
                 email,\
                 contact_number,\
                 pin_code):

        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.address = address
        self.email = email
        self.contact_number = contact_number
        self.pin_code = pin_code












