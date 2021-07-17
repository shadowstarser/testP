from django.contrib import admin
from django.urls import path , include
from tsevent.views import tseventCreateView , tseventListView

app_name = 'tsevent'
urlpatterns = [
    path('tsevent/create/', tseventCreateView.as_view()),
    path('List/all/', tseventListView.as_view()),
]
