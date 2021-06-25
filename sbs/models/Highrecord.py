from django.contrib.auth.models import User
from django.db import models
from sbs.models.Agecategory import Agecategory
from sbs.models.Competition import  Competition

class Highrecord(models.Model):
    TURKEY = 0
    WORLD = 1
    OLYMPIAD = 2
    EUROPE = 3

    COMPGENERALTYPE = (
        (TURKEY, 'Türkiye'),
        (WORLD, 'Dünya'),
        (OLYMPIAD, 'Olimpiyat'),
        (EUROPE, 'Avrupa')
    )

    INTERUNIVERSITY = 0
    INTERSCHOOL = 1
    PERSONAL = 2
    GRANDPRİX = 3


    COMPTYPE = (
        (INTERUNIVERSITY, 'Üniversiteler Arası'),
        (INTERSCHOOL, 'Okullar Arası'),
        (PERSONAL, 'Ferdi'),
        (GRANDPRİX, 'Grand Prix')
    )

    birthdate = models.DateTimeField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=255, blank=True, null=True)
    creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
    eventdate = models.CharField(db_column='eventDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eventplace = models.CharField(db_column='eventPlace', max_length=255, blank=True, null=True)  # Field name made lowercase.
    kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
    record = models.IntegerField()
    recordtype = models.IntegerField(db_column='recordType', blank=True, null=True,choices=COMPGENERALTYPE)  # Field name made lowercase.
    recordwhich = models.IntegerField(db_column='recordWhich', blank=True, null=True)  # Field name made lowercase.
    agecategory = models.ForeignKey(Agecategory, models.DO_NOTHING, db_column='ageCategory', blank=True, null=True)  # Field name made lowercase.
    competition = models.ForeignKey(Competition, models.DO_NOTHING, db_column='competition', blank=True, null=True)
    weight = models.ForeignKey('Weight', models.DO_NOTHING, db_column='weight', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'highrecord'