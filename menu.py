import os
import pyfiglet  #libreria para el banner, instalar con pip
import cv2       #captura de video, hay que instalar con pip
import threading #hilos de proceso
#from colorama import init,Fore,Back,Style


print("\n\n    ********* Desarrollado por oficina tecnica COV ******")
banner=pyfiglet.figlet_format("   Cliente RTSP ")#titulo del programa
def listasCam():
    #init()
    print("seleccione 2 camaras")
    print("1- conreso..\n 2- tribunales..\n 3- casa gobierno.. \n")
    x="rtsp://live-edge01.telecentro.net.ar:80/live/26hd-360"
    z="rtsp://live-edge01.telecentro.net.ar:80/live/26hd-360"
    hilo1= threading.Thread(target=reproductor2,args=(x,z))#se creael hilo con su funcion y argumentos
    hilo1.start()
    

def reproductor2(n,l):
    captura=cv2.VideoCapture(l)#se crean 2objetos de video
    captura2= cv2.VideoCapture(n)
    while True:
        ret , frame=captura2.read()
        ret , frame2=captura.read()#se guarda en la variable el video capturado
        cv2.imshow("cam1",frame)
        cv2.imshow("cam2",frame2)#se crean las 2 ventanas con los frames capturados
        k=cv2.waitKey(20)&0xff
        if k==27:
            break
    captura2.release()
    captura.release()
    cv2.destroyAllWindows()






def test():
    print("conectando a canal 26")
    captura= cv2.VideoCapture("rtsp://live-edge01.telecentro.net.ar:80/live/26hd-360")#
    while True:
        ret, frame=captura.read()
        cv2.imshow("Captura RTSP desarrolado por Oficina Tecnica COV",frame)
        k=cv2.waitKey(20)&0xff
        if k==27:
            break
    captura.release()
    cv2.destroyAllWindows()


    
    
def finalizar():
    exit()
print (banner)
menu=int(input("             ******** Cliente RTSP ********\n \n 1- Seleccionar camaras \n 2- recepcion canal 26 por rtsp \n 3- Salir\n"))
os.system("cls")
while menu !=0:
    if menu ==1 :
        listasCam()
    elif menu ==2:
        test()
    elif menu==3:
        finalizar()
    print (banner)
    menu=int(input("             ******** Cliente RTSP ********\n \n 1- Seleccionar camaras \n 2- recepcion canal 26 por rtsp \n 3- Salir\n"))
    os.system("cls")





