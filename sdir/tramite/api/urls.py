from django.conf.urls import url
from .views import TramitesApiView, CutsApiView
urlpatterns = [
    url(r'^$', TramitesApiView.as_view()),
    url(r'^estado/(?P<cut>[\w\-]+)?/?$', TramitesApiView.as_view()),
    url(r'^generacut/?$', CutsApiView.as_view())
]