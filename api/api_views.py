from django.http import JsonResponse 

def files_view(request):
    message = {"files" : []}
    return JsonResponse(message)

def file_upload(request):
    message = {"uploaded" : True}
    return JsonResponse(message)

def file_view(request, id):
    message = {"file" : "file", "id" : id}
    return JsonResponse(message)

def file_version_upload(request, id):
    message = {"new_version" : True}
    return JsonResponse(message)

def file_versions_view(request, id):
    message = {"file_versions" : [1, 2, 3], "id": id}
    return JsonResponse(message)

def file_share(request, id):
    message = {"shared" : True, "id": id}
    return JsonResponse(message)

def file_restore(request, id):
    message = {"restore": True, "id": id}
    return JsonResponse(message)