import cv2
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt


def Canny_Edge(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny_edge_frame = cv2.Canny(gray_frame, threshold1=50, threshold2=100, apertureSize=3, L2gradient=True)
    return canny_edge_frame
    

video = cv2.VideoCapture(1)

run = True
while run:
    ret, frame = video.read()

    cv2.imshow("Canny Edge", Canny_Edge(frame))
    cv2.imshow("Normal Color", frame)

    key = cv2.waitKey(1)

    # SPACE is 32 in ASCII
    if key == 32:
        break

video.release()
cv2.destroyAllWindows()




