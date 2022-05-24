import cv2
from cv2 import VideoWriter, VideoWriter_fourcc
from datetime import datetime
import time
import threading
from uuid import uuid4

def make_video(temp_array):
    video = VideoWriter('activities/' + datetime.now().strftime("%Y-%m-%d-%I-%M") + str(uuid4()) + '.avi', VideoWriter_fourcc(*'MJPG'), 24, (1280, 720))

    for frame in temp_array:
        video.write(frame)
    
    video.release()

cam = cv2.VideoCapture(1)
first_frame = None

temp = []

while cam.isOpened():
    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue
    
    delta_frame = cv2.absdiff(first_frame, gray)
    threshold = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold, None, iterations=2)

    cntrs, _ = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cntrs:
        if cv2.contourArea(c) < 1000:
            continue
        else:
            flag = True
            (x, y, w, h) = cv2.boundingRect(c)
            #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            temp.append(frame)
    
    if len(temp) > 300:
        make_video(temp)
        temp = []
            
    cv2.imshow('Cam Footage', frame)

    first_frame = None
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
