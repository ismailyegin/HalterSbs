# Generated by Django 2.2.6 on 2020-05-12 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('sbs', '0002_referencereferee'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencereferee',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='referencereferee',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='referencereferee',
            name='is_active',
            field=models.BooleanField(default=False,
                                      help_text='Designates whether this user should be treated as active. '),
        ),
        migrations.AddField(
            model_name='referencereferee',
            name='is_staff',
            field=models.BooleanField(default=False,
                                      help_text='Designates whether the user can log into this admin site.'),
        ),
        migrations.AddField(
            model_name='referencereferee',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='referencereferee',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbs.City', verbose_name='İl'),
        ),
        migrations.AlterField(
            model_name='referencereferee',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbs.Country', verbose_name='Ülke'),
        ),
    ]
