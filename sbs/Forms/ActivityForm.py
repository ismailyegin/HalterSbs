from django import forms
from django.forms import ModelForm

from sbs.models.Activity import  Activity


class ActivityForm(ModelForm):



    class Meta:
        model = Activity

        fields = (
            'name', 'startDate', 'finishDate','compType','compGeneralType','eventPlace','eventDate','registerStartDate','registerFinishDate','type')

        labels = {'name': 'İsim', 'startDate': 'Başlangıç Tarihi', 'finishDate': 'Bitiş Tarihi', 'compType': 'Türü', 'compGeneralType': 'Genel Türü',
                  'eventPlace':'Etkinlik Yeri','eventDate':'Etkinlik tarihi','registerStartDate':'Ön Kayıt Başlangıç Tarihi',
                  'registerFinishDate':'Ön Kayıt Bitiş Tarihi','type':'Faaliyet Türü '}

        widgets = {



            'registerStartDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right datepicker6',  'autocomplete': 'on',
                       'onkeydown': 'return true'}),
            'registerFinishDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right datepicker6', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),
            'eventDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right datepicker6', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),
            'eventPlace': forms.TextInput(attrs={'class': 'form-control'}),

            'startDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker2', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),

            'finishDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'on',
                       'onkeydown': 'return true'}),

            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),

            'compType': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),
            'compGeneralType': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                            'style': 'width: 100%; '}),
            'type': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                   'style': 'width: 100%; '}),



        }
