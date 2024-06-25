#made by Felix FD, Zac Lee and Lim Donghwan from S206.

import random

print("Welcome to Text Fighter!")
print("You will be fighting against a bot using moves.")
print("The moves you can choose are:")
print("")
print("1, Kick. It has a 80% hit rate and deals 10 damage, there is a 10% chance that it will deal 20 damage and a 1% chance that it will deal 50 damage.")
print("")
print("2, Punch. It has a 90% hit rate and deals 5 damage, there is a 10% chance that it will deal 10 damage and a 1% chance it will deal 100 damage.")
print("")
print("3, Dig. It has a 90% success rate and it allows you to ignore the bot's attack.")
print("")
print("4, Hatsune Miku. It has a 100% success rate. There is a 50% chance to heal 10 health and a 50% chance to deal 2 damage.")
print("")
print("5, Steal. It has a 20% success rate. There is a 20% chance you will steal 10hp from the enemy and a 5% chance you will steal 50hp!")
print("")
print("In this game, you will have 100 HP. If you get to 0, you die!")
print("Note that dmg is the abbreviation of damage, and that dealing dmg reduces your HP.")
print("The game will begin now!")

hp = 100
hp2 = 100
while hp > 0 and hp2 > 0:
    choice = input("Type 1, 2, 3, 4 or 5 to choose the move you want.")
    choice2 = random.randint(1,5)
    dtr1 = random.randint(1,100)
    dtr2 = random.randint(1,100)
    print("Bot chose:",choice2)
    if choice == '1':
        if dtr1>99 :
            if choice2 == 1:
                #when bot and player choice 1, where player gets 1% chance.
                if dtr2>99:
                    print("Both players dealt 50 damage to each other!")
                    hp -= 50
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 20 dmg and player dealt 50 dmg!")
                    hp -= 20
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Bot dealt 10 dmg and player dealt 50 dmg!")
                    hp -= 10
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<20:
                    print("Bot missed and player dealt 50 dmg!")
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 2:
                #when player choice 1 and bot choice 2, where player gets 1% chance.
                if dtr2>99:
                    print("Player deals 50 dmg and bot deals 100 dmg!")
                    hp -= 100
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Player deals 50 dmg and bot deals 10 dmg!")
                    hp -= 10
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>10:
                    print("Player deals 50 dmg and bot deals 5 dmg!")
                    hp -= 5
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Player deals 50 dmg and bot misses!")
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 3:
                #when player choice 1 and bot choice 3, where player gets 1% chance.
                if dtr2>10:
                    print("Player deals 50 dmg and bot successfully digs away from the attack!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<10:
                    print("Player deals 50 dmg and bot failed to dig away!")
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
            elif choice2 == 4:
                #when player choice 1 and bot choice 4, where player gets 1% chance.
                if dtr2>50:
                    print("Player deals 50 dmg and bot successfully heals 10hp!")
                    hp2 -= 40
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<50:
                    print("Player deals 50 dmg and bot deals 2 dmg!")
                    hp -= 2
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 5:
                #when player choice 1 and bot choice 5, where player gets 1% chance.
                if dtr2>95:
                    print("Bot stole 50hp and player dealt 50 dmg!")
                    hp -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>80:
                    print("Bot stole 10 hp and player dealt 50 dmg!")
                    hp -= 10
                    hp2 += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                elif dtr2<80:
                    print("Bot failed to steal hp and player dealt 50 dmg!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                
        elif dtr1>90:
            if choice2 == 1:
                  #when bot and player choice 1, where player gets 10% chance.
                if dtr2>99:
                    print("Bot dealt 50 dmg and player dealt 20 dmg")
                    hp -= 50
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Both dealt 20 dmg!")
                    hp -= 20
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Bot dealt 10 dmg and player dealt 20 dmg!")
                    hp -= 10
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<20:
                    print("Bot missed and player dealt 20 dmg!")
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
            elif choice2 == 2:
                #when player choice 1 and bot choice 2, where player gets 10% chance.
                if dtr2>99:
                    print("Player deals 20 dmg and bot deals 100 dmg!")
                    hp -= 100
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Player deals 20 dmg and bot deals 10 dmg!")
                    hp -= 10
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>10:
                    print("Player deals 20 dmg and bot deals 5 dmg!")
                    hp -= 5
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Player deals 20 dmg and bot misses!")
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 3:
                #when player choice 1 and bot choice 3, where player gets 10% chance.
                if dtr2>10:
                    print("Player deals 20 dmg and bot successfully digs away from the attack!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<10:
                    print("Player deals 20 dmg and bot failed to dig away!")
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 4:
                #when player choice 1 and bot choice 4, where player gets 10% chance.
                if dtr2>50:
                    print("Player deals 20 dmg and bot successfully heals 10hp!")
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<50:
                    print("Player deals 20 dmg and bot deals 2 dmg!")
                    hp -= 2
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 5:
                #when player choice 1 and bot choice 5, where player gets 10% chance.
                if dtr2>95:
                    print("Bot stole 50hp and player dealt 20 dmg!")
                    hp -= 50
                    hp2 += 30
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>80:
                    print("Bot stole 10 hp and player dealt 20 dmg!")
                    hp -= 10
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                elif dtr2<80:
                    print("Bot failed to steal hp and player dealt 20 dmg!")
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
        elif dtr1>20:
            if choice2 == 1:
                  #when bot and player choice 1, where player gets 80% chance.
                if dtr2>99:
                    print("Bot dealt 50 dmg and player dealt 10 dmg")
                    hp -= 50
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 20 dmg and player dealt 10 dmg!")
                    hp -= 20
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Both dealt 10 dmg!")
                    hp -= 10
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<20:
                    print("Bot missed and player dealt 10 dmg!")
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
            elif choice2 == 2:
                #when player choice 1 and bot choice 2, where player gets 80% chance.
                if dtr2>99:
                    print("Player deals 10 dmg and bot deals 100 dmg!")
                    hp -= 100
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Player deals 10 dmg and bot deals 10 dmg!")
                    hp -= 10
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>10:
                    print("Player deals 10 dmg and bot deals 5 dmg!")
                    hp -= 5
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Player deals 10 dmg and bot misses!")
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 3:
                #when player choice 1 and bot choice 3, where player gets 80% chance.
                if dtr2>10:
                    print("Player deals 10 dmg and bot successfully digs away from the attack!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<10:
                    print("Player deals 10 dmg and bot failed to dig away!")
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 4:
                #when player choice 1 and bot choice 4, where player gets 80% chance.
                if dtr2>50:
                    print("Player deals 10 dmg and bot successfully heals 10hp!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<50:
                    print("Player deals 10 dmg and bot deals 2 dmg!")
                    hp -= 2
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 5:
                #when player choice 1 and bot choice 5, where player gets 80% chance.
                if dtr2>95:
                    print("Bot stole 50hp and player dealt 10 dmg!")
                    hp -= 50
                    hp2 += 40
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>80:
                    print("Bot stole 10 hp and player dealt 10 dmg!")
                    hp -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                elif dtr2<80:
                    print("Bot failed to steal hp and player dealt 10 dmg!")
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
        elif dtr1<20:
            if choice2 == 1:
                  #when bot and player choice 1, where player misses.
                if dtr2>99:
                    print("Bot dealt 50 dmg and player missed!")
                    hp -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 20 dmg and player missed!")
                    hp -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Bot dealt 10 dmg and player missed!")
                    hp -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<20:
                    print("Both missed!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 2:
                #when player choice 1 and bot choice 2, where player misses.
                if dtr2>99:
                    print("Player misses and bot deals 100 dmg!")
                    hp -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Player misses and bot deals 10 dmg!")
                    hp -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>10:
                    print("Player misses and bot deals 5 dmg!")
                    hp -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Player and bot misses!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 3:
                #when player choice 1 and bot choice 3, where player misses.
                if dtr2>10:
                    print("Player misses and bot successfully digs away from the failed attack!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<10:
                    print("Player missed and bot failed to dig away!")
                    hp2 -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 4:
                #when player choice 1 and bot choice 4, where player misses.
                if dtr2>50:
                    print("Player misses and bot successfully heals 10hp!")
                    hp2 += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<50:
                    print("Player misses and bot deals 2 dmg!")
                    hp -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 5:
                #when player choice 1 and bot choice 5, where player misses.
                if dtr2>95:
                    print("Bot stole 50hp and player missed!")
                    hp -= 50
                    hp2 += 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>80:
                    print("Bot stole 10 hp and player missed!")
                    hp -= 10
                    hp2 += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                elif dtr2<80:
                    print("Bot failed to steal hp and player missed!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
            
    elif choice == '2':
        if dtr1>99 :
            if choice2 == 1:
                #when player choice 2 and bot choice 1, where player gets 1% chance.
                if dtr2>99:
                    print("Player deals 100 dmg and bot deals 50 dmg!")
                    hp -= 50
                    hp2 -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Player deals 100 dmg and bot deals 20 dmg!")
                    hp -= 20
                    hp2 -=100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Player deals 100 dmg and bot deals 10 dmg!")
                    hp -= 10
                    hp2 -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Player deals 100 dmg and bot misses!")
                    hp2 -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 2:
                #when bot and player choice 2, where player gets 1% chance.
                if dtr2>99:
                    print("Both players dealt 100 damage to each other!")
                    hp -= 100
                    hp2 -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 10 dmg and player dealt 100 dmg!")
                    hp -= 10
                    hp2 -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>10:
                    print("Bot dealt 5 dmg and player dealt 100 dmg!")
                    hp -= 5
                    hp2 -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Bot missed and player dealt 100 dmg!")
                    hp2 -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 3:
                #when player choice 2 and bot choice 3, where player gets 1% chance.
                if dtr2>10:
                    print("Player dealt 100 dmg and bot successfully digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2>10:
                    print("Player dealt 100 dmg and bot failed to dig away!")
                    hp2 -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 4:
                #when player choice 2 and bot choice 4, where player gets 1% chance.
                if dtr2>50:
                    print("Player dealt 100 dmg and bot healed 10hp!")
                    hp2 -= 90
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<50:
                    print("Player dealt 100 dmg and bot dealt 2 dmg!")
                    hp -= 2
                    hp2 -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
            elif choice2 == 5:
                #when player choice 2 and bot choice 5, where player gets 1% chance.
                if dtr2>95:
                    print("Player dealt 100 dmg and bot stole 50hp!")
                    hp -= 50
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2>80:
                    print("Player dealt 100 dmg and bot stole 10hp!")
                    hp -= 10
                    hp2 -= 90
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<80:
                    print("Player dealt 100 dmg and bot failed to steal!")
                    hp2 -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
            
        elif dtr1>90:
            if choice2 == 1:
                #when player choice 2 and bot choice 1, where player gets 10% chance.
                if dtr2>99:
                    print("Player deals 10 dmg and bot deals 50 dmg!")
                    hp -= 50
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Player deals 10 dmg and bot deals 20 dmg!")
                    hp -= 20
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Player deals 10 dmg and bot deals 10 dmg!")
                    hp -= 10
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Player deals 10 dmg and bot misses!")
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 2:
                  #when bot and player choice 2, where player gets 10% chance.
                if dtr2>99:
                    print("Bot dealt 100 dmg and player dealt 10 dmg")
                    hp -= 100
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Both dealt 10 dmg!")
                    hp -= 10
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>10:
                    print("Bot dealt 5 dmg and player dealt 10 dmg!")
                    hp -= 5
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Bot missed and player dealt 10 dmg!")
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 3:
                #when player choice 2 and bot choice 3, where player gets 10% chance.
                if dtr2>10:
                    print("Player dealt 10 dmg and bot successfully digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2>10:
                    print("Player dealt 10 dmg and bot failed to dig away!")
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 4:
                #when player choice 2 and bot choice 4, where player gets 10% chance.
                if dtr2>50:
                    print("Player dealt 10 dmg and bot healed 10hp!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<50:
                    print("Player dealt 10 dmg and bot dealt 2 dmg!")
                    hp -= 2
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
            elif choice2 == 5:
                #when player choice 2 and bot choice 5, where player gets 10% chance.
                if dtr2>95:
                    print("Player dealt 10 dmg and bot stole 50hp!")
                    hp -= 50
                    hp2 += 40
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2>80:
                    print("Player dealt 10 dmg and bot stole 10hp!")
                    hp -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<80:
                    print("Player dealt 10 dmg and bot failed to steal!")
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
        elif dtr1>10:
            if choice2 == 1:
                #when player choice 2 and bot choice 1, where player gets 80% chance.
                if dtr2>99:
                    print("Player deals 5 dmg and bot deals 50 dmg!")
                    hp -= 50
                    hp2 -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Player deals 5 dmg and bot deals 20 dmg!")
                    hp -= 20
                    hp2 -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Player deals 5 dmg and bot deals 10 dmg!")
                    hp -= 10
                    hp2 -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Player deals 5 dmg and bot misses!")
                    hp2 -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 2:
                  #when bot and player choice 2, where player gets 80% chance.
                if dtr2>99:
                    print("Bot dealt 100 dmg and player dealt 5 dmg")
                    hp -= 100
                    hp2 -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 10 dmg and player dealt 5 dmg!")
                    hp -= 10
                    hp2 -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>10:
                    print("Both dealt 5 dmg!")
                    hp -= 5
                    hp2 -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Bot missed and player dealt 5 dmg!")
                    hp2 -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 3:
                #when player choice 2 and bot choice 3, where player gets 80% chance.
                if dtr2>10:
                    print("Player dealt 5 dmg and bot successfully digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2>10:
                    print("Player dealt 5 dmg and bot failed to dig away!")
                    hp2 -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 4:
                #when player choice 2 and bot choice 4, where player gets 80% chance.
                if dtr2>50:
                    print("Player dealt 5 dmg and bot healed 10hp!")
                    hp2 += 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<50:
                    print("Player dealt 5 dmg and bot dealt 2 dmg!")
                    hp -= 2
                    hp2 -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 5:
                #when player choice 2 and bot choice 5, where player gets 80% chance.
                if dtr2>95:
                    print("Player dealt 5 dmg and bot stole 50hp!")
                    hp -= 50
                    hp2 += 45
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2>80:
                    print("Player dealt 5 dmg and bot stole 10hp!")
                    hp -= 10
                    hp2 += 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<80:
                    print("Player dealt 5 dmg and bot failed to steal!")
                    hp2 -= 5
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
        elif dtr1<10:
            if choice2 == 1:
                #when player choice 2 and bot choice 1, where player misses.
                if dtr2>99:
                    print("Player misses and bot deals 50 dmg!")
                    hp -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Player misses and bot deals 20 dmg!")
                    hp -= 20
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Player misses and bot deals 10 dmg!")
                    hp -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Both players missed!")
                    hp2 -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 2:
                  #when bot and player choice 2, where player misses.
                if dtr2>99:
                    print("Bot dealt 100 dmg and player missed!")
                    hp -= 100
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 10 dmg and player missed!")
                    hp -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>10:
                    print("Bot dealt 5 dmg and player missed!")
                    hp -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Both missed!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 3:
                #when player choice 2 and bot choice 3, where player misses.
                if dtr2>10:
                    print("Player missed and bot successfully digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2>10:
                    print("Player missed and bot failed to dig away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 4:
                #when player choice 2 and bot choice 4, where player misses.
                if dtr2>50:
                    print("Player missed and bot healed 10hp!")
                    hp2 += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<50:
                    print("Player missed and bot dealt 2 dmg!")
                    hp -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 5:
                #when player choice 2 and bot choice 5, where player gets 80% chance.
                if dtr2>95:
                    print("Player missed and bot stole 50hp!")
                    hp -= 50
                    hp2 += 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2>80:
                    print("Player missed and bot stole 10hp!")
                    hp -= 10
                    hp2 += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<80:
                    print("Player missed and bot failed to steal!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
        
    elif choice == '3':
        if dtr1>10 :
            if choice2 == 1:
                #when bot choice 1 and player choice 3, where player gets 90% chance.
                if dtr2>99:
                    print("Bot dealt 50 dmg and player digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 20 dmg and player digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Bot dealt 10 dmg and player digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<20:
                    print("Bot failed to attack and player digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 2:
                #when bot choice 2 and player choice 3, where player gets 90% chance.
                if dtr2>99:
                    print("Bot dealt 100 dmg and player digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 10 dmg and player digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Bot dealt 5 dmg and player digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<20:
                    print("Bot failed to attack and player digged away!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 3:
                #when bot and player choice 3, where player gets 90% chance.
                if dtr2>10:
                    print("Bot and player digged into the ground!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Player digged and bot failed to dig! ")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
            elif choice2 == 4:
                #when bot choice 4 and player choice 3, where player gets 90% chance.
                if dtr2>50:
                    print("Bot healed 10hp player digged into the ground!")
                    hp2 += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<50:
                    print("Bot dealt 2 dmg and player digged into the ground!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 5:
                #when bot choice 5 and player choice 3, where player gets 90% chance.
                if dtr2>95:
                    print("Bot stole 50hp and player digged into the ground!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>80:
                    print("Bot stole 10hp and player digged into the ground!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                elif dtr2<80:
                    print("Bot failed to steal and player digged into the ground!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
        elif dtr1<10 :
                if choice2 == 1:
                #when bot choice 1 and player choice 3, where player gets 10% chance.
                    if dtr2>99:
                        print("Bot dealt 50 dmg and player failed to dig away!")
                        hp -= 50
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    elif dtr2>90:
                        print("Bot dealt 20 dmg and player failed to dig away!")
                        hp -= 20
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    elif dtr2>20:
                        print("Bot dealt 10 dmg and player failed to dig away!")
                        hp -= 10
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    elif dtr2<20:
                        print("Bot failed to attack and player failed to dig away!")
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    else:
                        print("hakerman")
                        print(hp)
                        print(hp2)

                elif choice2 == 2:
                #when bot choice 2 and player choice 3, where player gets 10% chance. 
                    if dtr2>99:
                        print("Bot dealt 100 dmg and player failed to dig away!")
                        hp -= 100
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    elif dtr2>90:
                        print("Bot dealt 10 dmg and player failed to dig away!")
                        hp -= 10
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    elif dtr2>20:
                        print("Bot dealt 5 dmg and player failed to dig away!")
                        hp -= 5
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    elif dtr2<20:
                        print("Bot failed to attack and player failed to dig away!")
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    else:
                        print("hakerman")
                        print(hp)
                        print(hp2)
                    
                elif choice2 == 3:
                #when bot and player choice 3, where player gets 10% chance.
                    if dtr2>10:
                        print("Bot digged into the ground and player failed to dig!")
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    elif dtr2<10:
                        print("Player and bot failed to dig! ")
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    else:
                        print("hakerman")
                        print(hp)
                        print(hp2)
                        
                elif choice2 == 4:
                #when bot choice 4 and player choice 3, where player gets 10% chance.
                    if dtr2>50:
                        print("Bot healed 10hp player failed to dig!")
                        hp2 += 10
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    elif dtr2<50:
                        print("Bot dealt 2 dmg and player failed to dig!")
                        hp -= 2
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    else:
                        print("hakerman")
                        print(hp)
                        print(hp2)

                elif choice2 == 5:
                #when bot choice 5 and player choice 3, where player gets 10% chance.
                    if dtr2>95:
                        print("Bot stole 50hp and player failed to dig!")
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    elif dtr2>80:
                        print("Bot stole 10hp and player failed to dig!")
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
    
                    elif dtr2<80:
                        print("Bot failed to steal and player failed to dig!")
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)

                    else:
                        print("hakerman")
                        print(hp)
                        print(hp2)
                    
    elif choice == '4':
        if dtr1>50 :
            if choice2 == 1:
                #when bot choice 1 and player choice 4, where player gets heal 10hp.
                if dtr2>99:
                    print("Bot dealt 50 dmg and player healed 10hp!")
                    hp -= 40
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 20 dmg and player healed 10hp!")
                    hp -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Bot dealt 10 dmg and player healed 10hp!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<20:
                    print("Bot missed and player healed 10hp!")
                    hp += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 2:
                #when bot choice 2 and player choice 4, where player gets heal 10hp.
                if dtr2>99:
                    print("Bot dealt 100 dmg and player healed 10hp!")
                    hp -= 90
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 10 dmg and player healed 10hp!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Bot dealt 5 dmg and player healed 10hp!")
                    hp += 5 
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<20:
                    print("Bot missed and player healed 10hp!")
                    hp += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 3:
                #when bot choice 3 and player choice 4, where player gets heal 10hp.
                    if dtr2>10:
                        print("Bot digged into the ground and player healed 10hp!")
                        hp += 10
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    elif dtr2<10:
                        print("Player healed by 10 hp and bot failed to dig! ")
                        hp += 10
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    else:
                        print("hakerman")
                        print(hp)
                        print(hp2)
            
            elif choice2 == 4:
                #when bot and player choice 4, where player gets 50% chance (heal).
                if dtr2>50:
                    print("Both players healed themselves by 10hp!")
                    hp += 10
                    hp2 += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<50:
                    print("Bot dealt 2 dmg and player healed 10hp!")
                    hp += 8
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 5:
                #when bot and player choice 4, where player gets 50% chance (heal).
                if dtr2>95:
                    print("Bot stole 50hp and player healed 10 hp!")
                    hp -= 40
                    hp2 += 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>80:
                    print("Bot stole 10hp and player healed 10 hp!")
                    hp2 += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                elif dtr2<80:
                    print("Bot failed to steal and player healed 10 hp!")
                    hp += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
                    
        elif dtr1<50 :
            if choice2 == 1:
                #when bot choice 1 and player choice 4, where player deals 2 dmg.
                if dtr2>99:
                    print("Bot dealt 50 dmg and player dealt 2 dmg!")
                    hp -= 50
                    hp2 -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 20 dmg and player dealt 2 dmg!")
                    hp -= 20
                    hp2 -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Bot dealt 10 dmg and player dealt 2 dmg!")
                    hp -= 10
                    hp2 -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<20:
                    print("Bot missed and player dealt 2 dmg!")
                    hp2 -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 2:
                #when bot choice 2 and player choice 4, where player deals 2 dmg.
                if dtr2>99:
                    print("Bot dealt 100 dmg and player dealt 2 dmg!")
                    hp -= 100
                    hp2 -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>90:
                    print("Bot dealt 10 dmg and player dealt 2 dmg!")
                    hp -= 10
                    hp2 -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>20:
                    print("Bot dealt 5 dmg and player dealt 2 dmg!")
                    hp -= 5
                    hp2 -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<20:
                    print("Bot missed and player dealt 2 dmg!")
                    hp2 -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 3:
                #when bot choice 3 and player choice 4, where player deals 2 dmg.
                    if dtr2>10:
                        print("Bot digged into the ground and player dealt 2 dmg!")
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    elif dtr2<10:
                        print("Player dealt 2dmg and bot failed to dig! ")
                        hp2 -= 2
                        print("Your hp is:")
                        print(hp)
                        print("The enemy's hp is:")
                        print(hp2)
                    
                    else:
                        print("hakerman")
                        print(hp)
                        print(hp2)
                    
            elif choice2 == 4:
                #when bot and player choice 4, where player gets 50% chance (dmg 2).
                if dtr2>10:
                    print("Bot healed 10hp and player dealt 2 dmg!")
                    hp2 += 8 
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2<10:
                    print("Bot and player dealt 2 dmg!")
                    hp -= 2
                    hp2 -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)

            elif choice2 == 5:
                #when bot and player choice 4, where player deals 2 dmg.
                if dtr2>95:
                    print("Bot stole 50hp and player dealt 2 dmg!")
                    hp -= 50
                    hp2 += 48
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>80:
                    print("Bot stole 10hp and player dealt 2 dmg!")
                    hp -= 10
                    hp2 += 8
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                elif dtr2<80:
                    print("Bot failed to steal and player dealt 2 dmg!")
                    hp2 -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
            
    elif choice == '5':
        if dtr1>95 :
            if choice2 == 1:
                if dtr2 > 90:
                    print("Player stole 50hp from the Bot!")
                    hp2 -= 50
                    hp += 30
                    print("Bot did 20 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 == 90:
                    print("Player stole 50hp from the Bot!")
                    hp2 -= 50
                    
                    print("Bot did 50 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 > 20:
                    print("Player stole 50hp from the Bot!")
                    hp2 -= 50
                    hp += 40
                    print("Bot did 10 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 < 90:
                    print("Player stole 50hp from the Bot!")
                    hp2 -= 50
                    hp += 50
                    print("Bot did 0 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
            elif choice2 == 2:
                if dtr2 > 90:
                    print("Player stole 50hp from the Bot!")
                    hp2 -= 50
                    hp += 50
                    print("Bot did 0 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 < 90 and dtr >= 80:
                    print("Player stole 50hp from the Bot!")
                    hp2 -= 50
                    hp += 40
                    print("Bot did 10 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 == 1:
                    print("Player stole 50hp from the Bot!")
                    hp2 -= 50
                    hp -= 50
                    print("Bot did 100 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                    
                else:
                    print("Player stole 50hp from the Bot!")
                    hp2 -= 50
                    hp += 30
                    print("Bot did 20 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

            elif choice2 == 3:
                if dtr2>10:
                    print("Bot digged into the ground!")
                    print("Your Attack missed!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<=10:
                    print("Bot failed to dig!")
                    print("Your stole 50hp from Bot!")
                    hp2 -= 50
                    hp += 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
            elif choice2 == 4:
                if dtr2 > 50:
                    print("Your stole 50hp from Bot!")
                    print("Bot healed 10 hp")
                    hp2 -= 40
                    hp += 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 <= 50:
                    print("Your stole 50hp from Bot!")
                    print("Bot did 2 dmg to the player")
                    hp2 -= 50
                    hp += 48
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
            elif choice2 == 5:
                #when bot and player choice 5, where player gets 5% chance (50hp steal).
                if dtr2>95:
                    print("Both players stole 50hp from each other, no change!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>80:
                    print("Player stole 50hp and bot stole 10hp!")
                    hp += 40
                    hp2 -= 40
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                elif dtr2<80:
                    print("Player stole 50hp and bot failed to steal!")
                    hp += 50
                    hp2 -= 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
        elif dtr1>80:
            if choice2 == 1:
                if dtr2 > 90:
                    print("Player stole 10hp from the Bot!")
                    hp2 -= 10
                    hp -= 10
                    print("Bot did 20 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 == 90:
                    print("Player stole 10hp from the Bot!")
                    hp2 -= 10
                    hp -= 40
                    print("Bot did 50 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 > 20:
                    print("Player stole 10hp from the Bot!")
                    hp2 -= 10
                    print("Bot did 10 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 < 90:
                    print("Player stole 10hp from the Bot!")
                    hp2 -= 10
                    hp += 10
                    print("Bot did 0 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
            elif choice2 == 2:
                if dtr2 > 90:
                    print("Player stole 10hp from the Bot!")
                    hp2 -= 10
                    hp += 10
                    print("Bot did 0 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 < 90 and dtr >= 80:
                    print("Player stole 10hp from the Bot!")
                    hp2 -= 10
                    hp += 0
                    print("Bot did 10 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 == 1:
                    print("Player stole 10hp from the Bot!")
                    hp2 -= 10
                    hp -= 90
                    print("Bot did 100 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                    
                else:
                    print("Player stole 10hp from the Bot!")
                    hp2 -= 10
                    hp -= 10
                    print("Bot did 20 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

            elif choice2 == 3:
                if dtr2>10:
                    print("Bot digged into the ground!")
                    print("Your Attack missed!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<10:
                    print("Bot failed to dig!")
                    print("Your stole 10hp from Bot!")
                    hp2 -= 10
                    hp += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
            elif choice2 == 4:
                if dtr2 > 50:
                    print("Your stole 51hp from Bot!")
                    print("Bot healed 10 hp")
                    
                    hp += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 <50:
                    print("Your stole 10hp from Bot!")
                    print("Bot did 2 dmg to the player")
                    hp2 -= 10
                    hp += 8
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
            elif choice2 == 5:
                #when bot and player choice 5, where player gets 20% chance (10hp steal).
                if dtr2>95:
                    print("Bot stole 50 hp and player stole 10hp!")
                    hp -= 40
                    hp2 += 40
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>80:
                    print("Both stole 10hp, no change!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                elif dtr2<80:
                    print("Player stole 10hp and bot failed to steal!")
                    hp += 10
                    hp2 -= 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)
        elif dtr1<80:
            if choice2 == 1:
                if dtr2 > 90:
                    print("Player missed")
                    
                    hp -= 20
                    print("Bot did 20 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 == 90:
                    print("Player missed")
                    hp -= 50
                    
                    print("Bot did 50 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 > 20:
                    print("Player missed")
                    
                    hp -= 10
                    print("Bot did 10 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 < 90:
                    print("Player missed")
                  
                    print("Bot did 0 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
            elif choice2 == 2:
                if dtr2 > 90:
                    print("Player missed")
          
                    print("Bot did 0 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 < 90 and dtr >= 80:
                    print("Player missed")
            
                    hp -= 10
                    print("Bot did 10 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 == 1:
                    print("Player stole 50hp from the Bot!")
                    hp2 -= 50
                    hp -= 100
                    print("Bot did 100 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                    
                else:
                    print("Player missed")
                    
                    hp -= 20
                    print("Bot did 20 dmg to Player")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

            elif choice2 == 3:
                if dtr2>10:
                    print("Bot digged into the ground!")
                    print("Your Attack missed!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2<=10:
                    print("Bot failed to dig!")
                    print("Your missed")
                  
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
            elif choice2 == 4:
                if dtr2 > 50:
                    print("Your missed")
                    print("Bot healed 10 hp")
                    hp2 += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                elif dtr2 <= 50:
                    print("Your missed")
                    print("Bot did 2 dmg to the player")
                    
                    hp -= 2
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
            elif choice2 == 5:
                #when bot and player choice 5, where player gets 80% chance (no steal).
                if dtr2>95:
                    print("Bot stole 50hp and player missed!")
                    hp -= 50
                    hp2 += 50
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)
                    
                elif dtr2>80:
                    print("Bot stole 10hp and player missed!")
                    hp -= 10
                    hp2 += 10
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                elif dtr2<80:
                    print("Both missed!")
                    print("Your hp is:")
                    print(hp)
                    print("The enemy's hp is:")
                    print(hp2)

                else:
                    print("hakerman")
                    print(hp)
                    print(hp2)


                
    else:
        print("Please do not input anything whether a space, or a letter.")
        print("Please input 1, 2, 3, 4 or 5. (The number only)")

if hp < 0 and hp < hp2:
    print("Bot has won the game!")
elif hp2 < 0 and hp < hp2:
    print("Bot has won the game!")
else:
    print("You have won the game!")



