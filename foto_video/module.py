import pathlib


def update_request_data_by_file_param(request):
    file = request.FILES['file']
    file_name = pathlib.Path(file.name).stem
    file_size = file.size
    file_type = pathlib.Path(file.name).suffix.replace(".", "")
    request.data.update({
        "name": file_name,
        "size": file_size,
        "type": file_type
    })
