from django.shortcuts import render
from django.views.generic import  TemplateView
from django.http import JsonResponse

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'


class  AddedTaskAPI(TemplateView):
    template_name = 'google.com.html'

def Json(request):
    return JsonResponse({'foo': 'bar'})