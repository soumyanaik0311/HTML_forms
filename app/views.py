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


def update_webpage(request):
    webpage=Webpage.objects.all()
    # Webpage.objects.filter(name='virat').update(url='https://virat.in')
    # Webpage.objects.filter(topic_name='cricket').update(url='https://India.com')
    # Webpage.objects.filter(name__regex='t$').update(url='https://virat.in')
    # Webpage.objects.filter(name='rohit').update(url='https://rohit.com')
    # Webpage.objects.filter(name='virat').update(topic_name='volleyball')
    # Webpage.objects.filter(name='virat').update(topic_name='hockey')  #foreign key error we cannot change the data which is not present in parent table
    # Webpage.objects.filter(name='soumya').update(url='https://virat.in') #the name soumya is not present in the webpage table so it will not perform any operation.

    # Webpage.objects.update_or_create(name='Messi',defaults={'url':'https://messi.in'})
    # Webpage.objects.update_or_create(topic_name='football',defaults={'url':'https://messi.in'}) #get method error....we cannot update more than 1 value
    # CTO=Topic.objects.get(topic_name='football')
    # Webpage.objects.update_or_create(name='rohit',defaults={'topic_name':CTO})
    # Webpage.objects.update_or_create(name='virat',defaults={'topic_name':CTO})
    # Webpage.objects.update_or_create(name='Soumya',defaults={'topic_name':CTO,'url':'https://soumya.com',})


    d={'webpage':webpage}
    return render(request,'display_webpages.html',d)




def delete_webpage(request):
    Webpage.objects.filter(name='Soumya').delete()
    
    webpage=Webpage.objects.all()
    d={'webpage':webpage}
    return render(request,'display_webpages.html',d)