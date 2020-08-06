from django.conf.urls import url
from .views import IndicadorEntidad
urlpatterns = [
    url(r'^ent/(?P<codigo>[1-9]+)?/?$', IndicadorEntidad.as_view())
]