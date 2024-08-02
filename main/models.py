from django.db import models

# Create your models here.


class Costumer(models.Model):
    first_name = models.CharField(max_length=25, verbose_name="Ism")
    last_name = models.CharField(max_length=25, verbose_name="Familya")
    father_name = models.CharField(max_length=25, verbose_name="otasi ism")
    phone_number= models.CharField(max_length=25, verbose_name="Telefon no'mr")
    mavzu = models.CharField(max_length=60, verbose_name="xullosa")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilish vaqti")

    class Meta:
        verbose_name = 'Mijoz'
        verbose_name_plural = 'Mijozlar'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class City(models.Model):
    name = models.CharField(max_length=70, verbose_name="Sotiladigan bino")
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Shahar'
        verbose_name_plural = 'Shaharlar'

    def __str__(self) -> str:
        return self.name
    
class Room(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.CASCADE, verbose_name='Shahar')
    number = models.PositiveIntegerField(verbose_name="Xonalar soni")

    class Meta:
        verbose_name = 'Xona'
        verbose_name_plural = 'Xonalar'

    def __str__(self) -> str:
        return f"{self.city.name} - {self.number}"

    
    
class Contract(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.CASCADE, verbose_name='Sotiladigan bino')
    full_name = models.ForeignKey(to=Costumer, on_delete=models.CASCADE, verbose_name="Xaridor To'liq ismi")
    # room = models.PositiveIntegerField(verbose_name="Uy xonalar soni")
    # passport = models.CharField(max_length=250, verbose_name="passport nomr uchun")
    # phone_number = models.CharField(max_length=20, verbose_name="Telefon nomr")
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE, verbose_name="Uy xonalar soni", null=True, blank=True)
    area = models.PositiveIntegerField(verbose_name="maydoni")
    money = models.PositiveBigIntegerField(verbose_name="Binoning narxi")
    month = models.PositiveIntegerField(verbose_name="Qancha oyga olmoqchi")
    advance_payment = models.PositiveBigIntegerField(null=True, blank=True, default=0, verbose_name="Oldindan qancha to'lov")
    monthTomoney = models.CharField(max_length=25, editable=False, verbose_name="Oyiga")  # Faqat o'qish uchun
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.month > 0:
            self.monthTomoney = "{:.2f}".format((self.money - self.advance_payment) / self.month)
        else:
            self.monthTomoney = "Invalid input"
        super().save(*args, **kwargs)
    

    class Meta:
        verbose_name = 'Shartnoma'
        verbose_name_plural = 'Shartnomalar'  


    def __str__(self) -> str:
        return f"{self.full_name}"



class SmsMessage(models.Model):
    name = 'sms xabarlar'
    all_costumer = models.CharField(max_length=70)
    all_contract = models.CharField(max_length=70)


    class Meta:
        verbose_name = 'SMS xabar'
        verbose_name_plural = 'SMS xabarlar'

    def __str__(self) -> str:
        return self.name

