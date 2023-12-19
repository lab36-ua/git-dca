import random

def jugar_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("****************************************")
    print("* ¡Bienvenido al juego de adivinanzas! *")
    print("****************************************")
    print("Estoy pensando en un número entre 1 y 100. ¡Adivina!")

    nombre = input("Introduce tu nombre: ")

    while True:
        intento_usuario = int(input("Tu suposición: "))
        intentos += 1

        if intento_usuario < numero_secreto:
            print(f"Muy bajo. Intenta de nuevo, {nombre}.")
        elif intento_usuario > numero_secreto:
            print(f"Muy alto. Intenta de nuevo, {nombre}.")
        else:
            print(f"¡Felicidades {nombre}! ¡Adivinaste el número en {intentos} intentos!")
            break

if __name__ == "__main__":
    jugar_adivinanza()

