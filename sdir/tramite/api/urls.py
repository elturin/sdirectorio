from django.conf.urls import url
from .views import TramitesApiView, CutsApiView, EntidadesApiView, TramiteUnicoApiView
urlpatterns = [
    url(r'^$', TramitesApiView.as_view()),
    url(r'^estado/(?P<cut>[\w\-]+)?/?$', TramitesApiView.as_view()),
    url(r'^generacut/?$', CutsApiView.as_view()),
    url(r'^listamuni/?$', EntidadesApiView.as_view()),
    url(r'^listatramite/?$', TramiteUnicoApiView.as_view())

]