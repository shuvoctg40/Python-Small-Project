# guessing Number = 18
# no of guesses 9
# print no of guesses left
# No of Guesses he took to finish
# game over

guess = 18
print("Guessing Number Game(Drop 9 times)")
i = 0
while i<9:
    print("Enter your Guess", 9-i, "times: ", end = ' ')
    inp = int(input())
    if inp == guess:
        print("You are won\n")
        break
    elif inp <= 10:
        print("Your Guess is very low")
    elif 10 < inp < guess:
        print("Your input is low")
    elif 25 <= inp:
        print("Your input is very high")
    elif 25 > inp > guess:
        print("Your input is high")
    i += 1
    if i == 9:
        print("Game Over")
        break


