from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def htmlforms(request):

    if request.method == 'POST':
        return HttpResponse(request.POST['em'])
    return render(request,'htmlforms.html')

def insert_topic(request):
    if request.method == 'POST':
        topic=request.POST['topic']
        TO=Topic.objects.get_or_create(topic_name=topic)[0]
        TO.save()
        return HttpResponse('topic is created')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    
    if request.method=='POST':
        tn=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']

        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()
        return HttpResponse('Webpage is created')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    LNO=Webpage.objects.all()
    d={'LNO':LNO}

    if request.method=='POST':
        
        nm=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']

        NO=Webpage.objects.get(name=nm)
        AO=AccessRecord.objects.get_or_create(name=NO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('Access Record is created')
    return render(request,'insert_access.html',d)


def select_topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        topic=request.POST.getlist('topic')
        webpage=Webpage.objects.none()
        for tn in topic:
            webpage=webpage|Webpage.objects.filter(topic_name=tn)
        d1={'webpage':webpage}
        return render(request,'display_webpages.html',d1)
    return render(request,'select_topic.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    return render(request,'checkbox.html',d)

