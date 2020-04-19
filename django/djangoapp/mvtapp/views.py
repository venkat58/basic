from django.shortcuts import render


# Create your views here.
import datetime  
# Create your views here.  
from django.http import HttpResponse, HttpResponseNotFound
def index(request):  
    now = datetime.datetime.now()  
    html = "<html><body><h1> hi venkat {{request.time}}</><h3>Now time is %s.</h3></body></html>" % now  
    return  HttpResponse(html)    # rendering the template in HttpResponse  