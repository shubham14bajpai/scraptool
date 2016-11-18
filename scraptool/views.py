from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


def index(request):
    context = {}
    template = 'index.html'
    return render(request, template, context)
        

def result(request):
    context = {}
    active_links = []
    if request.method == 'POST':
        url = request.POST.get('url', '')
        tag = request.POST.get('tag', '')
        print(url)
        print(tag)
        template = 'result.html'
        active_links = spider(url, tag)
        print(active_links)
        context = {'links':active_links, 'url':url}
        return render(request, template, context)   
    else :
        return render(request, 'base.html', {})

def spider(url, tag):
    active_links = []
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")
    for link in soup.findAll(tag):
        if link.text.strip() != "":
            #if str(link.get('href'))[:4] == "http" or str(link.get('href'))[:3] == "www" :
            #   active_links.append((link.get('href'),link.text))
            #elif str(link.get('href') == "#") :
            #   active_links.append((url,link.text))
            #else :
            #   active_links.append((url+str(link.get('href')),link.text))
            active_links.append(link.text);
    return active_links
    