from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from .models import *


def index (request):
    return render(request,"index.html")

def index2 (request):
    return render(request,"index2.html")

def lifeinsurancepage(request):
    return render(request,"lifeinsurance.html")

def longtermcareplanningpage(request):
    return render(request,"longtermcareplanning.html")

def retirementpage(request):
    return render(request,"retirement.html")

def estateplanningpage(request):
    return render(request,"estateplanning.html")

def wealthmanagementpage(request):
    return render(request,"wealthmanagement.html")

def collegeplanningpage(request):
    return render(request,"collegeplanning.html")