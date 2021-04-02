from django.http import JsonResponse


def test(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)
