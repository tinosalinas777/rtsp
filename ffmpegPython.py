import os
import threading
import time
import sys


promp="\033[1;32m"+"cov>>>"+"\033[0;m"



def cam1(x):
    

    os.system("ffplay -hide_banner -loglevel quiet -vf scale=1280:720 -i "+x)#para obs usar -vf scale=1280:720 escala exacta para captura obs
    
def camaras():
    lista1=open("comandos.txt",mode="r")
    lista2=open("nombres.txt",mode="r")
    listaNombres=list()
    for i in lista2:
        listaNombres.append(i)
    listaComandos=list()
    for i in lista1:
        listaComandos.append(i)
    lista1.close()
    time.sleep(1)
    print("\033[1;32m"+"\n\n                    ********* Desarrollado por oficina tecnica COV ******"+"\033[0;m\n\n")
    intro()
    print("\033[1;32m"+"\n\n                              selecione una camara\n "+"\033[0;m")

    for i in listaNombres:
        print(i)
    try:
        x=int(input(promp))
        if x ==99:
            os.system("cls")
            return

       
        os.system("cls")
        l=listaComandos[x]
    

        t1=threading.Thread(target=cam1, args=(l,))
        
        t1.start()
        
        
        
    except ValueError:
        print("\033[4;31m"+"la entrada debe ser un numero"+"\033[0;m")
        time.sleep(2)
        os.system("cls")
        
def emitirEscritorio(d,p):
    
    os.system("ffmpeg -hide_banner -loglevel quiet -f gdigrab -i desktop  -f rtsp -rtsp_transport udp rtsp://"+d+":"+p+"/miEscritorio")#transmite escritorio ffmpeg -f gdigrab -i desktop  -f rtsp -rtsp_transport udp rtsp://localhost:554/miEscritorio
    
def server():
    os.system("rtsp-simple-server.exe")

def openCVT():
  h1=threading.Thread(target=server)
  h1.start()
  
def hiloEscritorio():
    print("\033[1;32m"+"ingrese direccion del servidor rtsp"+"\033[0;m\n\n")
    d=input()
    print("\033[1;32m"+"ingrese puerto de escucha del servidor rtsp"+"\033[0;m\n\n")
    p=input()
    hilo1=threading.Thread(target=emitirEscritorio,args=(d,p))
    hilo1.start()
    time.sleep(1)
    os.system("cls")

def main():
    
    print("\033[1;32m"+"\n\n    ********* Desarrollado por oficina tecnica COV ******"+"\033[0;m\n\n")
    intro()
    print("             ******** Cliente RTSP ********\n \n 1- Seleccionar camaras \n 2- Iniciar servidor rtsp \n 3- Emitir escritorio\n 4- Salir\n")     

    menu=int(input(promp))
    os.system("cls")
    while True:
        
        try:
          if menu ==1:
                camaras()
          elif menu == 2:
                openCVT()
          elif menu == 3:
                hiloEscritorio()
          elif menu ==4:
                sys.exit()
          print("\033[1;32m"+"\n\n                    ********* Desarrollado por oficina tecnica COV ******"+"\033[0;m\n\n")
          intro()
          menu=int(input("\033[1;32m\n"+"                                ******** Herramientas RTSP ********\n \n "+"\033[0;m"+"1- Seleccionar camaras \n 2- Iniciar servidor rtsp \n 3- Emitir escritorio\n 4- Salir\n\n"+promp))
          os.system("cls")
        except ValueError:
            print("\033[4;31m"+"la entrada debe ser un numero"+"\033[0;m")
            time.sleep(2)
            os.system("cls")

def intro():
    print(" ██████╗██╗     ██╗███████╗███╗   ██╗████████╗███████╗    ██████╗ ████████╗███████╗██████╗ ")
    print("██╔════╝██║     ██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝    ██╔══██╗╚══██╔══╝██╔════╝██╔══██╗")
    print("██║     ██║     ██║█████╗  ██╔██╗ ██║   ██║   █████╗      ██████╔╝   ██║   ███████╗██████╔╝")
    print("██║     ██║     ██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝      ██╔══██╗   ██║   ╚════██║██╔═══╝ ")
    print("╚██████╗███████╗██║███████╗██║ ╚████║   ██║   ███████╗    ██║  ██║   ██║   ███████║██║     ")
    print(" ╚═════╝╚══════╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝     ")
    print("\n")

    

if __name__=='__main__':
    main()





   


