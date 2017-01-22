from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL

# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view FBV
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    print('obj.url:', obj.url)
    return HttpResponseRedirect(obj.url)
    # return HttpResponse("<h2>This is {}<h2>".format(obj.url))


class KirrCBView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        print('(CB)obj.url:', obj.url)
        return HttpResponse("<h1 style='color: navy'>hello again {}</h1>".format(obj.url))

    def post(self, request):
        return HttpResponse("<h1 style='color: navy'>hello again {} </h1>".format("post"))

