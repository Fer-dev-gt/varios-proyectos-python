import random


def run():
    numero_aleatoreo = random.randint(1, 100)
    numero_elegido = int(input("Elige un número del 1 al 100: \n"))
    while numero_elegido != numero_aleatoreo:
        if numero_elegido < numero_aleatoreo:
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")
        numero_elegido = int(input("Elige otro número: \n"))
    print("¡Ganaste!")

if __name__ == "__main__":
    run()