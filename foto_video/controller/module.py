import pathlib
import cv2
import threading


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


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')