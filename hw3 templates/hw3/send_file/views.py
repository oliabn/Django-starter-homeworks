from django.http import HttpResponse, FileResponse


def send_file(request):
    file = open('send_file/static/files/file_for_sending.txt', 'rb')
    return FileResponse(file, as_attachment=True, status=227)

# def send_file(request):
#     file_location = 'send_file/static/files/file_for_sending.txt'
#
#     with open(file_location, 'rb+') as file:
#         file_data = file.read()
#     return HttpResponse(file_data, status=227)
