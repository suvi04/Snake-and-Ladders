import random
locxn_1p=0
locxn_2p=0
#P1's turn
 
while True:
    dice_P1=random.randint(1,6)
    if dice_P1==6:
        print("P1 threw the dice - ",dice_P1,"\nP1 gets another turn ")
        locxn_1p=int(locxn_1p)+int(dice_P1)
        if locxn_1p==locxn_2p:
            locxn_2p=0
            print("P1 cut P2")
        print("P1 landed at - ",locxn_1p," initially ")
        dice_P1_2=random.randint(1,6)
        print("P1 threw the dice again- ",dice_P1_2)
        locxn_1p=int(locxn_1p)+int(dice_P1_2)
        if locxn_1p==locxn_2p:
            locxn_2p=0
            print("P1 cut P2")
        print("P1 finally landed at - ",locxn_1p)
        input()
    else:
        print("P1 threw the dice - ",dice_P1)
        locxn_1p=int(locxn_1p)+int(dice_P1)
        if locxn_1p==locxn_2p:
            locxn_2p=0
            print("P1 cut P2")
        print("P1 landed at - ",locxn_1p)
        input()
#P2's turn
    dice_P2=random.randint(1,6)
    if dice_P2==6:
        print("P2 threw the dice - ",dice_P2,"\nP2 gets another turn ")
        locxn_2p=int(locxn_2p)+int(dice_P2)
        print("P2 landed at - ",locxn_2p," initially ")
        if locxn_1p==locxn_2p:
            locxn_1p=0
            print("P2 cut P1")
        dice_P1_2=random.randint(1,6)
        print("P2 threw the dice again - ",dice_P1_2)
        locxn_2p=int(locxn_2p)+int(dice_P1_2)
        if locxn_1p==locxn_2p:
            locxn_1p=0
            print("P2 cut P1")
        print("P2 finally landed at - ",locxn_2p)
        input()
    else:
        print("P2 threw the dice - ",dice_P2)
        locxn_2p=int(locxn_2p)+int(dice_P2)
        if locxn_1p==locxn_2p:
            locxn_1p=0
            print("P2 cut P1")
        print("P2 landed at - ",locxn_2p)
        input()

#------------------FOR P1---------------------
#Snakes
    if locxn_1p==21:
        print("SIKE! You got bit.")
        locxn_1p=int(15)
        print("You landed on",locxn_1p)
    if locxn_1p==23:   
        print("SIKE! You got bit.")
        locxn_1p=int(6)
        print("You landed on",locxn_1p)
    if locxn_1p==29:
        print("SIKE! You got bit.") 
        locxn_1p=int(15)
        print("You landed on",locxn_1p)
    if locxn_1p==35:
        print("SIKE! You got bit.")
        locxn_1p=int(18)
        print("You landed on",locxn_1p)
    if locxn_1p==32:
        print("SIKE! You got bit.")
        locxn_1p=int(47)
        print("You landed on",locxn_1p)
    if locxn_1p==52:
        print("SIKE! You got bit.") 
        locxn_1p=int(38)
        print("You landed on",locxn_1p)
    if locxn_1p==71:
        print("SIKE! You got bit.")
        locxn_1p=int(34)
        print("You landed on",locxn_1p)
    if locxn_1p==69:
        print("SIKE! You got bit.")
        locxn_1p=int(42)
        print("You landed on",locxn_1p)
    if locxn_1p==82:
        print("SIKE! You got bit.") 
        locxn_1p=int(59)
        print("You landed on",locxn_1p)
    if locxn_1p==95:
        print("SIKE! You got bit.")
        locxn_1p=int(32)
        print("You landed on",locxn_1p)
    if locxn_1p==99:
        print("SIKE! You got bit.")
        locxn_1p=int(79)
        print("You landed on",locxn_1p)
