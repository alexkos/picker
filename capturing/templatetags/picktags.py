from django import forms
from django.template import Library, Node
from django.contrib.auth.forms import AuthenticationForm    

register = Library()

def parttext(object_text, search_word):
    display_text = ''

    for part in object_text.text.split('.'):
        place_numb  = part.lower().find(search_word.lower())
        len_word    = len(search_word)

        if place_numb==0:
            display_text += '<strong>' + part[place_numb:len_word] + '</strong> ' + \
                            part[len_word:len_word+30]
        else:
            display_text += part[place_numb-30:place_numb] + ' <strong>'+part[place_numb:place_numb+len_word] + '</strong> ' + part[place_numb+len_word:place_numb+len_word+30]
            # display_text += part[place_numb-30:place_numb+30]

    return display_text

register.simple_tag(parttext)