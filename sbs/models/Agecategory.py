
from django.db import models
class Agecategory(models.Model):
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    finishyear = models.IntegerField(db_column='finishYear')  # Field name made lowercase.
    kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
    name = models.IntegerField(blank=True, null=True)
    operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(blank=True, null=True)
    startyear = models.IntegerField(db_column='startYear')  # Field name made lowercase.


    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        managed = False
        db_table = 'agecategory'
