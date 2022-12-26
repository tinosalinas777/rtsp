import threading

def suma(a):
    #res=a+b
    print(a)

def resta(a):
    #res=a-b
    print(a)

z="cristian"
x="salinas"
hilo1 = threading.Thread(target=suma,args=(x,))#no olvidar coma despues de la variable o tira error
hilo2 = threading.Thread(target=resta,args=(z,))


hilo1.start()
hilo2.start()