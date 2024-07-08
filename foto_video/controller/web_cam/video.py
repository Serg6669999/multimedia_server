import os

import cv2
from django.http import StreamingHttpResponse

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
def highlight_face(net, frame, conf_threshold=0.7):
    frame_opencv_dnn = frame.copy()
    frame_height = frame_opencv_dnn.shape[0]
    frame_width = frame_opencv_dnn.shape[1]
    blob = cv2.dnn.blobFromImage(frame_opencv_dnn, 1.0, (300, 300),
                                 [104, 117, 123], True, False)
    net.setInput(blob)
    detections = net.forward()
    face_boxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frame_width)
            y1 = int(detections[0, 0, i, 4] * frame_height)
            x2 = int(detections[0, 0, i, 5] * frame_width)
            y2 = int(detections[0, 0, i, 6] * frame_height)
            face_boxes.append([x1, y1, x2, y2])
            cv2.rectangle(frame_opencv_dnn, (x1, y1), (x2, y2), (0, 255, 0),
                          int(round(frame_height / 150)), 8)
    return frame_opencv_dnn, face_boxes


def get_neuronet():
    face_proto = f"{ROOT_DIR}/web_cam/files/opencv_face_detector.pbtxt"
    face_model = f"{ROOT_DIR}/web_cam/files/opencv_face_detector_uint8.pb"

    face_net = cv2.dnn.readNet(face_model, face_proto)
    return face_net


def gen_display(camera):
    """
         Video flow generator function.
    """
    while True:
        # Read the picture
        has_frame, frame = camera.read()
        if has_frame:
            frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.25)
            # Decoding the picture
            face_net = get_neuronet()
            highlight_face_frame, face_boxes = highlight_face(face_net, frame)
            has_frame, frame = cv2.imencode('.jpeg', highlight_face_frame)
            if has_frame:
                # Converted to Byte type, stored in the iterator
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')


def video(request):
    # Video Stream Camera Object
    camera = cv2.VideoCapture(0)
    # Use passing transmission video stream
    return StreamingHttpResponse(gen_display(camera), content_type='multipart/x-mixed-replace; boundary=frame')
