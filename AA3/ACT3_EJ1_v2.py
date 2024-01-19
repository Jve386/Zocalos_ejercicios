import time
import multiprocessing

def entrada(coches):
    #simulamos la entrada de 200 coches
    for i in range(200):
        time.sleep(0.01)
        coches.value = coches.value + 1

def salida(coches):
    #simulamos la salida de 200 coches
    for i in range(200):
        time.sleep(0.01)
        coches.value = coches.value - 1

if __name__ == '__main__':
    coches = multiprocessing.Value('i', 300)
    entrada_coche = multiprocessing.Process(target=entrada, args=(coches,))
    salida_coche = multiprocessing.Process(target=salida, args=(coches,))

    entrada_coche.start()
    salida_coche.start()

    entrada_coche.join()
    salida_coche.join()