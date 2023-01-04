from django.urls import reverse
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
Classes = (
        ("Nur1","Nursery 1"),
        ("Nur2","Nursery 2"),
        ("Nur3","Nursery 2"),
        ("Pry1","Primary 1"),
        ("Pry2","Primary 2"),
        ("Pry3","Primary 3"),
        ("Pry4","Primary 4"),
        ("Pry5","Primary 5"),

    )


class School(models.Model): 
    
    surname = models.CharField(max_length=20, blank=False, null=True)
    First_Name = models.CharField(max_length=20, blank=False, null=True)
    Other_Name = models.CharField(max_length=20, blank=False, null=True)
    Date_of_Birth = models.DateField()
    postal_address = models.CharField(max_length=50, blank=False, null=True)
    Residential_Address = models.CharField(max_length=50, blank=False, null=True)
    Latest_school_addresss = models.CharField(max_length=50, blank=False, null=True)
    Latest_class_Attended = models.CharField(max_length=20,choices=Classes,default="Nur1")
    Home_telephone_number = PhoneNumberField(blank=False, null=True)
    name_of_father = models.CharField(max_length=20, blank=False, null=True)
    Occupation_of_Father = models.CharField(max_length=20, blank=False, null=True)
    Contact_address_of_Father = models.CharField(max_length=20, blank=False, null=True)
    tel_No_of_Father = PhoneNumberField(blank=False, null=True)
    name_of_mother = models.CharField(max_length=20, blank=False, null=True)
    Occupation_of_mother = models.CharField(max_length=20, blank=False, null=True)
    Contact_address_of_mother = models.CharField(max_length=20, blank=False, null=True)
    tel_No_of_mother = PhoneNumberField(blank=False, null=True)
    who_to_call_in_case_of_emergency = models.CharField(max_length=20, blank=False, null=True)
    any_allergy_or_physical_deafect = models.CharField(max_length=20)
    picture = models.ImageField(upload_to="images/")



    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse("formdetail")


    