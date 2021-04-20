import enum

from django.db import models

from sbs.models.File import File




from django.contrib.auth.models import User
class Claim(models.Model):

    WAITED = 'Beklemede'
    APPROVED = 'İzlemeye Alındı'
    PROPOUND = 'İşlem Devam Ediliyor'
    DENIED = 'Reddedildi'
    END='Bitti'

    STATUS_CHOICES = (
        (APPROVED, 'İşlem izlenmeye alındı'),
        (PROPOUND, 'İşlem Devam Ediyor'),
        (DENIED, 'İşlem Reddedildi'),
        (WAITED, 'İşlem Beklemede'),
        (END,'İşlem Bitti')
    )

    SBS = 'SPOR BİLGİ SİSTEMİ'
    MOBİL = 'MOBİL UYGULAMA'
    WEBSİTE = 'WEB SİTE'

    STATUS_PROJECT = (
        (SBS, 'SPOR BİLGİ SİSTEMİ'),
        (MOBİL, 'MOBİL UYGULAMA'),
        (WEBSİTE, 'WEB SİTE'),
    )

    ACİL = 'ACİL'
    ONEMLİ ='ÖNEMLİ'
    AZONEMLİ = 'AZ ÖNEMLİ'

    STATUS_PROJECT = (
        (SBS, 'SPOR BİLGİ SİSTEMİ'),
        (MOBİL, 'MOBİL UYGULAMA'),
        (WEBSİTE, 'WEB SİTE'),
    )

    İMPORTANCE = (
        (ACİL, 'ACİL'),
        (ONEMLİ, 'ÖNEMLİ'),
        (AZONEMLİ, 'AZ ÖNEMLİ'),
    )
    creationDate = models.DateTimeField(auto_now_add=True)
    modificationDate = models.DateTimeField(auto_now=True)
    # baslık
    title= models.CharField(blank=False, null=False, max_length=1000)
    # proje secimi
    project = models.CharField(max_length=128, verbose_name='Proje Seçiniz', choices=STATUS_PROJECT, default=SBS)
    # proje durumu
    status = models.CharField(max_length=128, verbose_name='Kayıt Durumu', choices=STATUS_CHOICES, default=WAITED)
    # proje açıklama
    definition= models.CharField(blank=False, null=False, max_length=1000)
    # önem durumu
    importanceSort = models.CharField(max_length=128, verbose_name='Önem Durumu', choices=İMPORTANCE, default=ACİL)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    files=models.ManyToManyField(File)


    def __str__(self):
        return '%s ' % self.title

    # class Meta:
    #     default_permissions=()