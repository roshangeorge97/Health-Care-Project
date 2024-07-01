from django.db import models

class Doctor(models.Model):
    first_name = models.CharField("First Name", max_length=122, null=False, blank=False)
    last_name = models.CharField("Last Name", max_length=122, null=False, blank=False)
    username = models.CharField("Username", max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField("Email ID", unique=True, null=False, blank=False)
    address_line1 = models.CharField("Address Line 1", max_length=255, null=False, blank=False)
    city = models.CharField("City", max_length=50, null=False, blank=False)
    state = models.CharField("State", max_length=50, null=False, blank=False)
    pincode = models.CharField("Pincode", max_length=10, null=False, blank=False)
    image = models.ImageField(upload_to='pics',default='default.svg')

    def natural_key(self):
        return self.email

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Patient(models.Model):
    first_name = models.CharField("First Name", max_length=122, null=False, blank=False)
    last_name = models.CharField("Last Name", max_length=122, null=False, blank=False)
    username = models.CharField("Username", max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField("Email ID", unique=True, null=False, blank=False)
    address_line1 = models.CharField("Address Line 1", max_length=255, null=False, blank=False)
    city = models.CharField("City", max_length=50, null=False, blank=False)
    state = models.CharField("State", max_length=50, null=False, blank=False)
    pincode = models.CharField("Pincode", max_length=10, null=False, blank=False)
    image = models.ImageField(upload_to='pics',default='default.svg')
    
    def natural_key(self):
        return self.email

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
