import cv2 as cv
import time

cv.namedWindow("camera", 1)
capture  = cv.VideoCapture(0)

while True:
    ret, frame = capture.read ()
    "frame = cv.cvtColor (frame,  cv.COLOR_BGR2BGRA) "

    file = "E:\\projects\\c102 capturing images\\"
    cv.imwrite (file, frame)
    cv.imshow("camera", frame)

    
    if cv.waitKey(10) & 0xFF == ord ('q'):
        break
capture.release()
cv.destroyAllWindows ()