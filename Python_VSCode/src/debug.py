
from random import randint


def generate_variables():
    # Genera un numero aleatorio del 1 al 5
    random_number = randint(1, 5)

    return random_number

random_number = generate_variables()

# Numero de vidas
lifes = 2
print(random_number)


while lifes > 0:
    guess = int(input("Enter your guess: "))

    if guess == random_number:
        print("You win")
        break
    elif lifes == 1:
        print("You lose")
        break
    else:
        lifes -= 1

