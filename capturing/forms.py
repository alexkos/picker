from django import forms
from django.forms import ModelForm
from capturing.models import NewSites
from django.contrib.auth.models import User


class FormSite(forms.Form):
    url = forms.CharField(max_length=50)

class FormDom(forms.Form):
    def __init__(self,userid,*args,**kwargs):
        super (FormDom,self ).__init__(*args,**kwargs)

        sites   = NewSites.objects.filter(user=1).values_list('url',flat=True)
        choices = zip(sites, sites)
        self.fields['domen'].choices = choices

    domen = forms.ChoiceField()
