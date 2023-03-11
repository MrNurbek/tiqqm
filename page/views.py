from django.shortcuts import render
from page.models import *
import datetime

date = datetime.date.today()
start_week = date - datetime.timedelta(date.weekday())
end_week = start_week + datetime.timedelta(7)


# Create your views here.
def my_view(request):
    context = {
        "dgu": DGU.objects.all(),
        "bgu": BGU.objects.all(),
        "patent": Patent.objects.all(),
        "mualliflikhuquqi": MualliflikHuquqi.objects.all(),
        "news": News.objects.all(),
        "user": request.user,
        "data": datetime.date.today(),
        "start_week": date - datetime.timedelta(date.weekday()),
        "end_week": start_week + datetime.timedelta(7),

    }
    return render(request, 'index.html', context=context)


def naw_view(request):
    context = {

        "data": datetime.date.today(),

    }
    return render(request, 'navbar.html', context=context)


def newsView(request, id):
    dict = {
        "news": News.objects.get(id=id),
    }
    return render(request, 'news.html', context=dict)


def patentView(request):
    dict = {
        "patent": Patent.objects.all(),
    }
    return render(request, 'patent.html', context=dict)


def dguView(request):
    dict = {
        "dgu": DGU.objects.all(),

    }
    return render(request, 'axborot.html', context=dict)


def bguView(request):
    dict = {

        "bgu": BGU.objects.all(),
    }
    return render(request, 'bgu.html', context=dict)


def mualliflikhuquqiView(request):
    dict = {

        "mualliflikhuquqi": MualliflikHuquqi.objects.all(),
    }
    return render(request, 'mualliflikhuquqi.html', context=dict)
