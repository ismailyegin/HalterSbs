# Generated by Django 2.2.6 on 2020-03-27 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wushu', '0016_remove_preregistration_communication'),
    ]

    operations = [
        migrations.AddField(
            model_name='preregistration',
            name='status',
            field=models.CharField(choices=[('Onaylandı', 'Onaylandı'), ('Onaya Gönderildi', 'Onaya Gönderildi'), ('Reddedildi', 'Reddedildi'), ('Beklemede', 'Beklemede')], default='Beklemede', max_length=128, verbose_name='Onay Durumu'),
        ),
    ]
