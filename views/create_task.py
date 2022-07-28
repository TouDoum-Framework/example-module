from django.http import JsonResponse, HttpRequest
# this create a task to mq can be received by the client
def create_task(request: HttpRequest):
    from client.core.tasks import client_exec
    client_exec.delay("example")
    return JsonResponse({}, status=200)