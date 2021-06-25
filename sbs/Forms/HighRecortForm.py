from django import forms
from django.forms import ModelForm
from sbs.models.Highrecord import Highrecord

class HighRecortForm(ModelForm):

    class Meta:
        model = Highrecord

        fields = (
             'eventdate', 'eventplace', 'name','record','recordtype','agecategory','competition','weight')

        labels = { 'eventdate': 'Rekor Tarihi', 'name': 'İsim Soy İsim ',
                  'record': 'Rekor ', 'recordtype': 'Rekor Türü ','agecategory':'Kategori','weight':'Siklet'}

        widgets = {
            'weight': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),
            'competition': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),
            'agecategory': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                               'style': 'width: 100%; '}),
            'eventdate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'required': 'required'}),
            'eventplace': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),

        }
    def __init__(self, *args, **kwargs):
        super(HighRecortForm,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
