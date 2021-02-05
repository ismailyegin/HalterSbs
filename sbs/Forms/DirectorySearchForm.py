from django.forms import ModelForm
from django import forms

from sbs.models.DirectoryMember import DirectoryMember


class DirectorySearchForm(ModelForm):
    class Meta:
        model = DirectoryMember
        fields = (
            'role', 'commission')
        labels = {'role': 'Üye Rolü', 'commission': 'Kurulu'}
        widgets = {

            'role': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%;'}),

            'commission': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;'}),

        }

    def __init__(self, *args, **kwargs):
        super(DirectorySearchForm, self).__init__(*args, **kwargs)
        self.fields['role'].required = False
        self.fields['commission'].required = False

