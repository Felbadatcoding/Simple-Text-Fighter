#text fighter from s2 but better
#could use classes but i realised halfway and this basically is using classes without classes anyways

#modules
from random import randint

#variables init
hps = [100, 100] #index 1 = p1, index 0 = p2
digstates = [False, False] #index 1 = p1, index 0 = p2
turncount = 0
mult = [1,1] #index 1 = p1, index 0 = p2
PLAYERS = []
TUTORIALS = ["Kick. It has a 80% hit rate and deals 10 damage, there is a 10% chance that it will deal 20 damage and a 1% chance that it will deal 50 damage.",
             "Punch. It has a 90% hit rate and deals 5 damage, there is a 10% chance that it will deal 10 damage and a 1% chance it will deal 60 damage.",
             "Dig. It has a 90% success rate and it allows you to ignore the opponent's attack.",
            "Hatsune Miku. It has a 100% success rate. There is a 50% chance to heal 10 hp and a 50% chance to heal 15 hp.",
            "Steal. It has a 40% success rate. There is a 80% chance you will steal 10hp from the enemy and a 20% chance you will steal 20hp",
            "WE THE BEST MUSIC. 100% success rate, increase the effect of the next move by 50%(excluding dig)"
             ]
MOVES = ["kick", "punch", "dig", "hatsune miku", "steal", "we the best music"]

#moves
def getmove():
    move = input("please select a move: ")
    if move.isnumeric():
        print("isnum yes")
        if 0 < int(move) <= 5:
            return int(move)-1
    else:
        if move in MOVES:
            return MOVES.index(move)
        if move.lower() == "info":
            tutorialmove = input("The moves availabe are [1] Kick, [2] Punch, [3] Dig, [4] Hatsune Miku, [5] Steal, [6] WE THE BEST MUSIC. Which move would you like to learn about? Enter the number of the move or its name: ")
            if tutorialmove.isnumeric():
                tutorialmove = int(tutorialmove)
                if tutorialmove <= 5 and  tutorialmove >= 1:
                    print(TUTORIALS[int(tutorialmove)-1])
                else: 
                    move = input("no info availble")
            else:
                if tutorialmove.lower in MOVES:
                    print(TUTORIALS[MOVES.index(tutorialmove)])
                else:
                    move = input("no info availble")
    if move.lower() != "info":
        print("invalid input, try again.")
    getmove()


    
def kick(roll, turncount):
    if roll <= 80:
        if roll <= 10:
            print(f"{PLAYERS[turncount%2]} did 20 dmg to {PLAYERS[(turncount+1)%2]} with a kick!")
            return -20
        elif roll == 11:
            print(f"{PLAYERS[turncount%2]} did 50 dmg to {PLAYERS[(turncount+1)%2]} with a kick!")
            return -50
        else:
            print(f"{PLAYERS[turncount%2]} did 10 dmg to {PLAYERS[(turncount+1)%2]} with a kick!")
            return -10

    print("you missed!")
    return 0

def punch(roll, turncount):
    if roll <= 90:
        if roll <= 10:
            print(f"{PLAYERS[turncount%2]} did 10 dmg to {PLAYERS[(turncount+1)%2]} with a punch!")
            return -10
        elif roll == 11:
            print(f"{PLAYERS[turncount%2]} did 60 dmg to {PLAYERS[(turncount+1)%2]} with a punch!")
            return -60
        else:
            print(f"{PLAYERS[turncount%2]} did 5 dmg to {PLAYERS[(turncount+1)%2]} with a punch!")
            return -5

    print("you missed!")
    return 0

def dig(roll, playerturn):
    if roll <= 90:
        digstates[playerturn] = True
        print("You dug a hole! ")
    else:
        print("You tried to dig a hole but your shovel broke! Move failed. ")

def digcheck(ifdig, turncount, opp, dmg):
    if ifdig == True:
        if dmg != 0:
            print(f"{PLAYERS[(turncount+1)%2]} digged and dodged your attack ")
            
            return opp, not ifdig
        else:
            return opp, ifdig
    else:
        return opp + dmg, ifdig

def miku(roll, playerturn):
    if roll <= 50:
        print(f"{PLAYERS[playerturn]} gained 10 hp with the power of song!" )
        return 10
    else:
        print(f"{PLAYERS[playerturn]} gained 15 hp with the power of song!" )
        return 15

