from django.forms import ModelForm
from sbs.models.Highrecord import Highrecord

class HighRecortForm(ModelForm):
    class Meta:
        model = Highrecord
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(HighRecortForm,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'