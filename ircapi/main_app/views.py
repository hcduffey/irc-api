from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def connection_list(request):

    if request.method == 'GET':
        return JsonResponse([{'name': 'testConnection'}], safe=False)
