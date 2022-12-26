import cv2
import time
import datetime


captura= cv2.VideoCapture("rtsp://localhost:8554/")#transmision del escritorio con vlc
#rtsp://live-edge01.telecentro.net.ar:80/live/26hd-360

while True:
    ret, frame=captura.read()

    cv2.imshow("Captura RTSP desarrolado por Oficina Tecnica COV",frame)
    k=cv2.waitKey(20)&0xff

    if k==27:
        break

captura.release()
cv2.destroyAllWindows()