import random

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

    respuesta = random.choice(respuestas)

    print("Bola Mágica dice:", respuesta)

bola_magica()
