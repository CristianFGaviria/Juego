import random

def play ():
    user = input("Ingresa Piedra, Papel o Tijera: ")
    computer = random.choice(["Piedra", "Papel", "Tijera"])

    if user == computer:
        return "ES UN EMPATE !!!!"

    if is_win(user, computer):
        return "GANASTE"

    return "PERDISTE"

def is_win (player, opponent):
    if (player == "Piedra" and opponent == "Tijeras") or (player == "Tijeras" and opponent == "Papel") or (player == "Papel" and opponent == "Piedra"):
        return True

print(play())