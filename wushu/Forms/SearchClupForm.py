from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from wushu.models.CategoryItem import CategoryItem
from wushu.models.SportsClub import SportsClub

class SearchClupForm(ModelForm):
    sportsClub = forms.ModelChoiceField(queryset=SportsClub.objects.all(),
                                        to_field_name='name',
                                        empty_label="Seçiniz",
                                        label="Kulübü",
                                        required=False,
                                        widget=forms.Select(
                                            attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                   'style': 'width: 100%; '}))

    class Meta:
        model =CategoryItem

        fields = (
            'sportsClub', 'branch')

        labels = { 'branch': 'Branş', 'sportsClub': 'Kulüp'}

        widgets = {



            'branch': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%;'}),
            'sportsClub': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%;'}),

        }
