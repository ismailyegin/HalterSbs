from django import forms
from django.forms import ModelForm
from sbs.models.Claim import Claim
class ClaimAdminForm(ModelForm):
    class Meta:
        model = Claim
        fields = (
             'title', 'project','definition','importanceSort','status')
        labels = {
                   'title': 'Başlık ',
                   'status': 'Onay Durumu  ',
                   'definition': 'Açıklama ',
                   'importanceSort':'Önem Durumu',
                   'project':'Proje Seçiniz',
        }
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                  'style': 'width: 100%; '}),
            'importanceSort': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),
            'project': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'definition':  forms.Textarea(
                attrs={'class': 'form-control ', 'rows': '4'}),
        }
