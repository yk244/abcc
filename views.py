from django.shortcuts import render
from django.http import  HttpResponse,Http404
from  .models import act

# Create your views here.
def act_detail(requst):

        return render(requst,"act_detail.html")


