from django.shortcuts import render
from django.http import HttpResponse
from dp27app.models import *

#whats new:here we are displaying the databse data to the user by using front end and views.
def createtopic(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=Topic.objects.get_or_create(topic_name=topic)
        if t[1]==True:
            t[0].save()
            return HttpResponse("<h2>topic added successfully</h2>")
        else:
            return HttpResponse("<h2>Topic is already exist in the table</h2>")
    return render(request,"createtopic.html")

def createwebpage(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        name=request.POST.get("name")
        url=request.POST.get("url")
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        w=WebPage.objects.get_or_create(topic=t,name=name,url=url)[0]
        w.save()
        return HttpResponse("<h1>Webpage added successfully</h1>")
    topics=Topic.objects.all()
    return render(request,"createwebpage.html",context={'topics':topics})
        