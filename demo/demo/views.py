from .model import Model
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseForbidden
from django.shortcuts import render

def api_cells(request):
    if request.method == 'POST':
        # returns the id of the newly added cell which is described by whatever
        # post arguments were passed
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

def index(request):
    all_cells = Model.get_cells()
    return render(request, 'demo/index.html', {"cells": all_cells, "num_cells": len(all_cells)})

def cell(request, cell_id=None):
    cell_data = Model.get_cell(cell_id)
    if cell_data is None:
        return HttpResponseNotFound()
    else:
        return render(request, 'demo/cell.html', {'cell': cell_data})
