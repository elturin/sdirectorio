from django.shortcuts import render
from django.http import HttpResponse
from entidades.models import Entidad
from django.views.generic import TemplateView


def demo_vista_basica(request):
    return HttpResponse('Hola mundo4!!')

def inicio_indicadores(requiest):
    template = 'home.html'
    contex = {
        "titulo" : "Indica",
        "entidades" : Entidad.objects.all()

    }
    return render(requiest,template,contex)


class IndicadorEntidad(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super(IndicadorEntidad,self).get_context_data(**kwargs)
        context.update({
        "titulo" : "Indica",
        "entidades" : Entidad.objects.all()
         })
        return (context)
