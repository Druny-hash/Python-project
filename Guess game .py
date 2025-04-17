def guess_game():
    secret_number = 11
    guess_count = 0
    guess_limit = 3
    while guess_count < guess_limit:
        guess = int(input("Guess :"))
        guess_count = guess_count + 1
        if guess == secret_number:
            print("You Won! ")
            return True
    else:
        print("You Lost! ")
        return False

result = guess_game()
print(result)