from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

height, width = GetSystemMetrics(0), GetSystemMetrics(1)

file_name = f'test.mp4'
fourc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
capture_video = cv2.VideoWriter(file_name, fourc, 10, (1920, 1080))

while True:
    img = ImageGrab.grab(bbox=None)
    audio_frame, val = player.get_frame()
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Recorder', img_final)
    capture_video.write(img_final)

    if cv2.waitKey(10) == ord('q'):
        cv2.destroyAllWindows()
        break