from django import forms
from sbs.models.ReferenceReferee import ReferenceReferee
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db import models
from sbs.models.CategoryItem import CategoryItem



class RefereeForm(ModelForm):
    k_definition = forms.ModelChoiceField(queryset=CategoryItem.objects.filter(forWhichClazz='REFEREE_GRADE'),
                                               to_field_name='name',
                                               empty_label="Seçiniz",
                                               label="Kademe",
                                               widget=forms.Select(
                                                   attrs={'class': 'form-control select2 select2-hidden-accessible',
                                                          'style': 'width: 100%; '}))
    class Meta:

        model = ReferenceReferee
        fields = (
            'first_name', 'last_name', 'email', 'is_active', 'phoneNumber', 'address', 'postalCode', 'phoneNumber2',
            'city',
            'country', 'iban', 'tc', 'profileImage', 'height', 'weight', 'birthDate', 'bloodType', 'gender', 'birthplace', 'motherName',
            'fatherName')
        labels = {'iban': 'İban Adresi', 'first_name': 'Ad', 'last_name': 'Soyad', 'email': 'Email',
                  'phoneNumber': 'Cep Telefonu', 'phoneNumber2': 'Sabit Telefon', 'postalCode': 'Posta Kodu',
                  'city': 'İl', 'country': 'Ülke', 'tc': 'T.C.', 'gender': 'Cinsiyet',
                  }
        widgets = {



            'tc': forms.TextInput(attrs={'class': 'form-control ', 'required': 'required'}),

            'height': forms.TextInput(attrs={'class': 'form-control'}),

            'weight': forms.TextInput(attrs={'class': 'form-control'}),

            'birthplace': forms.TextInput(
                attrs={'class': 'form-control ', 'value': '', 'required': 'required'}),

            'motherName': forms.TextInput(
                attrs={'class': 'form-control ', 'value': '', 'required': 'required'}),

            'fatherName': forms.TextInput(
                attrs={'class': 'form-control ', 'value': '', 'required': 'required'}),


            'birthDate': forms.DateInput(
                attrs={'class': 'form-control  pull-right', 'id': 'datepicker', 'autocomplete': 'off',
                       'onkeydown': 'return false', 'required': 'required'}),

            'bloodType': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                             'style': 'width: 100%; '}),

            'gender': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                          'style': 'width: 100%; '}),

            'first_name': forms.TextInput(
                attrs={'class': 'form-control ', 'value': '', 'required': 'required'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control ', 'required': 'required'}),
            'email': forms.TextInput(attrs={'class': 'form-control ', 'required': 'required'}),

            'is_active': forms.CheckboxInput(attrs={'class': 'iCheck-helper'}),
            'address': forms.Textarea(
                attrs={'class': 'form-control ', 'rows': '2'}),

            'phoneNumber': forms.TextInput(attrs={'class': 'form-control '}),

            'iban': forms.TextInput(attrs={'class': 'form-control '}),

            'phoneNumber2': forms.TextInput(attrs={'class': 'form-control '}),

            'postalCode': forms.TextInput(attrs={'class': 'form-control '}),

            'city': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                        'style': 'width: 100%;', 'required': 'required'}),

            'country': forms.Select(attrs={'class': 'form-control select2 select2-hidden-accessible',
                                           'style': 'width: 100%;', 'required': 'required'}),

        }

    def clean_email(self):

        data = self.cleaned_data['email']
        print(self.instance)
        if self.instance.id is None:
            if User.objects.filter(email=data).exists():
                raise forms.ValidationError("Bu email başka bir kullanıcı tarafından kullanılmaktadır.")
            return data
        else:
            return data

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
