from django import forms
from django.template import Library, Node
from django.contrib.auth.forms import AuthenticationForm    

register = Library()

def parttext(object_text, search_word):
    print '-----------------'
    print search_word
    print '-----------------'

    display_text = ''

    for part in object_text.text.split('.'):
        place_numb = part.lower().find(search_word.lower())
        display_text += part[place_numb-30:place_numb+30]

    return display_text

register.simple_tag(parttext)