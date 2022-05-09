from filosofo import *
from ventana import window

if __name__=="__main__":
    window = window()


    lista=[]
    for i in range(N):
        lista.append(filosofo(window)) #AGREGA UN FILOSOFO A LA LISTA

    for f in lista:
        f.start() #ES EQUIVALENTE A RUN()
    window.run()
    for f in lista:
        f.join() #BLOQUEA HASTA QUE TERMINA EL THREAD