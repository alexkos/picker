import os, re
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from picker.settings import LOGIN_REDIRECT_URL
from capturing.models import NewSites, TextSite
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from capturing.forms import FormSite, FormDom, FormSearchText

def main_page(request):
    context = RequestContext(request)

    return render_to_response('main_page.html', 
                               context_instance=context)

@login_required
def capture(request):
    context = RequestContext(request)

    if request.method == 'POST':
        userid = request.user.id
        form   = FormSite(request.POST)

        if form.is_valid():
            url     = form.cleaned_data['url']
            pattern = re.compile('\w+://([-\w+.]*)/')
            match   = pattern.match(url)
            domain  = match.group(1)

            user    = User.objects.get(id=userid)
            newsite = NewSites.objects.create_site(url, user)

            path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'../sitecrawler')
            os.popen('cd %s && scrapy crawl pick -a urls=%s -a address_domains=%s -a userid=%s' 
                % (path, url, domain, userid))
        return HttpResponseRedirect(reverse(capture)) 
    else:
        form = FormSite(auto_id=False)

    return render_to_response('enter_url.html', 
                              {'form_site':form},
                               context_instance=context)

@login_required
def display_links(request):
    context = RequestContext(request)
    
    if request.method == 'GET':
        userid = request.user.id
        form   = FormDom(userid, auto_id=False)

        siteid = request.GET.get('domen','')

        if not siteid:
            data = ''
        else:
            data = NewSites.objects.get(id=siteid)

    return render_to_response('display_links.html', 
                              {'form_links' : form,
                               'links'      : data,},
                               context_instance=context)

@login_required
def search(request):
    context = RequestContext(request)

    if request.method == 'GET':
        userid = request.user.id
        form   = FormSearchText(userid, auto_id=False)
        match  = ''

        if request.GET:
            siteid = request.GET.get('site','')
            search = request.GET.get('text','')
            form   = FormSearchText(userid, search, auto_id=False)
            data   = NewSites.objects.get(id=siteid)

            pages  = data.textsite_set.extra(where=['text_tsv @@ plainto_tsquery(%s)'],
                                             params=[search])

            if not pages:
                match  = 'Don\'t find of match'
        else:
            pages  = []
            search = ''

    return render_to_response('search.html', 
                              {'form_search': form,
                               'pages'      : pages,
                               'search_word': search,
                               'match'      : match},
                               context_instance=context)