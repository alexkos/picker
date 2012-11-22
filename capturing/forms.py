import re
from django import forms
from django.forms import ModelForm
from capturing.models import NewSites
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _

def get_tuple_url(userid):
    sites    = NewSites.objects.filter(user=userid).values_list('url',flat=True)
    siteid   = NewSites.objects.filter(user=userid).values_list('id',flat=True)
    choices  = zip(siteid, sites)

    return choices

class FormSite(forms.Form):
    url = forms.URLField(max_length=100, 
                         widget=forms.TextInput(attrs={'placeholder': 'Enter url',
                                                       }))
    def clean_url(self):
        url         = self.cleaned_data['url']
        pattern_url = re.compile('\w+://[-\w+.]*/')
        match_url   = pattern_url.match(url)
        url_right   = match_url.group(0)

        return url_right

class FormDom(forms.Form):
    def __init__(self,userid,*args,**kwargs):
        super (FormDom,self ).__init__(*args,**kwargs)

        self.fields['domen'].choices = get_tuple_url(userid)

    domen = forms.ChoiceField()

class FormSearchText(forms.Form):
    def __init__(self,userid, word='',*args,**kwargs):
        super (FormSearchText,self ).__init__(*args,**kwargs)

        self.fields['site'].choices = get_tuple_url(userid)
        self.fields['text'].widget.attrs['value'] = word

    site = forms.ChoiceField()
    text  = forms.CharField(max_length=30, 
                         widget=forms.TextInput(attrs={'placeholder': 'Enter word',
                                                       }))
