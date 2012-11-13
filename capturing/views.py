from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)

    return render_to_response('enter_url.html', 
                               context_instance=context)

def search(request):
    context = RequestContext(request)
    
    return render_to_response('search.html', 
                               context_instance=context)

