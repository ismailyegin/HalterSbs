from django import forms
from django.forms import ModelForm
from sbs.models.Highrecord import Highrecord

class HighRecortSearchForm(ModelForm):

    class Meta:
        model = Highrecord

        fields = (
             'eventdate','sportyear', 'eventplace', 'name','recordtype','agecategory','competition','weight','recordwhich')

        labels = { 'eventdate': 'Rekor Tarihi', 'name': 'Sporcu İsim ','eventplace':'Rekor Yeri',
                  'record': 'Rekor ', 'recordtype': 'Rekor Türü ','agecategory':' Yaş Kategori','weight':'Sıklet','recordwhich':'Kaldırış Türü','sportyear':'Sporcunun Dogum Yılı '}

        widgets = {
            'weight': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),
            'competition': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),
            'agecategory': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                               'style': 'width: 100%; '}),
            'eventdate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker4', 'autocomplete': 'off',
                       'onkeydown': 'return false',}),

            'sportyear': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker5', 'autocomplete': 'off',
                       'onkeydown': 'return false', }),
            'eventplace': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),

            'recordwhich': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                               'style': 'width: 100%; '}),

        }
    def __init__(self, *args, **kwargs):
        super(HighRecortSearchForm,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
