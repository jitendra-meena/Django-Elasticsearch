from django.urls import path
from .views import *

urlpatterns = [
    path('' , home,name="home"),
    path('search/' , PublisherDocumentView.as_view({'get': 'list'})),
]
