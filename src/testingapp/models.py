from django.db import models


class Country(models.Model):
    class Meta:
        db_table = 'country'
    name = models.CharField(max_length=120)
    capital = models.CharField(max_length=120)
    currency = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name
