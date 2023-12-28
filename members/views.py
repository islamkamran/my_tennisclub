from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request):
    # template = loader.get_template('myFirst.html')
    # return HttpResponse(template.render())

    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context,request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    mymembers = Member.objects.all().values()
    mydata = Member.objects.all().order_by('-firstname', 'joining_date').values()
    template = loader.get_template('template.html')
    context = {
        'mydata': mydata,
        'mymembers': mymembers,
        'greetings':1,
        'day':'friday',
        'daya':'asa',
        'fruits': ['Apple', 'Banana', 'Cherry'], 
        'y': ['Apple', 'Banana', 'Cherry'],
    }
    return HttpResponse(template.render(context, request))



