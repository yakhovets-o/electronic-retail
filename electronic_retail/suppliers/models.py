from django.db import models

class Address(models.Model):
    """Модель для хранения адресов.

    Атрибуты:
        country: страна
        city: город
        street: улица
        house_number: номер дома
    """

    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=50, verbose_name="Номер дома")

    def __str__(self):
        return (
            f"{self.country}, {self.city} "
            f"{self.street}, {self.house_number}"
        )