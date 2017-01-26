from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitURLForm
from .models import KirrURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitURLForm()
        print('rget:', request.GET)
        context = {'form': form,
                   'title': 'Home form',
            }
        return render(request, 'shortener/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        context = {'form': form,
                   'title': 'Home form',
                   }
        template = 'shortener/home.html'
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {'object': obj,
                       'created': created,
                       }
            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/already_exists.html'

        return render(request, template, context)



class KirrCBView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        print('obj.url:', obj.url)
        return HttpResponseRedirect(obj.url)
        # return HttpResponse("<h1 style='color: navy'>hello again {}</h1>".format(obj.url))

    def post(self, request):
        return HttpResponse("<h1 style='color: navy'>hello again {} </h1>".format("post"))

