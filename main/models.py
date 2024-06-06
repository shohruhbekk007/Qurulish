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
    monthTomoney = models.CharField(max_length=25)

    def get_money(self):
        return self.money / self.month


    def __str__(self) -> str:
        return f"{self.full_name}"

    

