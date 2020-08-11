from django.db import models

from sbs.models.GrupForReport import GrupForReport
from sbs.models.Competition import Competition
from sbs.models.Athlete import Athlete
from sbs.models.Weight import Weight


class Compathleteforsearch(models.Model):
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
    operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.

    competition = models.ForeignKey(Competition, models.SET_NULL, db_column='competition', blank=True, null=True)
    total = models.IntegerField(default=0)
    lotno = models.IntegerField(db_column='lotNo', default=0)  # Field name made lowercase.
    athlete = models.ForeignKey(Athlete, models.SET_NULL, db_column='athlete', blank=True, null=True)
    sıklet = models.ForeignKey(Weight, models.DO_NOTHING, db_column='sıklet', blank=True, null=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        db_table = 'compathleteforsearch'
        managed = False
