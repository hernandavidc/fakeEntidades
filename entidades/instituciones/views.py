from .models import Inscrito
from django.http import JsonResponse

def getUsuarios(request):
    users = Inscrito.objects.all()
    data = list(users.values("id","nombre"))
    return JsonResponse(data, safe=False)

def getUsuarioDetail(request, pk):
    data = Inscrito.objects.filter(id=pk)
    return JsonResponse(list(data.values("id","nombre", "programas")),safe=False)