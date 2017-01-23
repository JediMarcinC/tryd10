from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitURLForm
from .models import KirrURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitURLForm()
        print('rget:', request.GET)
        return render(request, 'shortener/home.html', {})

    def post(self, request, *args, **kwargs):
        # print('rpost:', request.POST)
        # print('request.POST.get("url"):', request.POST.get('url'))
        # print('request.POST["url"]:', request.POST["url"])
        form = SubmitURLForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        return render(request, 'shortener/home.html', {})



class KirrCBView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        print('obj.url:', obj.url)
        return HttpResponseRedirect(obj.url)
        # return HttpResponse("<h1 style='color: navy'>hello again {}</h1>".format(obj.url))

    def post(self, request):
        return HttpResponse("<h1 style='color: navy'>hello again {} </h1>".format("post"))

