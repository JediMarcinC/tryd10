
from django.conf.urls import url
from django.contrib import admin

from shortener.views import kirr_redirect_view, KirrCBView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<shortcode>[\w-]{3,15})/$', kirr_redirect_view),
    url(r'^b/(?P<shortcode>[\w-]{3,15})/$', KirrCBView.as_view()),

]
