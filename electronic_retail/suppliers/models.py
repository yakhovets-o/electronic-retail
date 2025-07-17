from django.db import models


class Address(models.Model):
    """Stores physical addresses for suppliers"""

    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=255, verbose_name="Улица")
    house_number = models.CharField(max_length=50, verbose_name="Номер дома")

    def __str__(self):
        return (
            f"{self.country}, {self.city} "
            f"{self.street}, {self.house_number}"
        )