#Ladders
    if locxn_1p==2:
        print("YAY! You climbed up .") 
        locxn_1p=int(18)
        print("You landed on",locxn_1p)
    if locxn_1p==12:
        print("YAY! You climbed up .") 
        locxn_1p=int(28)
        print("You landed on",locxn_1p)
    if locxn_1p==11:
        print("YAY! You climbed up .") 
        locxn_1p=int(31)
        print("You landed on",locxn_1p)
    if locxn_1p==70:
        print("YAY! You climbed up .") 
        locxn_1p=int(94)
        print("You landed on",locxn_1p)
    if locxn_1p==85:
        print("YAY! You climbed up .") 
        locxn_1p=int(97)
        print("You landed on",locxn_1p)
    if locxn_1p==22:
        print("YAY! You climbed up .") 
        locxn_1p=int(40)
        print("You landed on",locxn_1p)
    if locxn_1p==41:
        print("YAY! You climbed up .") 
        locxn_1p=int(59)
        print("You landed on",locxn_1p)
    if locxn_1p==77:
        print("YAY! You climbed up .") 
        locxn_1p=int(84)
        print("You landed on",locxn_1p)
    if locxn_1p==46:
        print("YAY! You climbed up .") 
        locxn_1p=int(55)
        print("You landed on",locxn_1p)
    if locxn_1p==36:
        print("YAY! You climbed up .") 
        locxn_1p=int(62)
        print("You landed on",locxn_1p)
    if locxn_1p==41:
        print("YAY! You climbed up .") 
        locxn_1p=int(59)
        print("You landed on",locxn_1p)



#Snakes
    if locxn_2p==21:
        print("SIKE! You got bit.")
        locxn_2p=int(15)
        print("You landed on",locxn_2p)
    if locxn_2p==23:   
        print("SIKE! You got bit.")
        locxn_2p=int(6)
        print("You landed on",locxn_2p)
    if locxn_2p==29:
        print("SIKE! You got bit.") 
        locxn_2p=int(15)
        print("You landed on",locxn_2p)
    if locxn_2p==35:
        print("SIKE! You got bit.")
        locxn_2p=int(18)
        print("You landed on",locxn_2p)
    if locxn_2p==32:
        print("SIKE! You got bit.")
        locxn_2p=int(47)
        print("You landed on",locxn_2p)
    if locxn_2p==52:
        print("SIKE! You got bit.") 
        locxn_2p=int(38)
        print("You landed on",locxn_2p)
    if locxn_2p==71:
        print("SIKE! You got bit.")
        locxn_2p=int(34)
        print("You landed on",locxn_2p)
    if locxn_2p==69:
        print("SIKE! You got bit.")
        locxn_2p=int(42)
        print("You landed on",locxn_2p)
    if locxn_2p==82:
        print("SIKE! You got bit.") 
        locxn_2p=int(59)
        print("You landed on",locxn_2p)
    if locxn_2p==95:
        print("SIKE! You got bit.")
        locxn_2p=int(32)
        print("You landed on",locxn_2p)
    if locxn_2p==99:
        print("SIKE! You got bit.")
        locxn_2p=int(79)
        print("You landed on",locxn_2p)
#Ladders
    if locxn_2p==2:
        print("YAY! You climbed up .") 
        locxn_2p=int(18)
        print("You landed on",locxn_2p)
    if locxn_2p==12:
        print("YAY! You climbed up .") 
        locxn_2p=int(28)
        print("You landed on",locxn_2p)
    if locxn_2p==11:
        print("YAY! You climbed up .") 
        locxn_2p=int(31)
        print("You landed on",locxn_2p)
    if locxn_2p==70:
        print("YAY! You climbed up .") 
        locxn_2p=int(94)
        print("You landed on",locxn_2p)
    if locxn_2p==85:
        print("YAY! You climbed up .") 
        locxn_2p=int(97)
        print("You landed on",locxn_2p)
    if locxn_2p==22:
        print("YAY! You climbed up .") 
        locxn_2p=int(40)
        print("You landed on",locxn_2p)
    if locxn_2p==41:
        print("YAY! You climbed up .") 
        locxn_2p=int(59)
        print("You landed on",locxn_2p)
    if locxn_2p==77:
        print("YAY! You climbed up .") 
        locxn_2p=int(84)
        print("You landed on",locxn_2p)
    if locxn_2p==46:
        print("YAY! You climbed up .") 
        locxn_2p=int(55)
        print("You landed on",locxn_2p)
    if locxn_2p==36:
        print("YAY! You climbed up .") 
        locxn_2p=int(62)
        print("You landed on",locxn_2p)
    if locxn_2p==41:
        print("YAY! You climbed up .") 
        locxn_2p=int(59)
        print("You landed on",locxn_2p)


#Winning condition
    if locxn_1p>=100:
        print("YAY P1 Won ")
        break
    if locxn_2p>=100:
        print("YAY P2 Won ")
        break