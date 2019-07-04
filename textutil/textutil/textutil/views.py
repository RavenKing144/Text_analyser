from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return HttpResponse("hello world")

def contactus(request):
    return HttpResponse("hello world")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')


    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'analyzed_text': analyzed}
        djtext = analyzed
       
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'analyzed_text': analyzed}
        djtext = analyzed
        
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        analyzed="please select any operation and try again"
        params={'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)
