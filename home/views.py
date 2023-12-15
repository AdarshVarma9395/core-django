from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    peoples = [
        {'name':'adarsh varma','age':24},
        {'name':'nitin sirsath','age':23},
        {'name':'sunny','age':26},
        {'name':'snadesh','age':17},
    ]

    vegetables = ['tomato', 'potato', 'pumpkin']


    return render(request , "index.html" , context = {'peoples' : peoples ,'vegetables' : vegetables })


def about(request):
    return render(request , "about.html" )


def contact(request):
    return render(request , "contact.html")



