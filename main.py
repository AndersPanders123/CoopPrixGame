Money = 54
Bank = 1000
Monster = 22
Cookies = 32
Pizza = 110
Is = 15
Kjøping = True

def Overføring(Money, Bank):
    print("Broke individual ")
    Overføring = str(input("Vil du overføre penger? ")).lower()
    if "ja" in Overføring:
        print("Du har",Bank,"i banken") 
        while True:
            try:
                PengeOverføring = int(input("Hvor mye vil du ta ut? ")) 
                if Bank >= PengeOverføring:
                    Money += PengeOverføring
                    Bank -= PengeOverføring 
                    print("Du har", Money,"penger")
                break
            except:
                print("Tulling, ta ut penger med tall.")

def CoopPrix(Vare):
    
while Kjøping:

    kjøp = str(input("Hva vil du ha i dag? ")).lower()

    if "monster" in kjøp and "cookies" in kjøp and "is" in kjøp:
        if Money < Monster + Cookies + Is:
            Overføring(Money, Bank)
        else:
            Money = Money - (Monster + Cookies + Is)
            print("Du kjøper Monster, Cookies og Is")
            print(Money, "Penger igjen")


    elif "lommebok" in kjøp:
        print(Money)


    elif "monster" in kjøp:
        if Money < Monster:
            Overføring(Money,Bank)
        else:
            Money = Money - Monster
            print("Du kjøper en Monster")
            print(Money, "Penger igjen")


    elif "cookies" in kjøp:
        if Money < Cookies:
            Overføring(Money,Bank)
        else:
            Money = Money - Cookies
            print("Du kjøper Cookies")
            print(Money, "Penger igjen")


    elif "is" in kjøp:
        if Money < Is:
            Overføring(Money,Bank)
        else:
            Money = Money - Is
            print("Du kjøper is")
            print(Money, "Penger igjen")


    elif "Pizza" in kjøp:
        if Money < Pizza:
            Overføring(Money,Bank)
        else:
            Money = Money - Pizza
            print("Du kjøper Pizza")
            print(Money, "Penger igjen")
        
    else:
        print("GO BACK TO THE ZOO")

    Kjøping2 = str(input("Vil du kjøpe noe mer? ")).lower()
    if "nei" in Kjøping2:
        Kjøping = False
        print("Hade bra sjef.")