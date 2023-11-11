import random

def generar_numero_par_aleatorio():
    numero_par_aleatorio = random.randrange(2, 11, 2)
    return numero_par_aleatorio

while True:
    numero_par = generar_numero_par_aleatorio()
    print("Número par al azar entre 2 y 10:", numero_par)
    input("Presiona Enter para generar otro número par...")


