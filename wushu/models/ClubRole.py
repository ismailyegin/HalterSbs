from django.db import models


class ClubRole(models.Model):
    name = models.TextField(blank=True, null=True, verbose_name='Kulüp Üye Rolü')

    def __str__(self):
        return '%s ' % self.name




    class Meta:
        default_permissions = ()