def steal(roll, ifdig, turncount, player, opp):
    if roll <= 40:
        if roll > 8:
            if ifdig == True:
                print(f"{PLAYERS[(turncount+1)%2]} digged and dodged your attack ")
                return player, opp
            else:
                print(f"{PLAYERS[turncount%2]} stole 10 hp from {PLAYERS[(turncount+1)%2]}!")
                return player+10, opp+10
        else:
            print(f"{PLAYERS[turncount%2]} stole 20 hp from {PLAYERS[(turncount+1)%2]}!")
            return player+20, opp+20
    print("you failed!")
    return player, opp

def wethebestmusic(mult):
    print("WE THE BEST MUSIC, next move has +50% effect")
    return mult*1.5

#game init
print("Welcome to Text Fighter!")

gametype = input("Do you want to play singleplayer or multiplayer[single/multi]? ").lower()
while (gametype != "single") and (gametype != "multi"):
    gametype = input("please enter a valid input[single/multi]: ").lower()
if gametype == "multi":
    PLAYERS = ["PLAYER 2", "PLAYER 1"]
else:
    PLAYERS = ["PLAYER","BOT"]
print("You will be fighting against a bot using moves.")
print("The moves you can choose are:")
print("")
print("1, Kick. It has a 80% hit rate and deals 10 damage, there is a 10% chance that it will deal 20 damage and a 1% chance that it will deal 50 damage.")
print("")
print("2, Punch. It has a 90% hit rate and deals 5 damage, there is a 10% chance that it will deal 10 damage and a 1% chance it will deal 60 damage.")
print("")
print("3, Dig. It has a 90% success rate and it allows you to ignore the oppponents's attack.")
print("")
print("4, Hatsune Miku. It has a 100% success rate. There is a 50% chance to heal 10 hp and a 50% chance to heal 15 hp.")
print("")
print("5, Steal. It has a 25% success rate. There is a 80% chance you will steal 10hp from the enemy and a 20% chance you will steal 20hp!")
print("")
print("6, WE THE BEST MUSIC. 100% success rate, increase the effect of the next move by 50%(excluding dig) \n")
print("Enter the move's corresponding number or its name to use it.")
print("------------------------------------------------------------------------")
print("Players start with 100hp. If you get to 0, you die!")
input("Press enter to start now!")
print("The game will begin now! \n")



while hps[0]*hps[1] > 0:
    turncount += 1
    playerturn = turncount % 2
    opp = (turncount+1) % 2
    roll = randint(1,100)
    print(f"{PLAYERS[1]} hp: {hps[1]}, {PLAYERS[0]} hp: {hps[0]} \n")
    
    print(PLAYERS[playerturn], "turn! \n")
    if gametype == "multi" or (gametype == "single" and playerturn == 0):
        print("type ""info"" to learn more about the moves")
        move = getmove()
        print(MOVES[move], "was chosen!")
        if move == 0:
            hps[opp], digstates[opp] = digcheck(digstates[opp], turncount, hps[opp], punch(roll, turncount)*mult[playerturn])
        elif move == 1:
            hps[opp], digstates[opp] = digcheck(digstates[opp], turncount, hps[opp],  punch(roll, turncount)*mult[playerturn])
        elif move == 2:
            dig(roll, playerturn)
        elif move == 3:
             hps[playerturn] += miku(roll, turncount)*mult[playerturn]
        elif move == 4:
            hps[playerturn], hps[opp % 2] = steal(roll, digstates[opp], turncount, hps[playerturn], hps[opp])
        elif move == 5:
            mult[playerturn] = wethebestmusic(mult[playerturn])
    else:
        move = randint(1,5)
        if move == 0:
            hps[opp], digstates[opp] = digcheck(digstates[opp], turncount, hps[opp] + punch(roll, turncount)*mult[playerturn])
        elif move == 1:
            hps[opp], digstates[opp] = digcheck(digstates[opp], turncount, hps[opp] + punch(roll, turncount)*mult[playerturn])
        elif move == 2:
            dig(roll, playerturn)
        elif move == 3:
             hps[playerturn] += miku(roll, playerturn)*mult[playerturn]
        elif move == 4:
            hps[playerturn], hps[opp % 2] = steal(roll, digstates[opp], turncount, hps[playerturn], hps[opp])
        elif move == 5:
            mult[playerturn] = wethebestmusic(mult[playerturn])


    print("------------------------------------------------------------------------")

        
    




    

    
    

