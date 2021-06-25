
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
        if self.name == 0:
            if self.sex == 0:
                return '%s' % ("YILDIZ ERKEK")
            elif self.sex == 1:
                return '%s' % ("YILDIZ BAYAN")
        if self.name == 1:
            if self.sex == 0:
                return '%s' % ("GENÇ ERKEK")
            elif self.sex == 1:
                return '%s' % ("GENÇ BAYAN")
        if self.name == 2:
            if self.sex == 0:
                return '%s' % ("BÜYÜK ERKEK")
            elif self.sex == 1:
                return '%s' % ("BÜYÜK BAYAN")
        if self.name == 3:
            if self.sex == 0:
                return '%s' % ("AU23 ERKEK")
            elif self.sex == 1:
                return '%s' % ("AU23 BAYAN")
        if self.name == 4:
            if self.sex == 0:
                return '%s' % ("U15 ERKEK")
            elif self.sex == 1:
                return '%s' % ("U15 BAYAN")

        return '%s' % (self.name)

    class Meta:
        managed = False
        db_table = 'agecategory'
