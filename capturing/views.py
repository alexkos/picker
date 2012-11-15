import os
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from capturing.forms import FormSite, FormDom
from capturing.models import NewSites, TextSite
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    context = RequestContext(request)

    if request.method == 'POST':
        if request.user.is_authenticated():
            userid = request.user.id
            form   = FormSite(request.POST)

            if form.is_valid():
                url    = form.cleaned_data['url']
                domain = url.split('/')[2]
                user   = User.objects.get(id=userid)
                site   = NewSites(url=url, user=user)
                site.save()

                path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'../sitecrawler')
                os.popen('cd %s && scrapy crawl dmoz -a urls=%s -a address_domains=%s' 
                    % (path, url, domain))

                return HttpResponseRedirect(reverse(index)) #reverse
    else:
        form = FormSite()

        return render_to_response('enter_url.html', 
                                  {'form':form},
                                   context_instance=context)

def display_links(request):
    context = RequestContext(request)
    
    if request.method == 'GET':
        if request.user.is_authenticated():
            userid = request.user.id
            form   = FormDom(userid)
            if request.GET:
                siteid = request.GET['domen']
                data   = NewSites.objects.get(id=siteid)

                return render_to_response('display_links.html', 
                                          {'form_links':form,
                                           'site':data,},
                                           context_instance=context)
        return render_to_response('display_links.html', 
                                  {'form_links':form},
                                   context_instance=context)

def search(request):
    context = RequestContext(request)
    
    return render_to_response('search.html', 
                               context_instance=context)

