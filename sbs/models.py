# from django.contrib.auth.models import User
# from django.db import models
#
#
# class AccountsForgot(models.Model):
#     uuid = models.CharField(max_length=32)
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     status = models.IntegerField()
#     user = models.ForeignKey('AuthUser', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'accounts_forgot'
#
#
# class Agecategory(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     finishyear = models.IntegerField(db_column='finishYear')  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     name = models.IntegerField(blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     sex = models.IntegerField(blank=True, null=True)
#     startyear = models.IntegerField(db_column='startYear')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'agecategory'
#
#
# class Agecategoryweight(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     agecategory = models.ForeignKey(Agecategory, models.DO_NOTHING, db_column='ageCategory', blank=True, null=True)  # Field name made lowercase.
#     weight = models.ForeignKey('Weight', models.DO_NOTHING, db_column='weight', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'agecategoryweight'
#
#
# class Archivedocument(models.Model):
#     categorypath = models.CharField(db_column='categoryPath', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     archivefolder = models.ForeignKey('Category', models.DO_NOTHING, db_column='archiveFolder', blank=True, null=True)  # Field name made lowercase.
#     location = models.ForeignKey('Category', models.DO_NOTHING, db_column='location', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'archivedocument'
#
#
# class Archivefield(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     field = models.IntegerField(blank=True, null=True)
#     isstatic = models.TextField(db_column='isStatic')  # Field name made lowercase. This field type is a guess.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     title = models.CharField(max_length=255, blank=True, null=True)
#     archivefolder = models.ForeignKey('Category', models.DO_NOTHING, db_column='archiveFolder', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'archivefield'
#
#
# class Archivefielddocument(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     fieldvalue = models.TextField(db_column='fieldValue', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     archivedocument = models.ForeignKey(Archivedocument, models.DO_NOTHING, db_column='archiveDocument', blank=True, null=True)  # Field name made lowercase.
#     archivefield = models.ForeignKey(Archivefield, models.DO_NOTHING, db_column='archivefield', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'archivefielddocument'
#
#
# class Athlete(models.Model):
#     birthdate = models.DateTimeField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     name = models.CharField(max_length=255, blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     photo = models.TextField(blank=True, null=True)
#     sex = models.IntegerField(blank=True, null=True)
#     surname = models.CharField(max_length=255, blank=True, null=True)
#     country = models.ForeignKey('Country', models.DO_NOTHING, db_column='country', blank=True, null=True)
#     sportclub = models.ForeignKey('Sportclub', models.DO_NOTHING, db_column='sportClub', blank=True, null=True)  # Field name made lowercase.
#     tck = models.BigIntegerField(blank=True, null=True)
#     person = models.ForeignKey('Person', models.DO_NOTHING, db_column='person', blank=True, null=True)
#     user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='user', blank=True, null=True)
#     communication = models.ForeignKey('Communication', models.DO_NOTHING, db_column='communication', blank=True, null=True)
#     modificationdate = models.DateTimeField(db_column='modificationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'athlete'
#
#
# class AthleteLicenses(models.Model):
#     athlete = models.ForeignKey(Athlete, models.DO_NOTHING)
#     license = models.OneToOneField('License', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'athlete_licenses'
#
#
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
#
# class AuthtokenToken(models.Model):
#     key = models.CharField(primary_key=True, max_length=40)
#     created = models.DateTimeField()
#     user = models.OneToOneField(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'authtoken_token'
#
#
# class Bank(models.Model):
#     accountno = models.CharField(db_column='accountNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     branchcode = models.CharField(db_column='branchCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     entityid = models.IntegerField(db_column='entityId')  # Field name made lowercase.
#     iban = models.CharField(max_length=255)
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     name = models.CharField(max_length=255)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     owner = models.CharField(max_length=255)
#     tablename = models.IntegerField(db_column='tableName', blank=True, null=True)  # Field name made lowercase.
#     currency = models.ForeignKey('Categoryitem', models.DO_NOTHING, db_column='currency', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bank'
#
#
# class Bodysize(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     entityid = models.IntegerField(db_column='entityId')  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     length = models.FloatField()
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     shoesnumber = models.FloatField(db_column='shoesNumber')  # Field name made lowercase.
#     sportshosenumber = models.FloatField(db_column='sportShoseNumber')  # Field name made lowercase.
#     tablename = models.IntegerField(db_column='tableName', blank=True, null=True)  # Field name made lowercase.
#     weight = models.FloatField()
#     dresssize = models.ForeignKey('Categoryitem', models.DO_NOTHING, db_column='dressSize', blank=True, null=True)  # Field name made lowercase.
#     pantsize = models.ForeignKey('Categoryitem', models.DO_NOTHING, db_column='pantSize', blank=True, null=True)  # Field name made lowercase.
#     topsize = models.ForeignKey('Categoryitem', models.DO_NOTHING, db_column='topSize', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'bodysize'
#
#
# class Category(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     degree = models.IntegerField()
#     description = models.CharField(max_length=255, blank=True, null=True)
#     forwhichclazz = models.CharField(db_column='forWhichClazz', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     isbase = models.TextField(db_column='isBase')  # Field name made lowercase. This field type is a guess.
#     islastcategory = models.TextField(db_column='isLastCategory')  # Field name made lowercase. This field type is a guess.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     title = models.CharField(max_length=255)
#     parentcategory = models.ForeignKey('self', models.DO_NOTHING, db_column='parentCategory', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'category'
#
#
# class CategoryCategory(models.Model):
#     category_id = models.IntegerField()
#     subcategories_id = models.IntegerField(db_column='subCategories_id')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'category_category'
#
#
# class CategoryCategoryitem(models.Model):
#     category_id = models.IntegerField()
#     items_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'category_categoryitem'
#
#
# class Categoryitem(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=255)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
#     forwhichclazz = models.CharField(db_column='forWhichClazz', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     branch = models.CharField(max_length=128, blank=True, null=True)
#     isfirst = models.IntegerField(db_column='isFirst', blank=True, null=True)  # Field name made lowercase.
#     parent_id = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'categoryitem'
#
#
# class Check(models.Model):
#     balance = models.FloatField()
#     ciro = models.TextField()  # This field type is a guess.
#     correspondentbranch = models.CharField(db_column='correspondentBranch', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     currency = models.CharField(max_length=255)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     drawinglocation = models.CharField(db_column='drawingLocation', max_length=255)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     serino = models.BigIntegerField(db_column='seriNo')  # Field name made lowercase.
#     status = models.CharField(max_length=255, blank=True, null=True)
#     termdate = models.DateTimeField(db_column='termDate')  # Field name made lowercase.
#     type = models.CharField(max_length=255, blank=True, null=True)
#     bank = models.IntegerField(blank=True, null=True)
#     debtor = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'check'
#
#
# class City(models.Model):
#     countryid = models.ForeignKey('Country', models.DO_NOTHING, db_column='countryId')  # Field name made lowercase.
#     name = models.CharField(max_length=100)
#     plateno = models.CharField(db_column='plateNo', max_length=2)  # Field name made lowercase.
#     phonecode = models.CharField(db_column='phoneCode', max_length=7)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'city'
#
#
# class CityCounty(models.Model):
#     city_id = models.IntegerField()
#     counties_id = models.IntegerField(unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'city_county'
#
#
# class Communication(models.Model):
#     address = models.CharField(max_length=255, blank=True, null=True)
#     city = models.IntegerField(blank=True, null=True)
#     county = models.CharField(max_length=255, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(max_length=255, blank=True, null=True)
#     entityid = models.IntegerField(db_column='entityId', blank=True, null=True)  # Field name made lowercase.
#     fax = models.CharField(max_length=255, blank=True, null=True)
#     isactive = models.TextField(db_column='isActive', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     mobile = models.CharField(max_length=255, blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     postalcode = models.CharField(db_column='postalCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tablename = models.IntegerField(db_column='tableName', blank=True, null=True)  # Field name made lowercase.
#     tel1 = models.CharField(max_length=255, blank=True, null=True)
#     tel2 = models.CharField(max_length=255, blank=True, null=True)
#     website = models.CharField(db_column='webSite', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     internalno = models.CharField(db_column='internalNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     phonenumber = models.CharField(db_column='phoneNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     phonenumber2 = models.CharField(db_column='phoneNumber2', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     country = models.ForeignKey('Country', models.DO_NOTHING, db_column='country', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'communication'
#
#
# class Compathlete(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     degree = models.IntegerField()
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     kop1 = models.IntegerField()
#     kop1b = models.IntegerField()
#     kop2 = models.IntegerField()
#     kop2b = models.IntegerField()
#     kop3 = models.IntegerField()
#     kop3b = models.IntegerField()
#     kopdegree = models.IntegerField(db_column='kopDegree')  # Field name made lowercase.
#     kopkaldirissira = models.IntegerField(db_column='kopKaldirisSira')  # Field name made lowercase.
#     kopsilktotal = models.IntegerField(db_column='kopSilkTotal')  # Field name made lowercase.
#     koptotal = models.IntegerField(db_column='kopTotal')  # Field name made lowercase.
#     lotno = models.IntegerField(db_column='lotNo')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     sessionno = models.IntegerField(db_column='sessionNo')  # Field name made lowercase.
#     silk1 = models.IntegerField()
#     silk1b = models.IntegerField()
#     silk2 = models.IntegerField()
#     silk2b = models.IntegerField()
#     silk3 = models.IntegerField()
#     silk3b = models.IntegerField()
#     silkdegree = models.IntegerField(db_column='silkDegree')  # Field name made lowercase.
#     silktotal = models.IntegerField(db_column='silkTotal')  # Field name made lowercase.
#     total = models.IntegerField()
#     weight = models.FloatField()
#     athlete = models.ForeignKey(Athlete, models.DO_NOTHING, db_column='athlete', blank=True, null=True)
#     compcategory = models.ForeignKey('Compcategory', models.DO_NOTHING, db_column='compCategory', blank=True, null=True)  # Field name made lowercase.
#     sıklet = models.ForeignKey('Weight', models.DO_NOTHING, db_column='sıklet', blank=True, null=True)
#     lastliftvalue = models.IntegerField(db_column='lastLiftValue', blank=True, null=True)  # Field name made lowercase.
#     lastsilkliftvalue = models.IntegerField(db_column='lastSilkLiftValue', blank=True, null=True)  # Field name made lowercase.
#     competition = models.ForeignKey('Competition', models.DO_NOTHING, db_column='competition', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'compathlete'
#
#
# class Compcatage(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     agecategory = models.ForeignKey(Agecategory, models.DO_NOTHING, db_column='ageCategory', blank=True, null=True)  # Field name made lowercase.
#     compcategory = models.ForeignKey('Compcategory', models.DO_NOTHING, db_column='compCategory', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'compcatage'
#
#
# class Compcategory(models.Model):
#     athletegroup = models.CharField(db_column='athleteGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     sex = models.IntegerField(blank=True, null=True)
#     competition = models.ForeignKey('Competition', models.DO_NOTHING, db_column='competition', blank=True, null=True)
#     startdate = models.CharField(db_column='startDate', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=45, blank=True, null=True)
#     starttime = models.CharField(db_column='startTime', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     grupforreport = models.ForeignKey('Grupforreport', models.DO_NOTHING, db_column='grupForReport', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'compcategory'
#
#
# class Compcatweight(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     compcategory = models.ForeignKey(Compcategory, models.DO_NOTHING, db_column='compCategory', blank=True, null=True)  # Field name made lowercase.
#     weight = models.ForeignKey('Weight', models.DO_NOTHING, db_column='weight', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'compcatweight'
#
#
# class Competition(models.Model):
#     comptype = models.IntegerField(db_column='compType', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     finishdate = models.DateTimeField(db_column='finishDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     name = models.CharField(max_length=255, blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
#     eventplace = models.CharField(db_column='eventPlace', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     eventdate = models.CharField(db_column='eventDate', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     jurycount = models.IntegerField(db_column='juryCount', blank=True, null=True)  # Field name made lowercase.
#     compgeneraltype = models.IntegerField(db_column='compGeneralType', blank=True, null=True)  # Field name made lowercase.
#     eskimi = models.IntegerField()
#     isopen = models.IntegerField(db_column='isOpen')  # Field name made lowercase.
#     registerstartdate = models.DateTimeField(db_column='registerStartDate', blank=True, null=True)  # Field name made lowercase.
#     registerfinishdate = models.DateTimeField(db_column='registerFinishDate', blank=True, null=True)  # Field name made lowercase.
#     year = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'competition'
#
#
# class Compsession(models.Model):
#     agegroup = models.CharField(db_column='ageGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     sessiondate = models.DateTimeField(db_column='sessionDate', blank=True, null=True)  # Field name made lowercase.
#     sessiontime = models.CharField(db_column='sessionTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sex = models.IntegerField(blank=True, null=True)
#     competition = models.ForeignKey(Competition, models.DO_NOTHING, db_column='competition', blank=True, null=True)
#     weight = models.ForeignKey('Weight', models.DO_NOTHING, db_column='weight', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'compsession'
#
#
# class Country(models.Model):
#     binarycode = models.CharField(db_column='binaryCode', max_length=2)  # Field name made lowercase.
#     triplecode = models.CharField(db_column='tripleCode', max_length=3)  # Field name made lowercase.
#     name = models.CharField(max_length=100)
#     phonecode = models.CharField(db_column='phoneCode', max_length=6)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     photo = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'country'
#
#
# class CountryCity(models.Model):
#     country_id = models.IntegerField()
#     cities_id = models.IntegerField(unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'country_city'
#
#
# class County(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     name = models.CharField(max_length=255, blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'county'
#
#
# class Currencyvalue(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     currency = models.CharField(max_length=255, blank=True, null=True)
#     isdefault = models.TextField(db_column='isDefault')  # Field name made lowercase. This field type is a guess.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     value = models.FloatField()
#
#     class Meta:
#         managed = False
#         db_table = 'currencyvalue'
#
#
# class DefIlceler(models.Model):
#     rgno = models.AutoField(db_column='RGNO', primary_key=True)  # Field name made lowercase.
#     rgbno = models.SmallIntegerField(db_column='RGBNO', blank=True, null=True)  # Field name made lowercase.
#     ilkodu = models.SmallIntegerField(db_column='ILKODU', blank=True, null=True)  # Field name made lowercase.
#     ilad = models.CharField(db_column='ILAD', max_length=30, blank=True, null=True)  # Field name made lowercase.
#     ilcekodu = models.SmallIntegerField(db_column='ILCEKODU', blank=True, null=True)  # Field name made lowercase.
#     ilcead = models.CharField(db_column='ILCEAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
#     har_enlem = models.FloatField(db_column='HAR_ENLEM', blank=True, null=True)  # Field name made lowercase.
#     har_boylam = models.FloatField(db_column='HAR_BOYLAM', blank=True, null=True)  # Field name made lowercase.
#     har_kde = models.FloatField(db_column='HAR_KDE', blank=True, null=True)  # Field name made lowercase.
#     har_kdb = models.FloatField(db_column='HAR_KDB', blank=True, null=True)  # Field name made lowercase.
#     har_gbe = models.FloatField(db_column='HAR_GBE', blank=True, null=True)  # Field name made lowercase.
#     har_gbb = models.FloatField(db_column='HAR_GBB', blank=True, null=True)  # Field name made lowercase.
#     nufus = models.BigIntegerField(db_column='NUFUS', blank=True, null=True)  # Field name made lowercase.
#     ilcesira = models.SmallIntegerField(db_column='ILCESIRA', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'def_ilceler'
#
#
# class DefIller(models.Model):
#     rgno = models.IntegerField(db_column='RGNO')  # Field name made lowercase.
#     rgbno = models.FloatField(db_column='RGBNO', blank=True, null=True)  # Field name made lowercase.
#     il_kodu = models.SmallIntegerField(db_column='IL_KODU', blank=True, null=True)  # Field name made lowercase.
#     il_adi = models.CharField(db_column='IL_ADI', max_length=16, blank=True, null=True)  # Field name made lowercase.
#     har_enlem = models.FloatField(db_column='HAR_ENLEM', blank=True, null=True)  # Field name made lowercase.
#     har_boylam = models.FloatField(db_column='HAR_BOYLAM', blank=True, null=True)  # Field name made lowercase.
#     har_kde = models.FloatField(db_column='HAR_KDE', blank=True, null=True)  # Field name made lowercase.
#     har_kdb = models.FloatField(db_column='HAR_KDB', blank=True, null=True)  # Field name made lowercase.
#     har_gbe = models.FloatField(db_column='HAR_GBE', blank=True, null=True)  # Field name made lowercase.
#     har_gbb = models.FloatField(db_column='HAR_GBB', blank=True, null=True)  # Field name made lowercase.
#     nufus = models.BigIntegerField(db_column='NUFUS', blank=True, null=True)  # Field name made lowercase.
#     nufus_yogunlugu_km2 = models.BigIntegerField(db_column='NUFUS_YOGUNLUGU_KM2', blank=True, null=True)  # Field name made lowercase.
#     telefon_kodu = models.BigIntegerField(db_column='TELEFON_KODU', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'def_iller'
#
#
# class Denemetable(models.Model):
#     id = models.IntegerField(primary_key=True)
#     dosya = models.CharField(max_length=1000, db_collation='utf8_general_ci', blank=True, null=True)
#     resim = models.TextField(blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'denemetable'
#
#
# class Department(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     departmentstring = models.CharField(db_column='departmentString', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     department = models.OneToOneField(Category, models.DO_NOTHING, db_column='department', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'department'
#
#
# class District(models.Model):
#     townid = models.ForeignKey('Town', models.DO_NOTHING, db_column='townId')  # Field name made lowercase.
#     name = models.CharField(max_length=100)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'district'
#
#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
#
# class Documentarchive(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     document = models.TextField(blank=True, null=True)
#     entityid = models.IntegerField(db_column='entityId')  # Field name made lowercase.
#     extension = models.CharField(max_length=255, blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     name = models.CharField(max_length=255, blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     tablename = models.IntegerField(db_column='tableName', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'documentarchive'
#
#
# class Education(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     entityid = models.IntegerField(db_column='entityId')  # Field name made lowercase.
#     finishdate = models.DateTimeField(db_column='finishDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     schoolname = models.CharField(db_column='schoolName', max_length=255)  # Field name made lowercase.
#     startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
#     tablename = models.IntegerField(db_column='tableName', blank=True, null=True)  # Field name made lowercase.
#     type = models.ForeignKey(Categoryitem, models.DO_NOTHING, db_column='type', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'education'
#
#
# class Emailinfo(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(max_length=255)
#     entityid = models.IntegerField(db_column='entityId')  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     mailserver = models.CharField(db_column='mailServer', max_length=255)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     password = models.CharField(max_length=255)
#     port = models.IntegerField()
#     tablename = models.IntegerField(db_column='tableName', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'emailinfo'
#
#
# class Employee(models.Model):
#     address = models.CharField(max_length=255, blank=True, null=True)
#     birthdate = models.DateTimeField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     deaddate = models.DateTimeField(db_column='deadDate', blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(max_length=255, blank=True, null=True)
#     image = models.TextField(blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     mobilephone = models.CharField(db_column='mobilePhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=255)
#     nationalityid = models.BigIntegerField(db_column='nationalityId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     phone1 = models.CharField(max_length=255, blank=True, null=True)
#     phone2 = models.CharField(max_length=255, blank=True, null=True)
#     postalcode = models.CharField(db_column='postalCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     sex = models.CharField(max_length=255, blank=True, null=True)
#     surname = models.CharField(max_length=255)
#     basesalary = models.FloatField(db_column='baseSalary', blank=True, null=True)  # Field name made lowercase.
#     code = models.BigIntegerField()
#     dateofhire = models.DateTimeField(db_column='dateOfHire', blank=True, null=True)  # Field name made lowercase.
#     dateofleave = models.DateTimeField(db_column='dateOfLeave', blank=True, null=True)  # Field name made lowercase.
#     fulltime = models.TextField(db_column='fullTime')  # Field name made lowercase. This field type is a guess.
#     nationality = models.IntegerField(blank=True, null=True)
#     bank = models.IntegerField(blank=True, null=True)
#     department = models.IntegerField(blank=True, null=True)
#     jobinfo = models.IntegerField(db_column='jobInfo', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'employee'
#
#
# class EmployeePaymentdetails(models.Model):
#     employee_id = models.IntegerField()
#     payments_id = models.IntegerField(unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'employee_paymentdetails'
#
#
# class Employeeinouttime(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     which = models.CharField(max_length=255, blank=True, null=True)
#     employee = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'employeeinouttime'
#
#
# class FusioMigrationVersions(models.Model):
#     version = models.CharField(primary_key=True, max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'fusio_migration_versions'
#
#
# class Grupforreport(models.Model):
#     centerreferee = models.CharField(db_column='centerReferee', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     compdoctor = models.CharField(db_column='compDoctor', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     jurymemberfour = models.CharField(db_column='juryMemberFour', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     jurymemberone = models.CharField(db_column='juryMemberOne', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     jurymemberthree = models.CharField(db_column='juryMemberThree', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     jurymembertwo = models.CharField(db_column='juryMemberTwo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     jurypresident = models.CharField(db_column='juryPresident', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     marshallone = models.CharField(db_column='marshallOne', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     marshalltwo = models.CharField(db_column='marshallTwo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=255, blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     refereeone = models.CharField(db_column='refereeOne', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     refereetwo = models.CharField(db_column='refereeTwo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     speaker = models.CharField(max_length=255, blank=True, null=True)
#     techcontrollerone = models.CharField(db_column='techControllerOne', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     techcontrollertwo = models.CharField(db_column='techControllerTwo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     timekeeper = models.CharField(db_column='timeKeeper', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     competition = models.ForeignKey(Competition, models.DO_NOTHING, db_column='competition', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'grupforreport'
#
#
# class Highrecord(models.Model):
#     birthdate = models.DateTimeField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
#     country = models.CharField(max_length=255, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     eventdate = models.CharField(db_column='eventDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     eventplace = models.CharField(db_column='eventPlace', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     name = models.CharField(max_length=255, blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     record = models.IntegerField()
#     recordtype = models.IntegerField(db_column='recordType', blank=True, null=True)  # Field name made lowercase.
#     recordwhich = models.IntegerField(db_column='recordWhich', blank=True, null=True)  # Field name made lowercase.
#     agecategory = models.ForeignKey(Agecategory, models.DO_NOTHING, db_column='ageCategory', blank=True, null=True)  # Field name made lowercase.
#     competition = models.ForeignKey(Competition, models.DO_NOTHING, db_column='competition', blank=True, null=True)
#     weight = models.ForeignKey('Weight', models.DO_NOTHING, db_column='weight', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'highrecord'
#
#
# class Hltantrenor(models.Model):
#     aciklama = models.CharField(max_length=255, blank=True, null=True)
#     ad = models.CharField(max_length=255, blank=True, null=True)
#     adsoyad = models.CharField(db_column='adSoyad', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     anneadi = models.CharField(db_column='anneAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ayakkabino = models.CharField(db_column='ayakkabiNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     babaadi = models.CharField(db_column='babaAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankaadi = models.CharField(db_column='bankaAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankahesapno = models.CharField(db_column='bankaHesapNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankahesapssahibi = models.CharField(db_column='bankaHesapSsahibi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankaiban = models.CharField(db_column='bankaIban', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankasubeno = models.CharField(db_column='bankaSubeNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     boy = models.FloatField(blank=True, null=True)
#     ceptel = models.CharField(db_column='cepTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cinsiyet = models.CharField(max_length=255, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     dogumtarihi = models.DateTimeField(db_column='dogumTarihi', blank=True, null=True)  # Field name made lowercase.
#     dogumyeri = models.CharField(db_column='dogumYeri', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(max_length=255, blank=True, null=True)
#     emeklisicilno = models.CharField(db_column='emekliSicilNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esofmanbedenno = models.CharField(db_column='esofmanBedenNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     evtel = models.CharField(db_column='evTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hastalikaciklama = models.CharField(db_column='hastalikAciklama', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hastaliklimi = models.TextField(blank=True, null=True)  # This field type is a guess.
#     ikametadres = models.CharField(db_column='ikametAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ikametili = models.CharField(db_column='ikametIli', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     isadres = models.CharField(db_column='isAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     istel = models.CharField(db_column='isTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     izinalinacakadres = models.CharField(db_column='izinAlinacakAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kademe = models.CharField(max_length=255, blank=True, null=True)
#     kadroderecesi = models.CharField(db_column='kadroDerecesi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kangrubu = models.CharField(db_column='kanGrubu', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kilo = models.FloatField(blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     medenihali = models.CharField(db_column='medeniHali', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     meslek = models.CharField(max_length=255, blank=True, null=True)
#     nufusailesirano = models.IntegerField(db_column='nufusAileSiraNo', blank=True, null=True)  # Field name made lowercase.
#     nufusciltno = models.IntegerField(db_column='nufusCiltNo', blank=True, null=True)  # Field name made lowercase.
#     nufusil = models.CharField(db_column='nufusIl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusilce = models.CharField(db_column='nufusIlce', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusmahallekoy = models.CharField(db_column='nufusMahalleKoy', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusserino = models.CharField(db_column='nufusSeriNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufussirano = models.IntegerField(db_column='nufusSiraNo', blank=True, null=True)  # Field name made lowercase.
#     ogrenimdurumu = models.CharField(db_column='ogrenimDurumu', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     pasaportno = models.BigIntegerField(db_column='pasaportNo', blank=True, null=True)  # Field name made lowercase.
#     pasaporttarihi = models.DateTimeField(db_column='pasaportTarihi', blank=True, null=True)  # Field name made lowercase.
#     resim = models.TextField(blank=True, null=True)
#     soyad = models.CharField(max_length=255, blank=True, null=True)
#     statu = models.CharField(max_length=255, blank=True, null=True)
#     tcno = models.BigIntegerField(db_column='tcNo', blank=True, null=True)  # Field name made lowercase.
#     tisortno = models.CharField(db_column='tisortNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     uyruk = models.CharField(max_length=255, blank=True, null=True)
#     yabancidil = models.CharField(db_column='yabanciDil', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kulup = models.IntegerField(blank=True, null=True)
#     cezabaslangictarihi = models.IntegerField(db_column='cezaBaslangicTarihi', blank=True, null=True)  # Field name made lowercase.
#     cezasuresi = models.IntegerField(db_column='cezaSuresi', blank=True, null=True)  # Field name made lowercase.
#     cezabitistarihi = models.IntegerField(db_column='cezaBitisTarihi', blank=True, null=True)  # Field name made lowercase.
#     cezanedeni = models.CharField(db_column='cezaNedeni', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     toplamcezasayisi = models.IntegerField(db_column='toplamCezaSayisi', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltantrenor'
#
#
# class Hltarsivyeni(models.Model):
#     id = models.IntegerField(primary_key=True)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     dosya = models.CharField(max_length=255, blank=True, null=True)
#     klasor = models.CharField(max_length=255, blank=True, null=True)
#     raf = models.CharField(max_length=255, blank=True, null=True)
#     dolap = models.CharField(max_length=255, blank=True, null=True)
#     sene = models.IntegerField(blank=True, null=True)
#     number_6 = models.CharField(db_column='6', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7 = models.CharField(db_column='7', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_8 = models.CharField(db_column='8', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_9 = models.CharField(db_column='9', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_10 = models.CharField(db_column='10', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_11 = models.CharField(db_column='11', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_12 = models.CharField(db_column='12', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     blb_rgno = models.IntegerField(blank=True, null=True)
#     blb_tablosu = models.CharField(max_length=255, blank=True, null=True)
#     eski_blb_rgno = models.IntegerField(blank=True, null=True)
#     hatalar = models.CharField(max_length=255, blank=True, null=True)
#     durum = models.TextField(blank=True, null=True)  # This field type is a guess.
#     gelen_tarih = models.DateTimeField(blank=True, null=True)
#     gelen_sayi = models.CharField(max_length=255, blank=True, null=True)
#     gelen_kurum = models.CharField(max_length=255, blank=True, null=True)
#     metin = models.TextField(blank=True, null=True)
#     ocr = models.TextField(blank=True, null=True)
#     tur = models.CharField(max_length=255, blank=True, null=True)
#     olusturan = models.CharField(max_length=255, blank=True, null=True)
#     olusturan_zaman = models.DateTimeField(blank=True, null=True)
#     konu = models.CharField(max_length=255, blank=True, null=True)
#     resim = models.TextField(blank=True, null=True)
#     ext = models.CharField(max_length=45, blank=True, null=True)
#     filename = models.CharField(db_column='fileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     dosyayeni = models.IntegerField(db_column='dosyaYeni', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltarsivyeni'
#
#
# class Hlthakem(models.Model):
#     aciklama = models.CharField(max_length=255, blank=True, null=True)
#     ad = models.CharField(max_length=255, blank=True, null=True)
#     adsoyad = models.CharField(db_column='adSoyad', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     anneadi = models.CharField(db_column='anneAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ayakkabino = models.CharField(db_column='ayakkabiNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     babaadi = models.CharField(db_column='babaAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankaadi = models.CharField(db_column='bankaAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankahesapno = models.CharField(db_column='bankaHesapNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankahesapssahibi = models.CharField(db_column='bankaHesapSsahibi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankaiban = models.CharField(db_column='bankaIban', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankasubeno = models.CharField(db_column='bankaSubeNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     boy = models.FloatField(blank=True, null=True)
#     ceptel = models.CharField(db_column='cepTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cinsiyet = models.CharField(max_length=255, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     dogumtarihi = models.DateTimeField(db_column='dogumTarihi', blank=True, null=True)  # Field name made lowercase.
#     dogumyeri = models.CharField(db_column='dogumYeri', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(max_length=255, blank=True, null=True)
#     emeklisicilno = models.CharField(db_column='emekliSicilNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     esofmanbedenno = models.CharField(db_column='esofmanBedenNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     evtel = models.CharField(db_column='evTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hakemolduguyer = models.CharField(db_column='hakemOlduguYer', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hakemolustarihi = models.DateTimeField(db_column='hakemOlusTarihi', blank=True, null=True)  # Field name made lowercase.
#     hakemsicilno = models.CharField(db_column='hakemSicilNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hakemlikkategorisi = models.CharField(db_column='hakemlikKategorisi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hastalikaciklama = models.CharField(db_column='hastalikAciklama', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hastaliklimi = models.TextField(blank=True, null=True)  # This field type is a guess.
#     ikametadres = models.CharField(db_column='ikametAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ikametili = models.CharField(db_column='ikametIli', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     isadres = models.CharField(db_column='isAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     istel = models.CharField(db_column='isTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     izinalinacakadres = models.CharField(db_column='izinAlinacakAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kadroderecesi = models.CharField(db_column='kadroDerecesi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kangrubu = models.CharField(db_column='kanGrubu', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kilo = models.FloatField(blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     medenihali = models.CharField(db_column='medeniHali', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     meslek = models.CharField(max_length=255, blank=True, null=True)
#     nufusailesirano = models.IntegerField(db_column='nufusAileSiraNo', blank=True, null=True)  # Field name made lowercase.
#     nufusciltno = models.IntegerField(db_column='nufusCiltNo', blank=True, null=True)  # Field name made lowercase.
#     nufusil = models.CharField(db_column='nufusIl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusilce = models.CharField(db_column='nufusIlce', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusmahallekoy = models.CharField(db_column='nufusMahalleKoy', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusserino = models.CharField(db_column='nufusSeriNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufussirano = models.IntegerField(db_column='nufusSiraNo', blank=True, null=True)  # Field name made lowercase.
#     ogrenimdurumu = models.CharField(db_column='ogrenimDurumu', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     pasaportno = models.BigIntegerField(db_column='pasaportNo', blank=True, null=True)  # Field name made lowercase.
#     pasaporttarihi = models.DateTimeField(db_column='pasaportTarihi', blank=True, null=True)  # Field name made lowercase.
#     resim = models.TextField(blank=True, null=True)
#     soyad = models.CharField(max_length=255, blank=True, null=True)
#     tcno = models.BigIntegerField(db_column='tcNo', blank=True, null=True)  # Field name made lowercase.
#     tisortno = models.CharField(db_column='tisortNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     uyruk = models.CharField(max_length=255, blank=True, null=True)
#     yabancidil = models.CharField(db_column='yabanciDil', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cezabaslangictarihi = models.IntegerField(db_column='cezaBaslangicTarihi', blank=True, null=True)  # Field name made lowercase.
#     cezasuresi = models.IntegerField(db_column='cezaSuresi', blank=True, null=True)  # Field name made lowercase.
#     cezabitistarihi = models.IntegerField(db_column='cezaBitisTarihi', blank=True, null=True)  # Field name made lowercase.
#     cezanedeni = models.CharField(db_column='cezaNedeni', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     toplamcezasayisi = models.IntegerField(db_column='toplamCezaSayisi', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hlthakem'
#
#
# class Hltiller(models.Model):
#     il_adi = models.CharField(db_column='IL_ADI', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltiller'
#
#
# class Hltkategori(models.Model):
#     kategoriadi = models.CharField(db_column='kategoriAdi', max_length=255, db_collation='utf8_general_ci')  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltkategori'
#
#
# class Hltkulup(models.Model):
#     aciklama = models.CharField(max_length=255, blank=True, null=True)
#     ad = models.CharField(max_length=255, blank=True, null=True)
#     adsoyad = models.CharField(db_column='adSoyad', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     anneadi = models.CharField(db_column='anneAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     babaadi = models.CharField(db_column='babaAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankaadi = models.CharField(db_column='bankaAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankaeft = models.CharField(db_column='bankaEft', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankahesapno = models.CharField(db_column='bankaHesapNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankahesapssahibi = models.CharField(db_column='bankaHesapSsahibi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankaiban = models.CharField(db_column='bankaIban', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankasubeno = models.CharField(db_column='bankaSubeNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     branssorumlusuadsoyad = models.CharField(db_column='bransSorumlusuAdSoyad', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     branssorumlusuceptel = models.CharField(db_column='bransSorumlusuCepTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     branssorumlusuemail = models.CharField(db_column='bransSorumlusuEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     branssorumlusuistel = models.CharField(db_column='bransSorumlusuIsTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ceptel = models.CharField(db_column='cepTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cinsiyet = models.CharField(max_length=255, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     dogumtarihi = models.DateTimeField(db_column='dogumTarihi', blank=True, null=True)  # Field name made lowercase.
#     dogumyeri = models.CharField(db_column='dogumYeri', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(max_length=255, blank=True, null=True)
#     evtel = models.CharField(db_column='evTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ikametadres = models.CharField(db_column='ikametAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ikametili = models.CharField(db_column='ikametIli', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     isadres = models.CharField(db_column='isAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     istel = models.CharField(db_column='isTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kangrubu = models.CharField(db_column='kanGrubu', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     kulupadi = models.CharField(db_column='kulupAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kulupadres = models.CharField(db_column='kulupAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kulupfax = models.CharField(db_column='kulupFax', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kulupil = models.CharField(db_column='kulupIl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kulupkisaad = models.CharField(db_column='kulupKisaAd', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kulupmail = models.CharField(db_column='kulupMail', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kulupmuduradsoyad = models.CharField(db_column='kulupMudurAdSoyad', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kulupmudurceptel = models.CharField(db_column='kulupMudurCepTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kulupmuduremail = models.CharField(db_column='kulupMudurEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kulupmuduristel = models.CharField(db_column='kulupMudurIsTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kuluprenkler = models.CharField(db_column='kulupRenkler', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kuluptel = models.CharField(db_column='kulupTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     medenihali = models.CharField(db_column='medeniHali', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusailesirano = models.IntegerField(db_column='nufusAileSiraNo', blank=True, null=True)  # Field name made lowercase.
#     nufusciltno = models.IntegerField(db_column='nufusCiltNo', blank=True, null=True)  # Field name made lowercase.
#     nufusil = models.CharField(db_column='nufusIl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusilce = models.CharField(db_column='nufusIlce', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusmahallekoy = models.CharField(db_column='nufusMahalleKoy', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusserino = models.CharField(db_column='nufusSeriNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufussirano = models.IntegerField(db_column='nufusSiraNo', blank=True, null=True)  # Field name made lowercase.
#     ogrenimdurumu = models.CharField(db_column='ogrenimDurumu', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     pasaportno = models.BigIntegerField(db_column='pasaportNo', blank=True, null=True)  # Field name made lowercase.
#     pasaporttarihi = models.DateTimeField(db_column='pasaportTarihi', blank=True, null=True)  # Field name made lowercase.
#     resim = models.TextField(blank=True, null=True)
#     soyad = models.CharField(max_length=255, blank=True, null=True)
#     tcno = models.BigIntegerField(db_column='tcNo', blank=True, null=True)  # Field name made lowercase.
#     uyruk = models.CharField(max_length=255, blank=True, null=True)
#     yabancidil = models.CharField(db_column='yabanciDil', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     thf_kadi = models.IntegerField(blank=True, null=True)
#     thf_ksifre = models.CharField(max_length=20, blank=True, null=True)
#     thf_aktif = models.IntegerField(blank=True, null=True)
#     thf_durum = models.CharField(max_length=45, blank=True, null=True)
#     thf_tarayici = models.CharField(max_length=255, blank=True, null=True)
#     thf_ip = models.CharField(max_length=45, blank=True, null=True)
#     thf_zaman = models.DateTimeField(blank=True, null=True)
#     thf_ip_sunucu = models.CharField(max_length=45, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'hltkulup'
#
#
# class Hltkulupmusabaka(models.Model):
#     musabakaid = models.IntegerField(db_column='musabakaId')  # Field name made lowercase.
#     ilksporcuid = models.IntegerField(db_column='ilkSporcuId', blank=True, null=True)  # Field name made lowercase.
#     ilksporcupuan = models.IntegerField(db_column='ilkSporcuPuan', blank=True, null=True)  # Field name made lowercase.
#     ikincisporcuid = models.IntegerField(db_column='ikinciSporcuId', blank=True, null=True)  # Field name made lowercase.
#     ikincisporcupuan = models.IntegerField(db_column='ikinciSporcuPuan', blank=True, null=True)  # Field name made lowercase.
#     siklet = models.CharField(max_length=100, blank=True, null=True)
#     cinsiyet = models.CharField(max_length=100, blank=True, null=True)
#     kulupid = models.IntegerField(db_column='kulupId')  # Field name made lowercase.
#     kulupderece = models.IntegerField(db_column='kulupDerece', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltkulupmusabaka'
#
#
# class Hltkuluptoplampuan(models.Model):
#     musabakaid = models.IntegerField(db_column='musabakaId')  # Field name made lowercase.
#     kulupid = models.IntegerField(db_column='kulupId')  # Field name made lowercase.
#     toplamsporcu = models.IntegerField(db_column='toplamSporcu')  # Field name made lowercase.
#     toplampuan = models.IntegerField(db_column='toplamPuan')  # Field name made lowercase.
#     derece = models.IntegerField(blank=True, null=True)
#     cinsiyet = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'hltkuluptoplampuan'
#
#
# class Hltmakbuz(models.Model):
#     tck = models.BigIntegerField(blank=True, null=True)
#     adi_soyadi = models.CharField(max_length=100, blank=True, null=True)
#     dogum_yeri = models.CharField(max_length=45, blank=True, null=True)
#     ili = models.CharField(max_length=45, blank=True, null=True)
#     iban = models.CharField(max_length=45, blank=True, null=True)
#     cep = models.CharField(max_length=100, blank=True, null=True)
#     kademe = models.CharField(max_length=45, blank=True, null=True)
#     foto = models.CharField(max_length=20, blank=True, null=True)
#     makbuz = models.CharField(max_length=20, blank=True, null=True)
#     sifre = models.CharField(max_length=10, blank=True, null=True)
#     fotoblb = models.TextField(blank=True, null=True)
#     makbuzblb = models.TextField(blank=True, null=True)
#     thf_aktif = models.IntegerField(blank=True, null=True)
#     thf_durum = models.CharField(max_length=45, blank=True, null=True)
#     thf_tarayici = models.CharField(max_length=255, blank=True, null=True)
#     thf_ip = models.CharField(max_length=45, blank=True, null=True)
#     thf_zaman = models.DateTimeField(blank=True, null=True)
#     thf_ip_sunucu = models.CharField(max_length=255, blank=True, null=True)
#     tur = models.CharField(max_length=45, blank=True, null=True)
#     e_posta = models.CharField(max_length=200, blank=True, null=True)
#     banka = models.CharField(max_length=100, blank=True, null=True)
#     dogum_tarihi = models.DateField(blank=True, null=True)
#     notlar = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'hltmakbuz'
#
#
# class Hltmusabaka(models.Model):
#     adi = models.CharField(max_length=255, blank=True, null=True)
#     baslangictarihi = models.DateTimeField(db_column='baslangicTarihi', blank=True, null=True)  # Field name made lowercase.
#     bitistarihi = models.DateTimeField(db_column='bitisTarihi', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kategori = models.ForeignKey(Hltkategori, models.DO_NOTHING, blank=True, null=True)
#     tipi = models.CharField(max_length=255, blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     ili = models.CharField(max_length=255, blank=True, null=True)
#     durum = models.IntegerField(blank=True, null=True)
#     ferdi = models.IntegerField(blank=True, null=True)
#     puanhesaplandi = models.IntegerField(db_column='puanHesaplandi', blank=True, null=True)  # Field name made lowercase.
#     eskimi = models.IntegerField(blank=True, null=True)
#     coklukategori = models.IntegerField(db_column='cokluKategori', blank=True, null=True)  # Field name made lowercase.
#     kategoriadi = models.CharField(db_column='kategoriAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tipi2 = models.CharField(max_length=255, blank=True, null=True)
#     okul = models.IntegerField(blank=True, null=True)
#     kulup = models.IntegerField(blank=True, null=True)
#     canli = models.IntegerField(blank=True, null=True)
#     canli_www = models.CharField(max_length=255, blank=True, null=True)
#     yayinla = models.IntegerField(blank=True, null=True)
#     basarim = models.IntegerField(blank=True, null=True)
#     aciklama = models.TextField(blank=True, null=True)
#     sene = models.IntegerField(blank=True, null=True)
#     yeri = models.CharField(max_length=150, blank=True, null=True)
#     onlinebaslangictarihi = models.DateField(db_column='onlineBaslangicTarihi', blank=True, null=True)  # Field name made lowercase.
#     onlinebitistarihi = models.DateField(db_column='onlineBitisTarihi', blank=True, null=True)  # Field name made lowercase.
#     seremoni = models.CharField(max_length=150, blank=True, null=True)
#     guncel = models.IntegerField(blank=True, null=True)
#     tekniktoplanti = models.CharField(db_column='teknikToplanti', max_length=150, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltmusabaka'
#
#
# class Hltmusabakabasvuru(models.Model):
#     adi = models.CharField(max_length=100, blank=True, null=True)
#     cinsiyet = models.CharField(max_length=25, blank=True, null=True)
#     il = models.CharField(max_length=45, blank=True, null=True)
#     siklet = models.CharField(max_length=10, blank=True, null=True)
#     toplam = models.CharField(max_length=10, blank=True, null=True)
#     zaman = models.DateTimeField(blank=True, null=True)
#     musabaka_id = models.IntegerField(blank=True, null=True)
#     dogum_tarihi = models.CharField(max_length=15, blank=True, null=True)
#     olusturan = models.CharField(max_length=255, blank=True, null=True)
#     olusturan_id = models.IntegerField(blank=True, null=True)
#     kulup = models.CharField(max_length=255, blank=True, null=True)
#     guncel_zaman = models.DateTimeField(blank=True, null=True)
#     tck = models.BigIntegerField(blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltmusabakabasvuru'
#
#
# class Hltmusabakabasvuruantrenor(models.Model):
#     adi = models.CharField(max_length=200, blank=True, null=True)
#     musabaka = models.ForeignKey(Hltmusabaka, models.DO_NOTHING, blank=True, null=True)
#     zaman = models.DateTimeField(blank=True, null=True)
#     olusturan = models.CharField(max_length=200, blank=True, null=True)
#     olusturan_id = models.IntegerField(blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltmusabakabasvuruantrenor'
#
#
# class Hltmusabakaolay(models.Model):
#     musabakaid = models.ForeignKey(Hltmusabaka, models.DO_NOTHING, db_column='musabakaId')  # Field name made lowercase.
#     gun = models.DateField()
#     saat = models.TimeField()
#     ring = models.CharField(max_length=100)
#     cinsiyet = models.CharField(max_length=100)
#     hakemgrubu = models.CharField(db_column='hakemGrubu', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     jurigrubu = models.CharField(db_column='juriGrubu', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     siklet = models.CharField(max_length=100, blank=True, null=True)
#     sporcusayisi = models.IntegerField(db_column='sporcuSayisi', blank=True, null=True)  # Field name made lowercase.
#     sporcugrubu = models.CharField(db_column='sporcuGrubu', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     bittimi = models.IntegerField(blank=True, null=True)
#     derecetamam = models.IntegerField(db_column='dereceTamam', blank=True, null=True)  # Field name made lowercase.
#     kategori = models.ForeignKey(Hltkategori, models.DO_NOTHING, blank=True, null=True)
#     kategoriadi_siklet = models.CharField(db_column='kategoriAdi_siklet', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     kategoriadi = models.CharField(db_column='kategoriAdi', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltmusabakaolay'
#
#
# class Hltmusabakayonetimi(models.Model):
#     musabaka = models.ForeignKey(Hltmusabaka, models.DO_NOTHING, blank=True, null=True)
#     sporcu = models.ForeignKey('Hltsporcu', models.DO_NOTHING, blank=True, null=True)
#     kurano = models.IntegerField(db_column='kuraNo', blank=True, null=True)  # Field name made lowercase.
#     sirano = models.IntegerField(db_column='siraNo', blank=True, null=True)  # Field name made lowercase.
#     kulupid = models.IntegerField(db_column='kulupId', blank=True, null=True)  # Field name made lowercase.
#     grubu = models.CharField(max_length=255, blank=True, null=True)
#     siklet = models.CharField(max_length=100, blank=True, null=True)
#     cinsiyet = models.CharField(max_length=100, blank=True, null=True)
#     koparma1 = models.IntegerField(blank=True, null=True)
#     koparma1b = models.IntegerField(blank=True, null=True)
#     koparma2 = models.IntegerField(blank=True, null=True)
#     koparma2b = models.IntegerField(blank=True, null=True)
#     koparma3 = models.IntegerField(blank=True, null=True)
#     koparma3b = models.IntegerField(blank=True, null=True)
#     koparmatoplam = models.IntegerField(db_column='koparmaToplam', blank=True, null=True)  # Field name made lowercase.
#     koparmaderece = models.IntegerField(db_column='koparmaDerece', blank=True, null=True)  # Field name made lowercase.
#     silkme1 = models.IntegerField(blank=True, null=True)
#     silkme1b = models.IntegerField(blank=True, null=True)
#     silkme2 = models.IntegerField(blank=True, null=True)
#     silkme2b = models.IntegerField(blank=True, null=True)
#     silkme3 = models.IntegerField(blank=True, null=True)
#     silkme3b = models.IntegerField(blank=True, null=True)
#     silkmetoplam = models.IntegerField(db_column='silkmeToplam', blank=True, null=True)  # Field name made lowercase.
#     silkmederece = models.IntegerField(db_column='silkmeDerece', blank=True, null=True)  # Field name made lowercase.
#     toplam = models.IntegerField(blank=True, null=True)
#     derece = models.IntegerField(blank=True, null=True)
#     puan = models.IntegerField(blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kilosu = models.FloatField(blank=True, null=True)
#     olayid = models.ForeignKey(Hltmusabakaolay, models.DO_NOTHING, db_column='olayId', blank=True, null=True)  # Field name made lowercase.
#     antrenor = models.IntegerField(blank=True, null=True)
#     koparmasirano = models.IntegerField(db_column='koparmaSiraNo', blank=True, null=True)  # Field name made lowercase.
#     silkmesirano = models.IntegerField(db_column='silkmeSiraNo', blank=True, null=True)  # Field name made lowercase.
#     kategoriadi_siklet = models.CharField(db_column='kategoriAdi_siklet', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     derece_str = models.CharField(max_length=45, blank=True, null=True)
#     okul = models.CharField(max_length=255, blank=True, null=True)
#     il = models.CharField(max_length=100, blank=True, null=True)
#     kategoriadi = models.CharField(db_column='kategoriAdi', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     kategori = models.ForeignKey(Hltkategori, models.DO_NOTHING, blank=True, null=True)
#     nerden = models.CharField(max_length=200, blank=True, null=True)
#     pdf_id = models.IntegerField(blank=True, null=True)
#     toplamsirano = models.BigIntegerField(db_column='toplamSiraNo', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltmusabakayonetimi'
#
#
# class Hltmusabakayonetimihakemt(models.Model):
#     musabakaid = models.IntegerField(db_column='musabakaId', blank=True, null=True)  # Field name made lowercase.
#     hakemid = models.IntegerField(db_column='hakemId', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     olayid = models.IntegerField(db_column='olayId', blank=True, null=True)  # Field name made lowercase.
#     kategoriid = models.IntegerField(db_column='kategoriId', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltmusabakayonetimihakemt'
#
#
# class Hltolimpiyatmadalya(models.Model):
#     sira_no = models.IntegerField(blank=True, null=True)
#     adi = models.CharField(max_length=200, blank=True, null=True)
#     bilgi = models.CharField(max_length=200, blank=True, null=True)
#     tur = models.CharField(max_length=45, blank=True, null=True)
#     adi_id = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'hltolimpiyatmadalya'
#
#
# class Hltolimpiyatsporcu(models.Model):
#     id = models.IntegerField(primary_key=True)
#     adi = models.CharField(max_length=45, blank=True, null=True)
#     bilgi = models.TextField(blank=True, null=True)
#     foto = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'hltolimpiyatsporcu'
#
#
# class Hltrekor(models.Model):
#     rekor = models.FloatField()
#     tipi = models.CharField(max_length=100)
#     sporcuid = models.IntegerField(db_column='sporcuId')  # Field name made lowercase.
#     siklet = models.CharField(max_length=100)
#     cinsiyet = models.CharField(max_length=100)
#     kopsilk = models.CharField(db_column='kopSilk', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     kulupid = models.PositiveIntegerField(db_column='kulupId', blank=True, null=True)  # Field name made lowercase.
#     baslangictarihi = models.DateTimeField(db_column='baslangicTarihi', blank=True, null=True)  # Field name made lowercase.
#     bitistarihi = models.DateTimeField(db_column='bitisTarihi', blank=True, null=True)  # Field name made lowercase.
#     yeri = models.CharField(max_length=1000, blank=True, null=True)
#     kategoriid = models.PositiveIntegerField(db_column='kategoriId', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltrekor'
#
#
# class Hltrekoral(models.Model):
#     number_1 = models.CharField(db_column='1', max_length=45, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_2 = models.FloatField(db_column='2', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_3 = models.CharField(db_column='3', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_4 = models.DateTimeField(db_column='4', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_5 = models.CharField(db_column='5', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_6 = models.DateTimeField(db_column='6', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7 = models.CharField(db_column='7', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_8 = models.CharField(db_column='8', max_length=45, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#
#     class Meta:
#         managed = False
#         db_table = 'hltrekoral'
#
#
# class Hltsiklet(models.Model):
#     cinsiyet = models.CharField(max_length=255, blank=True, null=True)
#     kilo = models.CharField(max_length=255, blank=True, null=True)
#     kopbaraj = models.IntegerField(db_column='kopBaraj', blank=True, null=True)  # Field name made lowercase.
#     silkbaraj = models.IntegerField(db_column='silkBaraj', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kategori_id = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'hltsiklet'
#
#
# class Hltsporcu(models.Model):
#     aciklama = models.CharField(max_length=255, blank=True, null=True)
#     ad = models.CharField(max_length=255, blank=True, null=True)
#     adsoyad = models.CharField(db_column='adSoyad', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     anneadi = models.CharField(db_column='anneAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     antrenor = models.BigIntegerField(blank=True, null=True)
#     ayakkabino = models.CharField(db_column='ayakkabiNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     babaadi = models.CharField(db_column='babaAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankaadi = models.CharField(db_column='bankaAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankahesapno = models.CharField(db_column='bankaHesapNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankahesapssahibi = models.CharField(db_column='bankaHesapSsahibi', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankaiban = models.CharField(db_column='bankaIban', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     bankasubeno = models.CharField(db_column='bankaSubeNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     boy = models.FloatField(blank=True, null=True)
#     ceptel = models.CharField(db_column='cepTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     cinsiyet = models.CharField(max_length=255, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     dogumtarihi = models.DateTimeField(db_column='dogumTarihi', blank=True, null=True)  # Field name made lowercase.
#     dogumyeri = models.CharField(db_column='dogumYeri', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     email = models.CharField(max_length=255, blank=True, null=True)
#     esofmanbedenno = models.CharField(db_column='esofmanBedenNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     evtel = models.CharField(db_column='evTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hastalikaciklama = models.CharField(db_column='hastalikAciklama', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     hastaliklimi = models.TextField(blank=True, null=True)  # This field type is a guess.
#     ikametadres = models.CharField(db_column='ikametAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ikametili = models.CharField(db_column='ikametIli', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     isadres = models.CharField(db_column='isAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     istel = models.CharField(db_column='isTel', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     izinalinacakadres = models.CharField(db_column='izinAlinacakAdres', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kangrubu = models.CharField(db_column='kanGrubu', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kategori = models.CharField(max_length=255, blank=True, null=True)
#     kilo = models.FloatField(blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     medenihali = models.CharField(db_column='medeniHali', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     meslek = models.CharField(max_length=255, blank=True, null=True)
#     nufusailesirano = models.IntegerField(db_column='nufusAileSiraNo', blank=True, null=True)  # Field name made lowercase.
#     nufusciltno = models.IntegerField(db_column='nufusCiltNo', blank=True, null=True)  # Field name made lowercase.
#     nufusil = models.CharField(db_column='nufusIl', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusilce = models.CharField(db_column='nufusIlce', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusmahallekoy = models.CharField(db_column='nufusMahalleKoy', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufusserino = models.CharField(db_column='nufusSeriNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     nufussirano = models.IntegerField(db_column='nufusSiraNo', blank=True, null=True)  # Field name made lowercase.
#     ogrenimdurumu = models.CharField(db_column='ogrenimDurumu', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     okuyor = models.TextField(blank=True, null=True)  # This field type is a guess.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     pasaportno = models.BigIntegerField(db_column='pasaportNo', blank=True, null=True)  # Field name made lowercase.
#     pasaporttarihi = models.DateTimeField(db_column='pasaportTarihi', blank=True, null=True)  # Field name made lowercase.
#     resim = models.TextField(blank=True, null=True)
#     soyad = models.CharField(max_length=255, blank=True, null=True)
#     tcno = models.BigIntegerField(db_column='tcNo', blank=True, null=True)  # Field name made lowercase.
#     tisortno = models.CharField(db_column='tisortNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     ulkeid = models.IntegerField(db_column='ulkeId', blank=True, null=True)  # Field name made lowercase.
#     yabancidil = models.CharField(db_column='yabanciDil', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     kulup = models.IntegerField(blank=True, null=True)
#     okul = models.CharField(max_length=255, blank=True, null=True)
#     cezabaslangictarihi = models.DateField(db_column='cezaBaslangicTarihi', blank=True, null=True)  # Field name made lowercase.
#     cezasuresi = models.IntegerField(db_column='cezaSuresi', blank=True, null=True)  # Field name made lowercase.
#     cezabitistarihi = models.DateField(db_column='cezaBitisTarihi', blank=True, null=True)  # Field name made lowercase.
#     cezanedeni = models.CharField(db_column='cezaNedeni', max_length=1000, blank=True, null=True)  # Field name made lowercase.
#     toplamcezasayisi = models.IntegerField(db_column='toplamCezaSayisi', blank=True, null=True)  # Field name made lowercase.
#     dogumyili = models.IntegerField(db_column='dogumYili', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hltsporcu'
#
#
# class Hlttablo(models.Model):
#     ilgilitabloid = models.IntegerField(db_column='ilgiliTabloId')  # Field name made lowercase.
#     tabloadi = models.CharField(db_column='tabloAdi', max_length=255)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'hlttablo'
#
#
# class Hltulke(models.Model):
#     adi = models.CharField(max_length=255)
#     kisaadi = models.CharField(db_column='kisaAdi', max_length=255)  # Field name made lowercase.
#     bayrak = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'hltulke'
#
#
# class Jarinfo(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     name = models.CharField(max_length=255, blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     value = models.CharField(max_length=255, blank=True, null=True)
#     module = models.ForeignKey('Module', models.DO_NOTHING, db_column='module', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'jarinfo'
#
#
# class Kobaltinfo(models.Model):
#     address = models.CharField(max_length=255, blank=True, null=True)
#     company = models.CharField(max_length=255, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     iscentre = models.TextField(db_column='isCentre')  # Field name made lowercase. This field type is a guess.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     licensecode = models.CharField(db_column='licenseCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     logo = models.TextField(blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     owner = models.CharField(max_length=255, blank=True, null=True)
#     parentkobilid = models.IntegerField(db_column='parentKobilId')  # Field name made lowercase.
#     productname = models.CharField(db_column='productName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     taxno = models.CharField(db_column='taxNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     taxoffice = models.CharField(db_column='taxOffice', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     telno = models.CharField(db_column='telNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     version = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'kobaltinfo'
#
#
# class License(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     expiredate = models.DateTimeField(db_column='expireDate', blank=True, null=True)  # Field name made lowercase.
#     isactive = models.TextField(db_column='isActive')  # Field name made lowercase. This field type is a guess.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     licenseno = models.CharField(db_column='licenseNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
#     cityheadship = models.ForeignKey(City, models.DO_NOTHING, db_column='cityHeadShip', blank=True, null=True)  # Field name made lowercase.
#     sportsclub = models.ForeignKey('Sportclub', models.DO_NOTHING, db_column='sportsClub', blank=True, null=True)  # Field name made lowercase.
#     branch = models.CharField(max_length=45, blank=True, null=True)
#     status = models.CharField(max_length=45, blank=True, null=True)
#     lisansphoto = models.CharField(db_column='lisansPhoto', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     reddetwhy = models.CharField(max_length=45, blank=True, null=True)
#     coach = models.ForeignKey('SbsCoach', models.DO_NOTHING, blank=True, null=True)
#     isferdi = models.IntegerField(db_column='isFerdi')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'license'
#
#
# class Location(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     entityid = models.IntegerField(db_column='entityId')  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     locationid = models.IntegerField(db_column='locationId')  # Field name made lowercase.
#     locationname = models.IntegerField(db_column='locationName', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     tablename = models.IntegerField(db_column='tableName', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'location'
#
#
# class Module(models.Model):
#     buttonname = models.CharField(db_column='buttonName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     mainentity = models.CharField(db_column='mainEntity', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     modulecode = models.IntegerField(db_column='moduleCode', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     path = models.CharField(max_length=255, blank=True, null=True)
#     parentmodule = models.ForeignKey('self', models.DO_NOTHING, db_column='parentModule', blank=True, null=True)  # Field name made lowercase.
#     haswindow = models.IntegerField(db_column='hasWindow', blank=True, null=True)  # Field name made lowercase.
#     isbase = models.IntegerField(db_column='isBase', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'module'
#
#
# class ModuleJarinfo(models.Model):
#     module_id = models.IntegerField()
#     entitylist_id = models.IntegerField(db_column='entityList_id', unique=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'module_jarinfo'
#
#
# class Nationality(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     flag = models.TextField(blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     name = models.CharField(max_length=255)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     shortname = models.CharField(db_column='shortName', max_length=255)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'nationality'
#
#
# class Neighborhood(models.Model):
#     districtid = models.ForeignKey(District, models.DO_NOTHING, db_column='districtId')  # Field name made lowercase.
#     name = models.CharField(max_length=100)
#     zipcode = models.CharField(db_column='zipCode', max_length=20)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'neighborhood'
#
#
# class Olympicachievement(models.Model):
#     id = models.IntegerField(primary_key=True)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=100, blank=True, null=True)
#     year = models.IntegerField(blank=True, null=True)
#     place = models.CharField(max_length=45, blank=True, null=True)
#     siklet = models.CharField(max_length=45, blank=True, null=True)
#     whichlift = models.IntegerField(db_column='whichLift', blank=True, null=True)  # Field name made lowercase.
#     whichmedal = models.IntegerField(db_column='whichMedal', blank=True, null=True)  # Field name made lowercase.
#     weight = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'olympicachievement'
#
#
# class Onlineuser(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     personid = models.IntegerField(db_column='personId')  # Field name made lowercase.
#     sessionid = models.BigIntegerField(db_column='sessionId', unique=True, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'onlineuser'
#
#
# class Parameters(models.Model):
#     code = models.CharField(max_length=255)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     parametername = models.CharField(db_column='parameterName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     modulecode = models.IntegerField(db_column='moduleCode', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'parameters'
#
#
# class Paymentcheck(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'paymentcheck'
#
#
# class PaymentcheckCheck(models.Model):
#     paymentcheck_id = models.IntegerField()
#     checks_id = models.IntegerField(unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'paymentcheck_check'
#
#
# class Paymentdetails(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(max_length=255, blank=True, null=True)
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     paymentcheck = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'paymentdetails'
#
#
# class PaymentdetailsPaymentbank(models.Model):
#     paymentdetails_id = models.IntegerField(db_column='PaymentDetails_id', primary_key=True)  # Field name made lowercase.
#     paymentbank = models.FloatField(db_column='paymentBank', blank=True, null=True)  # Field name made lowercase.
#     paymentbank_key = models.IntegerField(db_column='paymentBank_KEY')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'paymentdetails_paymentbank'
#         unique_together = (('paymentdetails_id', 'paymentbank_key'),)
#
#
# class PaymentdetailsPaymentcash(models.Model):
#     paymentdetails_id = models.IntegerField(db_column='PaymentDetails_id', primary_key=True)  # Field name made lowercase.
#     paymentcash = models.FloatField(db_column='paymentCash', blank=True, null=True)  # Field name made lowercase.
#     paymentcash_key = models.CharField(db_column='paymentCash_KEY', max_length=255)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'paymentdetails_paymentcash'
#         unique_together = (('paymentdetails_id', 'paymentcash_key'),)
#
#
# class Person(models.Model):
#     birthcity = models.CharField(db_column='birthCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     birthdate = models.DateTimeField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
#     ciltno = models.IntegerField(db_column='ciltNo', blank=True, null=True)  # Field name made lowercase.
#     city = models.CharField(max_length=255, blank=True, null=True)
#     county = models.CharField(max_length=255, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     deaddate = models.DateTimeField(db_column='deadDate', blank=True, null=True)  # Field name made lowercase.
#     familyorder = models.IntegerField(db_column='familyOrder', blank=True, null=True)  # Field name made lowercase.
#     fathername = models.CharField(db_column='fatherName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     image = models.TextField(blank=True, null=True)
#     isuser = models.IntegerField(db_column='isUser', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     mothername = models.CharField(db_column='motherName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=255, blank=True, null=True)
#     nationalityid = models.BigIntegerField(db_column='nationalityId', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     orderno = models.IntegerField(db_column='orderNo', blank=True, null=True)  # Field name made lowercase.
#     passaportno = models.BigIntegerField(db_column='passaportNo', blank=True, null=True)  # Field name made lowercase.
#     password = models.CharField(max_length=255, blank=True, null=True)
#     surname = models.CharField(max_length=255, blank=True, null=True)
#     bloodtype = models.CharField(db_column='bloodType', max_length=128, blank=True, null=True)  # Field name made lowercase.
#     sex = models.IntegerField(blank=True, null=True)
#     nationality = models.ForeignKey(Nationality, models.DO_NOTHING, db_column='nationality', blank=True, null=True)
#     sicilno = models.CharField(db_column='sicilNo', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     cardnumber = models.CharField(db_column='cardNumber', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     gender = models.IntegerField()
#     tc = models.CharField(max_length=45, blank=True, null=True)
#     height = models.CharField(max_length=45, blank=True, null=True)
#     weight = models.CharField(max_length=45, blank=True, null=True)
#     birthplace = models.CharField(db_column='birthPlace', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     profileimage = models.CharField(db_column='profileImage', max_length=100, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'person'
#
#
# class Prevalent(models.Model):
#     address = models.CharField(max_length=255, blank=True, null=True)
#     authorityname = models.CharField(db_column='authorityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     code = models.BigIntegerField(unique=True, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     credibility = models.TextField(blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     doyousale = models.TextField(db_column='doYouSale')  # Field name made lowercase. This field type is a guess.
#     email = models.CharField(max_length=255, blank=True, null=True)
#     individual = models.TextField()  # This field type is a guess.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     mobilephone = models.CharField(db_column='mobilePhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=255)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     phone1 = models.CharField(max_length=255, blank=True, null=True)
#     phone2 = models.CharField(max_length=255, blank=True, null=True)
#     point = models.FloatField()
#     postalcode = models.CharField(db_column='postalCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     risklimit = models.FloatField(db_column='riskLimit', blank=True, null=True)  # Field name made lowercase.
#     smssendable = models.TextField(db_column='smsSendable')  # Field name made lowercase. This field type is a guess.
#     taxno = models.CharField(db_column='taxNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     taxoffice = models.CharField(db_column='taxOffice', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     type = models.TextField(blank=True, null=True)
#     bank = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'prevalent'
#
#
# class PrevalentPaymentdetails(models.Model):
#     prevalent_id = models.IntegerField()
#     payments_id = models.IntegerField(unique=True)
#
#     class Meta:
#         managed = False
#         db_table = 'prevalent_paymentdetails'
#
#
# class ProductPimages(models.Model):
#     product_id = models.IntegerField(db_column='Product_id')  # Field name made lowercase.
#     pimages = models.TextField(db_column='pImages', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'product_pimages'
#
#
# class Punishment(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     description = models.TextField(blank=True, null=True)
#     entityid = models.IntegerField(db_column='entityId')  # Field name made lowercase.
#     finishdate = models.DateTimeField(db_column='finishDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
#     tablename = models.IntegerField(db_column='tableName', blank=True, null=True)  # Field name made lowercase.
#     type = models.ForeignKey(Categoryitem, models.DO_NOTHING, db_column='type', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'punishment'
#
#
# class Representation(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     finishdate = models.DateTimeField(db_column='finishDate', blank=True, null=True)  # Field name made lowercase.
#     isactive = models.TextField(db_column='isActive')  # Field name made lowercase. This field type is a guess.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
#     department = models.ForeignKey(Category, models.DO_NOTHING, db_column='department', blank=True, null=True)
#     person = models.ForeignKey(Person, models.DO_NOTHING, db_column='person', blank=True, null=True)
#     position = models.ForeignKey(Category, models.DO_NOTHING, db_column='position', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'representation'
#
#
# class Role(models.Model):
#     role_id = models.AutoField(db_column='ROLE_ID', primary_key=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     modules = models.CharField(max_length=1000, blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     roletype = models.IntegerField(db_column='roleType', blank=True, null=True)  # Field name made lowercase.
#     category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'role'
#
#
# class Saledkobalt(models.Model):
#     address = models.CharField(max_length=255, blank=True, null=True)
#     authorityname = models.CharField(db_column='authorityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     brand = models.CharField(max_length=255)
#     company = models.CharField(max_length=255)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     iscentre = models.TextField(db_column='isCentre')  # Field name made lowercase. This field type is a guess.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     license = models.CharField(unique=True, max_length=255)
#     mobileid = models.CharField(db_column='mobileId', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     mobilephone = models.CharField(db_column='mobilePhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     modules = models.CharField(max_length=1000, blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     parentkobilid = models.IntegerField(db_column='parentKobilId')  # Field name made lowercase.
#     rate = models.IntegerField()
#     sublocation = models.CharField(db_column='subLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     taxoffice = models.CharField(db_column='taxOffice', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tcno = models.CharField(db_column='tcNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     tel1 = models.CharField(max_length=255, blank=True, null=True)
#     tel2 = models.CharField(max_length=255, blank=True, null=True)
#     thiskobilid = models.IntegerField(db_column='thisKobilId', unique=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'saledkobalt'
#
#
# class SbsActivity(models.Model):
#     type = models.IntegerField(db_column='Type')  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
#     finishdate = models.DateTimeField(db_column='finishDate', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=255)
#     eventplace = models.CharField(db_column='eventPlace', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     year = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_activity'
#
#
# class SbsAthlete(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     communication = models.OneToOneField('SbsCommunicationn', models.DO_NOTHING)
#     person = models.OneToOneField('SbsPerson', models.DO_NOTHING)
#     user = models.OneToOneField(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_athlete'
#
#
# class SbsAthleteBelts(models.Model):
#     athlete = models.ForeignKey(SbsAthlete, models.DO_NOTHING)
#     level = models.ForeignKey('SbsLevel', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_athlete_belts'
#         unique_together = (('athlete', 'level'),)
#
#
# class SbsBeltexam(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     examdate = models.DateField(db_column='examDate')  # Field name made lowercase.
#     paymenttype = models.CharField(db_column='paymentType', max_length=128)  # Field name made lowercase.
#     dekont = models.CharField(max_length=100)
#     dekontdate = models.DateField(db_column='dekontDate', blank=True, null=True)  # Field name made lowercase.
#     dekontdescription = models.CharField(db_column='dekontDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     status = models.CharField(max_length=128)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     branch = models.CharField(max_length=128)
#     sportclub = models.ForeignKey('SbsSportsclub', models.DO_NOTHING, db_column='sportClub_id')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_beltexam'
#
#
# class SbsBeltexamAthletes(models.Model):
#     beltexam = models.ForeignKey(SbsBeltexam, models.DO_NOTHING)
#     athlete = models.ForeignKey(SbsAthlete, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_beltexam_athletes'
#         unique_together = (('beltexam', 'athlete'),)
#
#
# class SbsBeltexamCoachs(models.Model):
#     beltexam = models.ForeignKey(SbsBeltexam, models.DO_NOTHING)
#     coach = models.ForeignKey('SbsCoach', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_beltexam_coachs'
#         unique_together = (('beltexam', 'coach'),)
#
#
# class SbsBranch(models.Model):
#     name = models.CharField(max_length=120, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_branch'
#
#
# class SbsCategoryitem(models.Model):
#     name = models.CharField(max_length=255)
#     forwhichclazz = models.CharField(db_column='forWhichClazz', max_length=255)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     branch = models.CharField(max_length=128, blank=True, null=True)
#     isfirst = models.IntegerField(db_column='isFirst', blank=True, null=True)  # Field name made lowercase.
#     parent_id = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_categoryitem'
#
#
# class SbsCity(models.Model):
#     name = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_city'
#
#
# class SbsClaim(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     title = models.CharField(max_length=1000)
#     project = models.CharField(max_length=128)
#     status = models.CharField(max_length=128)
#     definition = models.CharField(max_length=1000)
#     importancesort = models.CharField(db_column='importanceSort', max_length=128)  # Field name made lowercase.
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_claim'
#
#
# class SbsClaimFiles(models.Model):
#     claim = models.ForeignKey(SbsClaim, models.DO_NOTHING)
#     file = models.ForeignKey('SbsFile', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_claim_files'
#         unique_together = (('claim', 'file'),)
#
#
# class SbsClubrole(models.Model):
#     name = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_clubrole'
#
#
# class SbsCoach(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     communication = models.ForeignKey(Communication, models.DO_NOTHING)
#     person = models.ForeignKey(Person, models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     iban = models.CharField(max_length=120, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_coach'
#
#
# class SbsCoachGrades(models.Model):
#     coach_id = models.IntegerField()
#     level = models.ForeignKey('SbsLevel', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_coach_grades'
#
#
# class SbsCoachVisa(models.Model):
#     coach = models.ForeignKey(SbsCoach, models.DO_NOTHING)
#     level = models.ForeignKey('SbsLevel', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_coach_visa'
#
#
# class SbsCoachapplication(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     status = models.CharField(max_length=128)
#     dekont = models.CharField(max_length=100, blank=True, null=True)
#     coach = models.ForeignKey(SbsCoach, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_coachapplication'
#
#
# class SbsCommunicationn(models.Model):
#     postalcode = models.CharField(db_column='postalCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     phonenumber = models.CharField(db_column='phoneNumber', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     phonenumber2 = models.CharField(db_column='phoneNumber2', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     address = models.TextField(blank=True, null=True)
#     city = models.ForeignKey(SbsCity, models.DO_NOTHING, db_column='city')
#     country = models.ForeignKey('SbsCountry', models.DO_NOTHING, db_column='country')
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_communicationn'
#
#
# class SbsCountry(models.Model):
#     name = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_country'
#
#
# class SbsDirectorycommission(models.Model):
#     name = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_directorycommission'
#
#
# class SbsDirectorymember(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     commission = models.ForeignKey(SbsDirectorycommission, models.DO_NOTHING)
#     communication = models.ForeignKey(Communication, models.DO_NOTHING)
#     person = models.ForeignKey(Person, models.DO_NOTHING)
#     role = models.ForeignKey('SbsDirectorymemberrole', models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_directorymember'
#
#
# class SbsDirectorymemberrole(models.Model):
#     name = models.TextField()
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_directorymemberrole'
#
#
# class SbsFile(models.Model):
#     file = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_file'
#
#
# class SbsJudge(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     communication = models.ForeignKey(Communication, models.DO_NOTHING)
#     person = models.ForeignKey(Person, models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     iban = models.CharField(max_length=120, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_judge'
#
#
# class SbsJudgeGrades(models.Model):
#     judge = models.ForeignKey(SbsJudge, models.DO_NOTHING)
#     level = models.ForeignKey('SbsLevel', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_judge_grades'
#
#
# class SbsJudgeVisa(models.Model):
#     judge = models.ForeignKey(SbsJudge, models.DO_NOTHING)
#     level = models.ForeignKey('SbsLevel', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_judge_visa'
#
#
# class SbsJudgeapplication(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     status = models.CharField(max_length=128)
#     dekont = models.CharField(max_length=100, blank=True, null=True)
#     judge = models.ForeignKey(SbsJudge, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_judgeapplication'
#
#
# class SbsLevel(models.Model):
#     leveltype = models.CharField(db_column='levelType', max_length=128)  # Field name made lowercase.
#     branch = models.CharField(max_length=128)
#     isactive = models.IntegerField(db_column='isActive')  # Field name made lowercase.
#     startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
#     expiredate = models.DateField(db_column='expireDate', blank=True, null=True)  # Field name made lowercase.
#     durationday = models.IntegerField(db_column='durationDay', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     status = models.CharField(max_length=128)
#     dekont = models.CharField(max_length=100, blank=True, null=True)
#     form = models.CharField(max_length=100)
#     city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
#     definition = models.ForeignKey(Categoryitem, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_level'
#
#
# class SbsLicense(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     branch = models.CharField(max_length=128)
#     isactive = models.IntegerField(db_column='isActive')  # Field name made lowercase.
#     licenseno = models.CharField(db_column='licenseNo', max_length=255)  # Field name made lowercase.
#     expiredate = models.DateField(db_column='expireDate')  # Field name made lowercase.
#     startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
#     status = models.CharField(max_length=128)
#     lisansphoto = models.CharField(db_column='lisansPhoto', max_length=100)  # Field name made lowercase.
#     reddetwhy = models.CharField(max_length=255, blank=True, null=True)
#     cityheadship = models.ForeignKey(SbsCity, models.DO_NOTHING, db_column='cityHeadShip_id')  # Field name made lowercase.
#     sportsclub = models.ForeignKey('SbsSportsclub', models.DO_NOTHING, db_column='sportsClub_id')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_license'
#
#
# class SbsLogs(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate')  # Field name made lowercase.
#     subject = models.CharField(max_length=150, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user')
#     ip = models.CharField(max_length=20, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_logs'
#
#
# class SbsMenu(models.Model):
#     name = models.CharField(max_length=120, blank=True, null=True)
#     url = models.CharField(max_length=120, blank=True, null=True)
#     is_parent = models.IntegerField()
#     is_show = models.IntegerField()
#     fa_icon = models.CharField(max_length=120, blank=True, null=True)
#     parent_id = models.IntegerField(blank=True, null=True)
#     permission = models.OneToOneField(AuthPermission, models.DO_NOTHING, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menu'
#
#
# class SbsMenuadmin(models.Model):
#     name = models.CharField(max_length=120, blank=True, null=True)
#     url = models.CharField(max_length=120, blank=True, null=True)
#     is_parent = models.IntegerField()
#     is_show = models.IntegerField()
#     fa_icon = models.CharField(max_length=120, blank=True, null=True)
#     parent_id = models.IntegerField(blank=True, null=True)
#     sorting = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menuadmin'
#
#
# class SbsMenuadminPermission(models.Model):
#     menuadmin = models.ForeignKey(SbsMenuadmin, models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menuadmin_permission'
#         unique_together = (('menuadmin', 'user'),)
#
#
# class SbsMenuathlete(models.Model):
#     name = models.CharField(max_length=120, blank=True, null=True)
#     url = models.CharField(max_length=120, blank=True, null=True)
#     is_parent = models.IntegerField()
#     is_show = models.IntegerField()
#     fa_icon = models.CharField(max_length=120, blank=True, null=True)
#     parent_id = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menuathlete'
#
#
# class SbsMenuathletePermission(models.Model):
#     menuathlete = models.ForeignKey(SbsMenuathlete, models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menuathlete_permission'
#         unique_together = (('menuathlete', 'user'),)
#
#
# class SbsMenuclubuser(models.Model):
#     name = models.CharField(max_length=120, blank=True, null=True)
#     url = models.CharField(max_length=120, blank=True, null=True)
#     is_parent = models.IntegerField()
#     is_show = models.IntegerField()
#     fa_icon = models.CharField(max_length=120, blank=True, null=True)
#     parent_id = models.IntegerField(blank=True, null=True)
#     sorting = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menuclubuser'
#
#
# class SbsMenuclubuserPermission(models.Model):
#     menuclubuser = models.ForeignKey(SbsMenuclubuser, models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menuclubuser_permission'
#         unique_together = (('menuclubuser', 'user'),)
#
#
# class SbsMenucoach(models.Model):
#     name = models.CharField(max_length=120, blank=True, null=True)
#     url = models.CharField(max_length=120, blank=True, null=True)
#     is_parent = models.IntegerField()
#     is_show = models.IntegerField()
#     fa_icon = models.CharField(max_length=120, blank=True, null=True)
#     parent_id = models.IntegerField(blank=True, null=True)
#     sorting = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menucoach'
#
#
# class SbsMenucoachPermission(models.Model):
#     menucoach = models.ForeignKey(SbsMenucoach, models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menucoach_permission'
#         unique_together = (('menucoach', 'user'),)
#
#
# class SbsMenudirectory(models.Model):
#     name = models.CharField(max_length=120, blank=True, null=True)
#     url = models.CharField(max_length=120, blank=True, null=True)
#     is_parent = models.IntegerField()
#     is_show = models.IntegerField()
#     fa_icon = models.CharField(max_length=120, blank=True, null=True)
#     parent_id = models.IntegerField(blank=True, null=True)
#     sorting = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menudirectory'
#
#
# class SbsMenudirectoryPermission(models.Model):
#     menudirectory = models.ForeignKey(SbsMenudirectory, models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menudirectory_permission'
#         unique_together = (('menudirectory', 'user'),)
#
#
# class SbsMenureferee(models.Model):
#     name = models.CharField(max_length=120, blank=True, null=True)
#     url = models.CharField(max_length=120, blank=True, null=True)
#     is_parent = models.IntegerField()
#     is_show = models.IntegerField()
#     fa_icon = models.CharField(max_length=120, blank=True, null=True)
#     parent_id = models.IntegerField(blank=True, null=True)
#     sorting = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menureferee'
#
#
# class SbsMenurefereePermission(models.Model):
#     menureferee = models.ForeignKey(SbsMenureferee, models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_menureferee_permission'
#         unique_together = (('menureferee', 'user'),)
#
#
# class SbsPerson(models.Model):
#     tc = models.CharField(max_length=120, blank=True, null=True)
#     height = models.CharField(max_length=120, blank=True, null=True)
#     weight = models.CharField(max_length=120, blank=True, null=True)
#     birthplace = models.CharField(max_length=120, blank=True, null=True)
#     mothername = models.CharField(db_column='motherName', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     fathername = models.CharField(db_column='fatherName', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     profileimage = models.CharField(db_column='profileImage', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     birthdate = models.DateField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
#     bloodtype = models.CharField(db_column='bloodType', max_length=128)  # Field name made lowercase.
#     gender = models.CharField(max_length=128)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_person'
#
#
# class SbsPreregistration(models.Model):
#     status = models.CharField(max_length=128)
#     tc = models.CharField(max_length=120)
#     height = models.CharField(max_length=120, blank=True, null=True)
#     weight = models.CharField(max_length=120, blank=True, null=True)
#     birthplace = models.CharField(max_length=120, blank=True, null=True)
#     mothername = models.CharField(db_column='motherName', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     fathername = models.CharField(db_column='fatherName', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     profileimage = models.CharField(db_column='profileImage', max_length=100)  # Field name made lowercase.
#     birthdate = models.DateField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
#     bloodtype = models.CharField(db_column='bloodType', max_length=128, blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(max_length=128)
#     postalcode = models.CharField(db_column='postalCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     phonenumber = models.CharField(db_column='phoneNumber', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     phonenumber2 = models.CharField(db_column='phoneNumber2', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     address = models.TextField(blank=True, null=True)
#     name = models.CharField(max_length=120, blank=True, null=True)
#     shortname = models.CharField(db_column='shortName', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     foundingdate = models.DateField(db_column='foundingDate', blank=True, null=True)  # Field name made lowercase.
#     clubmail = models.CharField(db_column='clubMail', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     logo = models.CharField(max_length=100, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     isformal = models.IntegerField(db_column='isFormal')  # Field name made lowercase.
#     clubpostalcode = models.CharField(db_column='clubpostalCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     clubphonenumber = models.CharField(db_column='clubphoneNumber', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     clubphonenumber2 = models.CharField(db_column='clubphoneNumber2', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     clubaddress = models.TextField(blank=True, null=True)
#     first_name = models.CharField(max_length=30, blank=True, null=True)
#     last_name = models.CharField(max_length=150, blank=True, null=True)
#     email = models.CharField(max_length=254, blank=True, null=True)
#     is_staff = models.IntegerField(blank=True, null=True)
#     is_active = models.IntegerField(blank=True, null=True)
#     dekont = models.CharField(max_length=100, blank=True, null=True)
#     petition = models.CharField(max_length=100)
#     city = models.ForeignKey(City, models.DO_NOTHING)
#     clubcity = models.ForeignKey(City, models.DO_NOTHING)
#     clubcountry = models.ForeignKey(Country, models.DO_NOTHING)
#     country = models.ForeignKey(Country, models.DO_NOTHING)
#     role = models.ForeignKey(SbsClubrole, models.DO_NOTHING)
#     iban = models.CharField(max_length=120, blank=True, null=True)
#     iscoach = models.IntegerField(db_column='isCoach')  # Field name made lowercase.
#     kademe_belge = models.CharField(max_length=100, blank=True, null=True)
#     kademe_definition = models.CharField(max_length=150, blank=True, null=True)
#     kademe_startdate = models.DateField(db_column='kademe_startDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_preregistration'
#
#
# class SbsPunishment(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     startdate = models.DateTimeField(db_column='startDate')  # Field name made lowercase.
#     expiredate = models.DateTimeField(db_column='expireDate')  # Field name made lowercase.
#     durationday = models.IntegerField(db_column='durationDay')  # Field name made lowercase.
#     description = models.CharField(max_length=1000, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_punishment'
#
#
# class SbsQuestion(models.Model):
#     question = models.CharField(max_length=400, blank=True, null=True)
#     isactiv = models.IntegerField(db_column='isActiv', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate')  # Field name made lowercase.
#     reaply = models.CharField(max_length=400, blank=True, null=True)
#     count = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_question'
#
#
# class SbsReferencecoach(models.Model):
#     status = models.CharField(max_length=128, blank=True, null=True)
#     iban = models.CharField(max_length=120)
#     tc = models.CharField(max_length=120, blank=True, null=True)
#     height = models.CharField(max_length=120, blank=True, null=True)
#     weight = models.CharField(max_length=120, blank=True, null=True)
#     birthplace = models.CharField(max_length=120, blank=True, null=True)
#     mothername = models.CharField(db_column='motherName', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     fathername = models.CharField(db_column='fatherName', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     profileimage = models.CharField(db_column='profileImage', max_length=100)  # Field name made lowercase.
#     birthdate = models.DateTimeField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
#     bloodtype = models.CharField(db_column='bloodType', max_length=128, blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(max_length=128, blank=True, null=True)
#     postalcode = models.CharField(db_column='postalCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     phonenumber = models.CharField(db_column='phoneNumber', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     phonenumber2 = models.CharField(db_column='phoneNumber2', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     address = models.CharField(max_length=255, blank=True, null=True)
#     first_name = models.CharField(max_length=30, blank=True, null=True)
#     last_name = models.CharField(max_length=150, blank=True, null=True)
#     email = models.CharField(max_length=254, blank=True, null=True)
#     is_staff = models.IntegerField(blank=True, null=True)
#     is_active = models.IntegerField(blank=True, null=True)
#     city = models.ForeignKey(City, models.DO_NOTHING)
#     country = models.ForeignKey(Country, models.DO_NOTHING)
#     kademe_belge = models.CharField(max_length=100)
#     kademe_definition_id = models.IntegerField(blank=True, null=True)
#     kademe_startdate = models.DateField(db_column='kademe_startDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_referencecoach'
#
#
# class SbsReferencereferee(models.Model):
#     status = models.CharField(max_length=128, blank=True, null=True)
#     iban = models.CharField(max_length=120)
#     tc = models.CharField(max_length=120, blank=True, null=True)
#     height = models.CharField(max_length=120, blank=True, null=True)
#     weight = models.CharField(max_length=120, blank=True, null=True)
#     birthplace = models.CharField(max_length=120, blank=True, null=True)
#     mothername = models.CharField(db_column='motherName', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     fathername = models.CharField(db_column='fatherName', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     profileimage = models.CharField(db_column='profileImage', max_length=100)  # Field name made lowercase.
#     birthdate = models.DateTimeField(db_column='birthDate', blank=True, null=True)  # Field name made lowercase.
#     bloodtype = models.CharField(db_column='bloodType', max_length=128, blank=True, null=True)  # Field name made lowercase.
#     gender = models.CharField(max_length=128, blank=True, null=True)
#     postalcode = models.CharField(db_column='postalCode', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     phonenumber = models.CharField(db_column='phoneNumber', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     phonenumber2 = models.CharField(db_column='phoneNumber2', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     address = models.CharField(max_length=255, blank=True, null=True)
#     city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
#     email = models.CharField(max_length=254, blank=True, null=True)
#     first_name = models.CharField(max_length=45, blank=True, null=True)
#     is_active = models.IntegerField(blank=True, null=True)
#     is_staff = models.IntegerField(blank=True, null=True)
#     last_name = models.CharField(max_length=150, blank=True, null=True)
#     country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
#     kademe_definition_id = models.IntegerField(blank=True, null=True)
#     kademe_startdate = models.DateField(db_column='kademe_startDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_referencereferee'
#
#
# class SbsSandaathlete(models.Model):
#     athlete = models.OneToOneField(SbsAthlete, models.DO_NOTHING)
#     competition = models.OneToOneField(Competition, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_sandaathlete'
#
#
# class SbsSimplecategory(models.Model):
#     categoryname = models.CharField(db_column='categoryName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     compcategorycompleted = models.IntegerField(db_column='compCategoryCompleted', blank=True, null=True)  # Field name made lowercase.
#     comporder = models.IntegerField(db_column='compOrder', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     isduilian = models.IntegerField(db_column='isDuilian', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate')  # Field name made lowercase.
#     playersordered = models.IntegerField(db_column='playersOrdered', blank=True, null=True)  # Field name made lowercase.
#     recordcompleted = models.IntegerField(db_column='recordCompleted', blank=True, null=True)  # Field name made lowercase.
#     competition = models.IntegerField(blank=True, null=True)
#     area = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_simplecategory'
#
#
# class SbsSportclubuser(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     communication = models.ForeignKey(Communication, models.DO_NOTHING)
#     person = models.ForeignKey(Person, models.DO_NOTHING)
#     role = models.ForeignKey(SbsClubrole, models.DO_NOTHING)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     dataaccesscontrol = models.IntegerField(db_column='dataAccessControl', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_sportclubuser'
#
#
# class SbsSportsclub(models.Model):
#     name = models.CharField(max_length=120, blank=True, null=True)
#     shortname = models.CharField(db_column='shortName', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     foundingdate = models.CharField(db_column='foundingDate', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     clubmail = models.CharField(db_column='clubMail', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     logo = models.CharField(max_length=100, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     isformal = models.IntegerField(db_column='isFormal')  # Field name made lowercase.
#     communication = models.OneToOneField(SbsCommunicationn, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_sportsclub'
#
#
# class SbsSportsclubCoachs(models.Model):
#     sportsclub = models.ForeignKey(SbsSportsclub, models.DO_NOTHING)
#     coach = models.ForeignKey(SbsCoach, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_sportsclub_coachs'
#         unique_together = (('sportsclub', 'coach'),)
#
#
# class SbsTaoluathlete(models.Model):
#     athlete = models.OneToOneField(SbsAthlete, models.DO_NOTHING)
#     competition = models.OneToOneField(Competition, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_taoluathlete'
#
#
# class SbsTaoluathleteCategori(models.Model):
#     taoluathlete = models.ForeignKey(SbsTaoluathlete, models.DO_NOTHING)
#     simplecategory = models.ForeignKey(SbsSimplecategory, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_taoluathlete_categori'
#         unique_together = (('taoluathlete', 'simplecategory'),)
#
#
# class SbsVisaseminar(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate')  # Field name made lowercase.
#     modificationdate = models.DateTimeField(db_column='modificationDate')  # Field name made lowercase.
#     name = models.CharField(max_length=1000)
#     startdate = models.DateTimeField(db_column='startDate')  # Field name made lowercase.
#     finishdate = models.DateTimeField(db_column='finishDate')  # Field name made lowercase.
#     location = models.CharField(max_length=1000)
#     branch = models.CharField(max_length=128)
#     status = models.CharField(max_length=128)
#     forwhichclazz = models.CharField(db_column='forWhichClazz', max_length=255)  # Field name made lowercase.
#     year = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_visaseminar'
#
#
# class SbsVisaseminarCoach(models.Model):
#     visaseminar = models.ForeignKey(SbsVisaseminar, models.DO_NOTHING)
#     coach = models.ForeignKey(SbsCoach, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_visaseminar_coach'
#         unique_together = (('visaseminar', 'coach'),)
#
#
# class SbsVisaseminarCoachapplication(models.Model):
#     visaseminar = models.ForeignKey(SbsVisaseminar, models.DO_NOTHING)
#     coachapplication = models.ForeignKey(SbsCoachapplication, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_visaseminar_coachapplication'
#         unique_together = (('visaseminar', 'coachapplication'),)
#
#
# class SbsVisaseminarJudgeapplication(models.Model):
#     visaseminar = models.ForeignKey(SbsVisaseminar, models.DO_NOTHING)
#     judgeapplication = models.ForeignKey(SbsJudgeapplication, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_visaseminar_judgeapplication'
#         unique_together = (('visaseminar', 'judgeapplication'),)
#
#
# class SbsVisaseminarReferee(models.Model):
#     visaseminar = models.ForeignKey(SbsVisaseminar, models.DO_NOTHING)
#     judge = models.ForeignKey(SbsJudge, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sbs_visaseminar_referee'
#         unique_together = (('visaseminar', 'judge'),)
#
#
# class Smsinfo(models.Model):
#     balance = models.IntegerField()
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     entityid = models.IntegerField(db_column='entityId')  # Field name made lowercase.
#     header = models.CharField(max_length=255)
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     password = models.CharField(max_length=255)
#     tablename = models.IntegerField(db_column='tableName', blank=True, null=True)  # Field name made lowercase.
#     usercode = models.CharField(db_column='userCode', max_length=255)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'smsinfo'
#
#
# class Sportclub(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=255, blank=True, null=True)
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     username = models.CharField(max_length=120, blank=True, null=True)
#     password = models.CharField(max_length=120, blank=True, null=True)
#     shortname = models.CharField(db_column='shortName', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     foundingdate = models.CharField(db_column='foundingDate', max_length=120, blank=True, null=True)  # Field name made lowercase.
#     clubmail = models.CharField(db_column='clubMail', max_length=45, blank=True, null=True)  # Field name made lowercase.
#     logo = models.CharField(max_length=100, blank=True, null=True)
#     isformal = models.IntegerField(db_column='isFormal', blank=True, null=True)  # Field name made lowercase.
#     communication = models.IntegerField(blank=True, null=True)
#     dataaccesscontrol = models.IntegerField(db_column='dataAccessControl', blank=True, null=True)  # Field name made lowercase.
#     sportclubcol = models.CharField(max_length=45, blank=True, null=True)
#     isregister = models.IntegerField(db_column='isRegister', blank=True, null=True)  # Field name made lowercase.
#     petition = models.CharField(max_length=100, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sportclub'
#
#
# class SportclubClubuser(models.Model):
#     sportsclub = models.ForeignKey(Sportclub, models.DO_NOTHING)
#     sportclubuser = models.ForeignKey(SbsSportclubuser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sportclub_clubuser'
#
#
# class SportclubCoachs(models.Model):
#     sportsclub = models.ForeignKey(Sportclub, models.DO_NOTHING)
#     coach = models.ForeignKey(SbsCoach, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'sportclub_coachs'
#
#
# class Subdocument(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     data = models.TextField(blank=True, null=True)
#     fileextension = models.CharField(db_column='fileExtension', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     filename = models.CharField(db_column='fileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     filesize = models.FloatField(db_column='fileSize')  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     path = models.CharField(max_length=255, blank=True, null=True)
#     thumbnailid = models.IntegerField(db_column='thumbnailId')  # Field name made lowercase.
#     archivedocument = models.ForeignKey(Archivedocument, models.DO_NOTHING, db_column='archiveDocument', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'subdocument'
#
#
# class Town(models.Model):
#     cityid = models.ForeignKey(City, models.DO_NOTHING, db_column='cityId')  # Field name made lowercase.
#     name = models.CharField(max_length=50)
#     kobilid = models.IntegerField(db_column='kobilId', blank=True, null=True)  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'town'
#
#
# class Userinouttime(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     which = models.CharField(max_length=255, blank=True, null=True)
#     user = models.ForeignKey(Person, models.DO_NOTHING, db_column='user', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'userinouttime'
#
#
# class Weight(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     weight = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'weight'
#
#
# class Workorder(models.Model):
#     address = models.CharField(max_length=255, blank=True, null=True)
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     description = models.CharField(max_length=255, blank=True, null=True)
#     finishdate = models.DateTimeField(db_column='finishDate', blank=True, null=True)  # Field name made lowercase.
#     isoutoflist = models.TextField(db_column='isOutOfList')  # Field name made lowercase. This field type is a guess.
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     length = models.FloatField()
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     area = models.FloatField()
#     startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
#     status = models.IntegerField(blank=True, null=True)
#     width = models.FloatField()
#     workdefinition = models.CharField(db_column='workDefinition', max_length=255, blank=True, null=True)  # Field name made lowercase.
#     worktype = models.IntegerField(db_column='workType', blank=True, null=True)  # Field name made lowercase.
#     authorizedperson = models.ForeignKey(Person, models.DO_NOTHING, db_column='authorizedPerson', blank=True, null=True)  # Field name made lowercase.
#     creatorperson = models.ForeignKey(Person, models.DO_NOTHING, db_column='creatorPerson', blank=True, null=True)  # Field name made lowercase.
#     department = models.ForeignKey(Category, models.DO_NOTHING, db_column='department', blank=True, null=True)
#     code = models.CharField(max_length=45)
#
#     class Meta:
#         managed = False
#         db_table = 'workorder'
#
#
# class Worktypesize(models.Model):
#     creationdate = models.DateTimeField(db_column='creationDate', blank=True, null=True)  # Field name made lowercase.
#     distance = models.FloatField()
#     height = models.FloatField()
#     kobilid = models.IntegerField(db_column='kobilId')  # Field name made lowercase.
#     operationdate = models.DateTimeField(db_column='operationDate', blank=True, null=True)  # Field name made lowercase.
#     size = models.FloatField()
#     which = models.IntegerField(blank=True, null=True)
#     workorder = models.ForeignKey(Workorder, models.DO_NOTHING, db_column='workOrder', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'worktypesize'