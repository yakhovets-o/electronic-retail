from django.db import models


class SupplierLevel(models.IntegerChoices):
    """Supplier hierarchy levels"""

    FACTORY = 0, "Завод"
    DISTRIBUTOR = 1, "Дистрибьютор"
    DEALERSHIP_CENTER = 2, "Дилерский центр"
    LARGE_RETAIL_CHAIN = 3, "Крупная розничная сеть"
    INDIVIDUAL_ENTREPRENEUR = 4, "Индивидуальный предприниматель"
