import time
import random

name = input("WHATS YO NAME? ")
print ("HELLO, " + name, "TIME TO PLAY HANGMAN BY LEOO!")
print ("")
time.sleep(1)
print ("LETS GOOO")
time.sleep(1)
word = random.randint(1,12)

if word == 1:
    word = "LEOMARC"
elif word == 2:
    word = "GIBSON"
elif word == 3:
    word = "GAB"
elif word == 4:
    word = "TERENCE"
elif word == 5:
    word = "TRISHA"
elif word == 6:
    word = "PAT"
elif word == 7:
    word = "CHAPONK"
elif word == 8:
    word = "JEAN"
elif word == 9:
    word = "CLOTHES"
elif word == 10:
    word = "DOMINATION"
elif word == 11:
    word = "ALISSHA"
elif word == 12:
    word = "KHRYSTAL"
    
guesses = ""
turns = 14
while turns > 0:         
    failed = 0               
    for char in word:      
        if char in guesses:    
            print (char,end=""),    

        else:
            print ("-",end=""),     
            failed += 1    
    if failed == 0:
        print("")
        print ("You won")  
        break              
    print("")
    guess = input("guess a character:").upper()
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print ("Wrong")    
        print ("You have", + turns, "more guesses")
        if turns == 0:           
            print ("You Loose") 
