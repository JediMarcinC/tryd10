from django.conf.urls import url


from shortener.views import kirr_redirect_view, KirrCBView
from .views import wildcard_redirect

urlpatterns = [
    url(r'^(?P<path>.*)', wildcard_redirect),
]
