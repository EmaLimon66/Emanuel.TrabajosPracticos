import random
import time
#ej4
def generar_numero_par_aleatorio():
    numero_par_aleatorio = random.randrange(2, 11, 2)
    return numero_par_aleatorio

inicio_tiempo = time.time()

numero_par = generar_numero_par_aleatorio()

print("Número par al azar entre 2 y 10:", numero_par)

fin_tiempo = time.time()
tiempo_ejecucion = fin_tiempo - inicio_tiempo
print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

def bola_magica():
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]


    pregunta = input("Hazme una pregunta: ")

    inicio_tiempo = time.time()
    respuesta = random.choice(respuestas)

    print("Bola Mágica dice:", respuesta)

    fin_tiempo = time.time()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")


#ej5
bola_magica()
import random
import time

def bola_magica():
    respuestas = [
        "Es seguro que sí",
        "Las chances son buenas",
        "Puedes contar con ello",
        "Pregúntame de nuevo más tarde",
        "Concéntrate y pregunta de nuevo",
        "No veo con claridad, intenta de nuevo",
        "Mi respuesta es no",
        "Mis fuentes me dicen que no"
    ]

    pregunta = input("Hazme una pregunta: ")

    inicio_tiempo = time.time()
    respuesta = random.choice(respuestas)


    print("Bola Mágica dice:", respuesta)

    fin_tiempo = time.time()
    tiempo_ejecucion = fin_tiempo - inicio_tiempo
    print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")

bola_magica()
