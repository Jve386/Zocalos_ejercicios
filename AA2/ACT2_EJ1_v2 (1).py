import threading
import time
import datetime


def BuscarLlave():
    time.sleep(0.9)
    print('1.Busco la llave.')
    
def EncontrarLlave():
    time.sleep(0.7)
    print('2.Ya he encontrado la llave.')

def AbrirPuerta():
    time.sleep(0.3)
    print('3.Abro la puerta.')

def CerrarPuerta():
    time.sleep(0.5)
    print('4.Cierro la puerta.')

tiempo_ini = datetime.datetime.now()

#proceos 1
BuscarLlave()
#proceso 2
EncontrarLlave()
#proceso 3
AbrirPuerta()
#proceso 4
CerrarPuerta()


tiempo_fin = datetime.datetime.now()
print('Tiempo total de ejecuciÃ³n:',str(tiempo_fin.second - tiempo_ini.second))