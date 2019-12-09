from django.db import models


# Create your models here.
class Commission(models.Model):
    """
    Active commission info available on site.

    Commissions are indexed by title, and have a description and commissioner
    info.
    """

    commission_title = models.CharField(max_length=50)
    commissioner_name = models.CharField(max_length=50)
    commissioner_platform = models.CharField(max_length=50)
    commission_description = models.CharField(max_length=1000)
    complexity_rating = models.IntegerField(default=0)
    creation_date = models.DateTimeField()

    def __str__(self):
        return self.commission_title


class ArchivedCommission(models.Model):
    """A commission that has been completed."""

    commission_title = models.CharField(max_length=50)
    commissioner_name = models.CharField(max_length=50)
    commissioner_platform = models.CharField(max_length=50)
    commission_description = models.CharField(max_length=1000)
    creation_date = models.DateTimeField()
    completion_date = models.DateTimeField()

    def __str__(self):
        return self.commission_title
