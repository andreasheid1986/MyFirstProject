from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'firsttemplate.html')

def more(request):
    return render(request, 'firsttemplate_more.html')

def error_message_app(request):
        return render(request, 'error_message_app.html')