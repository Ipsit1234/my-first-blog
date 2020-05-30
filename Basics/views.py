from django.shortcuts import render

def index(request):
    note = {'name':'Divyanshi Kamra'}
    return render(request, 'navigator.html', note)