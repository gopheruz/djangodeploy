from django.urls import  path

from .views import HomePageView, AboutPageView, AddedTaskAPI, Json

urlpatterns = [
    path('json/', Json, name='json'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('task/', AddedTaskAPI.as_view(), name='task'),
    path('', HomePageView.as_view(),name= 'home'),

]
