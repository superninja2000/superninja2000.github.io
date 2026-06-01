import time
import sys
import random
playagain = 0
right = 0
total = 0
start = 0
print(r" ___     _    _    _    __        __    _        _____    ____")
print(r"|  _ \  | |  | |  | |  |   \    /   |  | |      / ___ \  |  _ \ ")
print(r"| | \ \ | |  | |  | |  | |\ \  / /| |  | |__   |  ____|  | | \_\ ")
print(r"| |  \ \| |  \ \__/ /  | | \ \/ / | |  |    \  \ \____   | |")
print(r"|_|   \___|   \____/   |_|  \__/  |_|  |____/   \_____|  |_|")
print(r"  _______    _    _     _____    _____    _____      _____    ____")
print(r" / ______|  | |  | |   / ___ \  / ____|  / ____|    / ___ \  |  _ \ ")
print(r"| |   ____  | |  | |  |  ____|  \ \____  \ \____   |  ____|  | | \_\ ")
print(r" \ \___\ \  \ \__/ /  \ \____    \___  \  \___  \  \ \____   | |")
print(r"  \______/   \____/    \_____|   |_____/  |_____/   \_____|  |_|")
print("")
time.sleep(2)
print("I will think of a number between 1 and 5. Try to guess that number.")
start = 1
while True:
    if start == 1:
        start = 0
        number = random.randint(1, 5)
        time.sleep(2)
        areyouready = input("Are you ready? ")
        if areyouready == "y":
            time.sleep(1)
            print ("That's great!")
            time.sleep(1)
            print("I'm thinking of a number", end="")
            for dot in "... ":
                time.sleep(0.5)
                sys.stdout.write(dot)
                sys.stdout.flush()
            print("Ok. I've got it!")
            time.sleep(2)
            guess = int(input("What's your guess? (Numbers only) "))
            if guess == number:
                time.sleep(2)
                print("You guessed correctly! Good Job!")
                right = right+1
                total = total+1
            else:
                time.sleep(2)
                print("Good guess! However,",number,"was the number I thought of. Better luck next time.")
                total = total+1
            time.sleep(2)
            print("You have guessed",right, "correct out of",total, "total guesses.")
            percent = right/total*100
            print("You guess correctly",percent,"percent of the time.")
            time.sleep(3)
            playagain = 1
            if playagain == 1:
                playagain = 0
                keepgoing = input("Would you like to keep playing? ")
                if keepgoing == "y":
                    time.sleep(1)
                    print("Alright! Time to play again!")
                    start = 1
                elif keepgoing == "n":
                    time.sleep(1)
                    print("Play again soon!")
                    sys.exit()
                else:
                    time.sleep(1)
                    print("Answer in y or n only please.")
                    time.sleep(1)
                    playagain = 1
        elif areyouready == "n":
            time.sleep(1)
            print ("You're a terrible person for not guessing.")
            sys.exit()
        else:
            time.sleep(1)
            print("Answer in y or n only please.")
            start = 1