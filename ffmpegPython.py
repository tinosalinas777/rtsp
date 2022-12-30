import os
import pyfiglet
import threading
import cv2

print("\n\n    ********* Desarrollado por oficina tecnica COV ******")
banner=pyfiglet.figlet_format("   Cliente RTSP ")#titulo del programa
print(banner)



def cam1(x):
    

    os.system("ffplay -hide_banner -loglevel error -max_delay 500000 "+x)
    

def cam2(x):
    
    os.system("ffplay -hide_banner -loglevel error -max_delay 500000 -rtsp_transport udp "+x)


def camaras():
    lista1=open("comandos.txt",mode="r")
    listaComandos=list()
    for i in lista1:
        listaComandos.append(i)
    lista1.close()
    print("\n\n    ********* Desarrollado por oficina tecnica COV ******")
    print(banner)
    print("   selecione camara\n 0- canal 26 \n 1- pasillo \n 2- racks\n")

    x=int(input())

    print("selecione previo")
    z=int(input())
    os.system("cls")
    l=listaComandos[x]
    m=listaComandos[z]

    t1=threading.Thread(target=cam1, args=(l,))
    t2=threading.Thread(target=cam2, args=(m,))
    t1.start()
    t2.start()


def grabaEscritorio():
    os.system("ffmpeg -hide_banner -loglevel error -f gdigrab -i desktop salida.avi")#graba escritorio

def openCVT():
    captura= cv2.VideoCapture("rtmp://200.105.122.11:1935/live/stream")#transmision del escritorio con vlc
    while True:
        ret, frame=captura.read()
        cv2.imshow("Captura RTSP desarrolado por Oficina Tecnica COV",frame)
        k=cv2.waitKey(20)&0xff
        if k==27:
          break
    captura.release()
    cv2.destroyAllWindows()

     
menu=int(input("             ******** Cliente RTSP ********\n \n 1- Seleccionar camaras \n 2- recepcion canal 26 por rtsp \n 3- grabar escritorio\n 4- Salir\n"))
os.system("cls")
while menu !=0:
    if menu ==1:
        camaras()
    elif menu == 2:
        openCVT()
    elif menu == 3:
        grabaEscritorio()
    elif menu ==4:
        exit()
    print("\n\n    ********* Desarrollado por oficina tecnica COV ******")
    print (banner)
    menu=int(input("             ******** Cliente RTSP ********\n \n 1- Seleccionar camaras \n 2- recepcion canal 26 por rtsp \n 3- grabar escritorio\n 4- Salir\n"))
    os.system("cls")


#"rtsp://live-edge01.telecentro.net.ar:80/live/26hd-360"