from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def users(request):
    if request.method =='POST':
        username = request.POST.get('username')
        id = request.POST.get('id')



    return render(request, 'users.html')