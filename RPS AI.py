import random
import time
spapop = 0
plaplu = "yes"
def play():
    global spapop
    print("I AM AN AI MADE BY LEO")
    time.sleep(1)
    print("i challenGE U TO A ROCK PEPA SISOR BATTLE")
    time.sleep(1)
    def rps():
        aimove = random.randint(1,3)
        move = 0
        global spapop
        print("What's your move? don't worry I won't cheat!")
        print("(1)Rock")
        print("(2)Paper")
        print("(3)Scissors")
        while move != "1"and move !="2" and move !="3":
            move = input("Rock, Paper, or Scissors?:")
        if move == "1" and aimove == 1:
            print("The computer chose rock")
            time.sleep(2)
            print("It's a draw! play again!")
            aimove -= aimove
            move = "0"
        if move == "2" and aimove == 2:
            print("The computer chose paper")
            time.sleep(2)
            print("It's a draw! play again!")
            aimove -= aimove
            move = "0"
        if move == "3" and aimove == 3:
            print("The computer chose scissors")
            time.sleep(2)
            print("It's a draw! play again!")
            aimove -= aimove
            move = "0"
        if move == "1" and aimove == 3:
            print("The computer chose scissors!")
            time.sleep(2)
            print("You won! awwwww YOU DIRTY CHEATER")
            spapop = 1
        if move == "2" and aimove == 1:
            print("The computer chose rock!")
            time.sleep(2)
            print("You won! awwwww YOU DIRTY CHEATER")
            spapop = 1
        if move == "3" and aimove == 2:
            print("The computer chose paper!")
            time.sleep(2)
            print("You won! awwwww YOU DIRTY CHEATER")
            spapop = 1
        if move == "1" and aimove == 2:
            print("The computer chose paper!")
            time.sleep(2)
            print("MWUAHAHAHAHA I BEAT YOU HUMAN")
            spapop = 2
        if move == "2" and aimove == 3:
            print("The computer chose scissors!")
            time.sleep(2)
            print("MWUAHAHAHAHA I BEAT YOU HUMAN")
            spapop = 2
        if move == "3" and aimove == 1:
            print("The computer chose rock!")
            time.sleep(2)
            print("MWUAHAHAHAHA I BEAT YOU HUMAN")
            spapop = 2
    while spapop != 1 and spapop != 2:
        rps()
        if spapop == 1:
            print("YOU WONT BEAT ME NEXT TIME")
        if spapop == 2:
            print("I BEAT YOU HUMAN MWUAHAHHAHAA REMEMBER THIS!!")
        
while plaplu == "yes" or plaplu == "Yes" or plaplu == "YES":
    play()
    spapop = spapop - spapop
    plaplu = input("Do you wanna play again? (type yes):")
