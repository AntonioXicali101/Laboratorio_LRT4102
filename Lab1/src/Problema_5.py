import random

def main():
    # Pick a random number between 1 and 10
    numero_oculto = random.randint(1, 10)
    intentos = 0
    encontrado = False

    # Keep guessing until the user finds the correct number
    while not encontrado:
        intento = int(input("Guess a number between 1 and 10: "))
        intentos += 1

        if intento < numero_oculto:
            print("Too low!")
        elif intento > numero_oculto:
            print("Too high!")
        else:
            print(f"Correct! You guessed the number in {intentos} attempts.")
            encontrado = True

if __name__ == "__main__":
    main()