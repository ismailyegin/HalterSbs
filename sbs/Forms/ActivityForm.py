from django import forms
from django.forms import ModelForm

from sbs.models.Activity import  Activity


class ActivityForm(ModelForm):



    class Meta:
        model = Activity

        fields = (
            'name', 'startDate', 'finishDate', 'eventPlace', 'type', 'year')

        labels = {'name': 'Tanımı', 'startDate': 'Başlangıç Tarihi', 'finishDate': 'Bitiş Tarihi',
                  'eventPlace': 'Etkinlik Yeri', 'type': 'Faaliyet Türü ', 'year': 'Yılı ', }

        widgets = {

            'year': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker5', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),

            'eventPlace': forms.TextInput(attrs={'class': 'form-control'}),

            'startDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker2', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),

            'finishDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),

            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),

            'type': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                   'style': 'width: 100%; '}),



        }
