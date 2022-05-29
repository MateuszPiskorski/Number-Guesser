from random import randint

computer_number = randint(1, 100)


def guesser(computer_number: int):
    player_number = input("Guess the number: ")

    try:
        player_number = int(player_number)
    except ValueError:
        return print("It's not a number!"), guesser(computer_number)

    if player_number < computer_number:
        return print("To small!"), guesser(computer_number)
    elif player_number > computer_number:
        return print("To big!"), guesser(computer_number)
    else:
        return print("You win!")


if __name__ == '__main__':
    guesser(computer_number)
