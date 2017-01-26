from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomeView, KirrCBView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^b/(?P<shortcode>[\w-]{3,15})/$', KirrCBView.as_view(), name='shortcode'),

]
