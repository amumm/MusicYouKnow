from django.shortcuts import render
from crawler import crawl
from django.http import HttpResponse
from django.template import Context, loader
from random import randint
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def music(request):
    template = loader.get_template("musicYouKnow.html")
    #string -main()
    context  = {

    }
    return HttpResponse(template.render(context,request))

@csrf_exempt
def music3(request, year):
    template = loader.get_template("musicYouKnow2.html")
    embed = crawl(str(int(year)+ randint(12,18)))
    #embed = crawl(2014)
    context  = {'embed': embed,'year': year}
    return HttpResponse(template.render(context,request))
