from django.db import models

# Create your models here.

class Costumer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    father_name = models.CharField(max_length=25)
    phone_number= models.CharField(max_length=25)
    mavzu = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return self.first_name
    

class City(models.Model):
    name = models.CharField(max_length=70)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name
    
    
class Contract(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.CASCADE)
    full_name = models.ForeignKey(to=Costumer, on_delete=models.CASCADE)
    room = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    money = models.PositiveBigIntegerField()
    month = models.PositiveIntegerField()
    advance_payment = models.PositiveBigIntegerField(null=True, blank=True, default=0)
    monthTomoney = models.CharField(max_length=25, editable=False)  # Faqat o'qish uchun

    def save(self, *args, **kwargs):
        if self.month > 0:
            self.monthTomoney = "{:.2f}".format((self.money - self.advance_payment) / self.month)
        else:
            self.monthTomoney = "Invalid input"
        super().save(*args, **kwargs)
    


    def __str__(self) -> str:
        return f"{self.full_name}"

# class ProfileMod(models.Model):
#     name = models.ForeignKey(to=Costumer,on_delete=models.CASCADE)
#     user_number=models.ForeignKey(to=Costumer,on_delete=models.CASCADE)
#     duty = models.IntegerField()

#     def __str__(self) -> str:
#         return self.name