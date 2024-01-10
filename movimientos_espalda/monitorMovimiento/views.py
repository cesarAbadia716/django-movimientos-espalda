# monitoreo_espalda/views.py
import socket
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DatosEspalda

@csrf_exempt
def socket_client(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))

        # Conectar al servidor Flask (ajusta la dirección y puerto según tu configuración)
        server_address = ('localhost', 8000)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)

        # Enviar datos al servidor Flask
        sock.sendall(json.dumps(data).encode('utf-8'))

        # Recibir la respuesta del servidor Flask
        response_data = sock.recv(1024).decode('utf-8')

        # Cerrar la conexión con el servidor Flask
        sock.close()

        # Procesar la respuesta y devolverla
        response = json.loads(response_data)
        return JsonResponse({'output': response['output']})

    return JsonResponse({'error': 'Invalid request method'})
