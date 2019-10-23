from .models import Inscrito, Institucion, Programa
from django.http import JsonResponse

def getUsuarios(request):
    users = Inscrito.objects.all()
    data = list(users.values("id","nombre"))
    return JsonResponse(data, safe=False)

def getUsuariosByInstitucion(request, slug):
    entidad = Institucion.objects.get(slug=slug)
    data = list(entidad.get_inscritos.values("id","nombre"))
    return JsonResponse(data, safe=False)

def getUsuarioDetail(request, pk):
    inscrito = Inscrito.objects.filter(id=pk)
    return JsonResponse(list(inscrito.values("id","nombre","programas")),safe=False)
