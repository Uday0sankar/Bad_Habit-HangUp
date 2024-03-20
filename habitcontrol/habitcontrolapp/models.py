from django.db import models

# Create your models here.
class Habits(models.Model):
    hab_img=models.ImageField(upload_to='pics')
    hab_name=models.CharField(max_length=150)
    
class Councilor(models.Model):
    coun_img=models.ImageField(upload_to='pics')
    coun_name=models.CharField(max_length=55)

    def __str__(self):
         return self.coun_name
    
class Booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_ph=models.CharField(max_length=12)
    coun_name=models.ForeignKey(Councilor,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)