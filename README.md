# 🎓 Seminario de Seguridad, procesos y zócalos


**UOC (Universitat Oberta de Catalunya)** - **CFGS Desarrollo de Aplicaciones Multiplataforma**

## Objetivo general
Programar procesos concurrentes y procesos de comunicación en una red de forma segura.

## Descripción 
Con el crecimiento de la sociedad digital los casos de incidentes en ciberseguridad han crecido de forma exponencial, hasta el punto de ser unos de los campos que han sufrido una mayor inversión en los últimos años. El objetivo de este seminario es conocer el funcionamiento de las comunicaciones entre aplicaciones.

## 📜 Enunciados

### 🌟 AA1. Gestión de procesos

#### Descripción
En la seguridad de las redes, uno de los elementos más importantes es la gestión de servicios en sistemas operativos. En esta actividad entenderás cómo se gestionan los procesos de un sistema operativo y cómo se utilizan los mecanismos para compartir información entre diversos hilos de un mismo proceso.

#### Objetivos
- Conocer en profundidad el funcionamiento de los sistemas operativos en lo relativo a la ejecución de diferentes programas y/o procesos.

#### Pasos a seguir:
1. Estudiar y aprender el funcionamiento de los sistemas operativos en lo relativo a la gestión de procesos.
2. Crear una máquina virtual Debian en VirtualBox en modo transparente para realizar las diferentes actividades.
3. Preparar el entorno de desarrollo de Python para el desarrollo de las actividades instalando Python 3.7 o superior y Visual Studio Code.
4. Abrir un Shell de Debian para monitorizar los procesos del sistema. Ejecutar la orden `pstree` con las opciones adecuadas para mostrar el árbol de procesos de un usuario en concreto (TU USUARIO).
5. Comprobar haciendo uso de la orden `ps -la` y de los valores `PID` y `PPID` mostrados para cada proceso, que efectivamente los procesos son padre e hijo. ¿Cuáles serían las opciones necesarias para mostrar los procesos de un usuario concreto en vista detallada? Ejecuta el comando y explica la información que presenta.
6. Indicar el número de proceso asignado (PID) y cuál es su proceso padre (PPID) del proceso de terminal.
7. Finalizar el proceso terminal con el comando `Kill -9` y el número de proceso asignado. ¿Qué ocurre? Explícalo.
8. Ejecutar el programa `python ACT1_EJ1_v2.py` disponible en el área de recursos del aula y explicar el funcionamiento del programa. **(Lo adjunto en el directorio AA1)**
9. Realizar un resumen con todos los puntos descritos.

---

### 🌟 AA2. Programación de hilos

#### Descripción
Uno de los aspectos más importantes de las comunicaciones actuales es la posibilidad de trabajar con la programación distribuida. La actividad tiene como objetivo aprender los conceptos de programación multi-hilo y multiproceso.

#### Objetivos
- Entender y desarrollar programas utilizando mecanismos multihilo y multiproceso.

#### Pasos a seguir:
1. Estudiar y aprender los conceptos básicos del funcionamiento de los sistemas en lo relativo a la ejecución de diferentes hilos de ejecución.
2. Ejecutar el programa `ACT2_EJ1_v2.py` disponible en el área de recursos del aula y explicar el funcionamiento del programa y el tiempo de ejecución.
3. Modificar el anterior programa para que se ejecuten cada una de las funciones definidas en diferentes hilos de ejecución y en el orden correcto. Explicar el funcionamiento y el tiempo de ejecución del programa. Podéis utilizar la función `threading.Thread`. **(Lo adjunto en el directorio AA2)**
   NOTA: no se pueden añadir sleeps para sincronizar las funciones.
4. Realizar las modificaciones necesarias en el programa anterior para que los métodos se ejecuten en orden. Pista: Podéis utilizar la función `start` y `join`.
5. Realizar un resumen con todos los puntos descritos.

---

### 🌟 AA3. Programación de comunicaciones en red

#### Descripción
Las redes de comunicaciones son el primer elemento de seguridad de cualquier infraestructura de una empresa. El resultado de esta actividad es conocer los protocolos básicos de comunicación entre aplicaciones y los principales modelos de computación distribuida.

#### Objetivos
- Conocer en profundidad el funcionamiento de los mecanismos de seguridad en la programación y el uso de la criptografía para las comunicaciones seguras.
- Entender y desarrollar programas utilizando mecanismos multiprocesos.

#### Pasos a seguir
1. Estudiar y aprender los conceptos básicos del funcionamiento de los protocolos de comunicación.
2. Explicar el funcionamiento básico de un Malware tipo troyano. Explica el tipo de comunicación y conexión que se realiza. Explica la diferencia entre un Troyano y un Ransomware, pon al menos un ejemplo de cada uno.
3. Explicar la diferencia entre multiproceso y multihilo.
4. Explicar la diferencia entre un thread daemon y non-daemon. Acompaña la explicación con un breve código de ejemplo.
5. Ejecutar el programa `ACT3_EJ1_v2.py` disponible en el área de recursos del aula y explicar el funcionamiento del programa. Añadir un mecanismo de sincronización que permita a los procesos compartir el mismo espacio de memoria. Podéis utilizar la función `lock` y `acquire`. **(Lo adjunto en el directorio AA3)**
6. Realizar un resumen con todos los puntos descritos.

---

Si deseas compartir ejercicios de un semestre diferente o colaborar en este repositorio para ayudar a futuros estudiantes, ¡sería genial!
