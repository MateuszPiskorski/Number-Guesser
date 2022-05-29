def guesser(min_num, max_num):
    return int((max_num - min_num) / 2) + min_num


def reversed_guesser(min_num=0, max_num=1000):
    print("Think about number from 1 to 1000 and I will guess it in 10 moves max ;)")

    guess = guesser(min_num, max_num)

    print("Guessing:", guess)
    check = input("""Your turn:
    -> To small - type 1
    -> To big - type 2
    -> You win! - type 3
    (do not cheat): """)

    try:
        check = int(check)
    except ValueError:
        print("You need to provide a number 1, 2 or 3"), reversed_guesser()

    if check not in range(1, 4):
        print("You need to provide a number 1, 2 or 3"), reversed_guesser()
    if check == 1:
        reversed_guesser(guess, max_num)
    elif check == 2:
        reversed_guesser(min_num, guess)
    elif check == 3:
        print("I won!")
    else:
        print("Do not cheat!"), reversed_guesser()


if __name__ == '__main__':
    reversed_guesser()
