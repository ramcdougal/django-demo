from .model import Model
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseForbidden

def api_cells(request):
    # need the safe=False because sending back a list instead of a dict
    if request.method == 'POST':
        return JsonResponse(Model.add_cell(**request.POST), safe=False)
    elif request.method == 'GET':
        return JsonResponse(Model.get_cells(), safe=False)
    else:
        return HttpResponseForbidden()

def api_cell(request, cell_id=None):
    cell_data = Model.get_cell(cell_id)
    if cell_data is None:
        return HttpResponseNotFound()
    else:
        return JsonResponse(cell_data)
