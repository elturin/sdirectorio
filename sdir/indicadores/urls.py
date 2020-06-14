from django.conf.urls import url
from .views import IndicadorEntidad
urlpatterns = [
    url(r'^ent/$', IndicadorEntidad.as_view())
]