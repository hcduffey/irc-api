from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import connection
import irc.client

# Create your views here.

@csrf_exempt
def connection_list(request):

    if request.method == 'GET':
        return JsonResponse([{'name': 'testConnection'}], safe=False)

    if request.method == 'POST':
        new_connection = connection.Connection("#test84747")
        try:
            new_connection.connect("irc.undernet.org", 6667, "isthisworking123")
        except irc.client.ServerConnectionError as err:
            return JsonResponse({'error': err}, safe=False)

        new_connection.start()

