# views.py
from django.shortcuts import render, HttpResponse, redirect
def index(request):

    return render(request, "hackathon_app/index.html")

def result_process(request):

    return redirect('/results')

def results(request):
    
    return render(request, "hackathon_app/results.html")


