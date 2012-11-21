from django import forms
from django.forms import ModelForm
from capturing.models import NewSites
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

class FormSite(forms.Form):
    url = forms.URLField(max_length=100, 
                         widget=forms.TextInput(attrs={'placeholder': 'Enter url',
                                                       }))
    def clean_url(self):
        url      = self.cleaned_data['url']
        url_splt = url.split('/')

        if len(url_splt) <= 4:
            return self.cleaned_data['url']
        else:
            raise forms.ValidationError(_('Only main domen'))


class FormDom(forms.Form):
    def __init__(self,userid,*args,**kwargs):
        super (FormDom,self ).__init__(*args,**kwargs)

        sites    = NewSites.objects.filter(user=userid).values_list('url',flat=True)
        siteid   = NewSites.objects.filter(user=userid).values_list('id',flat=True)
        choices  = zip(siteid, sites)
        self.fields['domen'].choices = choices

    domen = forms.ChoiceField()

class FormSearchText(forms.Form):
    def __init__(self,userid, word='',*args,**kwargs):
        super (FormSearchText,self ).__init__(*args,**kwargs)

        sites    = NewSites.objects.filter(user=userid).values_list('url',flat=True)
        siteid   = NewSites.objects.filter(user=userid).values_list('id',flat=True)
        choices  = zip(siteid, sites)
        self.fields['domen'].choices = choices
        self.fields['text'].widget.attrs['value'] = word

    domen = forms.ChoiceField()
    text  = forms.CharField(max_length=100, 
                         widget=forms.TextInput(attrs={'placeholder': 'Enter word',
                                                       }))
