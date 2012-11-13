from capturing.forms import FormSite
from capturing.models import NewSites
from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    context = RequestContext(request)

    if request.method == 'POST':
        if request.user.is_authenticated():
            userid = request.user.id
            form   = FormSite(request.POST)

            if form.is_valid():
                url  = form.cleaned_data['url']
                user = User.objects.get(id=userid)
                site = NewSites(url=url, user=user)
                site.save()

                return HttpResponseRedirect(request.path)
    else:
        form = FormSite()

        return render_to_response('enter_url.html', 
                                  {'form':form},
                                   context_instance=context)

    return render_to_response('enter_url.html', 
                                   context_instance=context)

def search(request):
    context = RequestContext(request)
    
    return render_to_response('search.html', 
                               context_instance=context)

