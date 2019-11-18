import random
import time
phealth = 100
slap = 0
pchealth = 100
drunken = 0
def play():
    global phealth
    global pchealth
    global slap
    print("So ya just der in da bar doin ya shit mate")
    time.sleep(1)
    print("And suddenly you see a guy across the room lookin liek a fucken idiot")
    time.sleep(1)
    print("Then this guy walks up to you..")
    time.sleep(1)
    print("Out of nowhere he decides to fight you like the fckin retard he is")
    time.sleep(.5)
    def drunkguy():
        global phealth
        global pchealth
        global drunken
        if drunken < 5:
            drunkguyu = random.randint(1,2)
        elif drunken == 5:
            drunkh = random.randint(40,60)
            print("The guy has drank too much and slightly collapsed losing a turn!!")
            time.sleep(1)
            print("He also loses",drunkh,"health!")
            drunken += 1
            pchealth -= drunkh
            drunkguyu = 3
        elif drunken > 5:
            drunkguyu = 1
        if drunkguyu == 1:
            plop = random.randint(17,20)
            phealth -= plop
            print("The drunk guy hit u with",plop,"damage!")
        elif drunkguyu == 3:
            print("")
        else:
            spap = random.randint(15,20)
            pchealth += spap
            print("The drunk guy drank more beer and healed for", spap,"health1!!!!!!")
            drunken += 1
            
        
    def punch():
        global pchealth
        punchu = random.randint(1,3)
        if punchu == 1 or punchu == 2:
            punchdam = random.randint(20,23)
            print("YOU SUCCESSFULLY PUNCHED THAT MOTHERFUCKER DEALING",punchdam,"DAMAGEEE")
            pchealth = pchealth - punchdam
        else:
            print("You missed lmao so sad")

    def kick():
        global pchealth
        kicku = random.randint(1,2)
        if kicku == 1:
            kickdam = random.randint(30,35)
            print("yoU SUCCESFULLY KICKED THAT BITCH LIKE THE BRUCE LEE YOU ARE DEALING",kickdam,"DAMAGEEEE")
            pchealth = pchealth - kickdam
        else:
            print("You missed haha so sad")
    def kiss():
        global pchealth
        global phealth
        kissdam = random.randint(13,15)
        print("YOU SUCKED THE LIFE AND DIGNITY OF THAT BITCH HEALING YOURSELF FOR",kissdam,"health")
        phealth += kissdam
        
    def kameha():
        global pchealth
        kamehau = random.randint(1,10)
        if kamehau == 1:
            kamehadam = 100
            print("KAMEEEEEEE")
            time.sleep(1)
            print("HAMEEEEEEE")
            time.sleep(2)
            print("HAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            time.sleep(2)
            print("You fuckin went super saiyan on that bitch and obliterated him!")
            pchealth = pchealth - kamehadam
        else:
            print("You missed, it's hard to hit a kamehameha mate")
    def pachoochoo():
        global slap
        print("What do you want to do?")
        print("(1) Punch!(20-23 damage 33% chance to miss)")
        print("(2) Kick!(30-35 damage 50% chance to miss)")
        print("(3) Kamehameha the fck out of this guy (100 damage 90% chance to miss)")
        print("(4) Kiss him (does 0 damage but heals you for 13-15 health)")
        while slap != "1" and slap != "2" and slap !="3" and slap!="4":
            slap = input("Just input 1 2 or 3 dont be a bitch:")
        if slap == "1":
            punch()
        elif slap == "2":
            kick()
        elif slap == "3":
            kameha()
        elif slap == "4":
            kiss()
    def check():
        global phealth
        global pchealth
        if pchealth <= 0:
            print("You won that bitch lmao")
        if phealth <= 0:
            print("You lost so sad")
        
    while phealth > 0 and pchealth > 0:
        global slap
        pachoochoo()
        time.sleep(2)
        check()
        if pchealth <= 0:
            break
        print("The dude still has",pchealth,"health!")
        time.sleep(2)
        drunkguy()
        time.sleep(1)
        check()
        if phealth <= 0:
            break
        print("You now have",phealth,"health left!")
        slap = "0"
    else:
        print("Ey you fuckin won lmao")
playplay = input("So, wanna play? (type yes):")
while playplay.lower() == "yes":
    pchealth = 100
    phealth = 100
    play()
    playplay = input("Do you wanna walk in dat fkin bar again? (type yes):")
    slap = "0"
    drunken = 0
else:
    print("The bar got burnt lmao so sad")
