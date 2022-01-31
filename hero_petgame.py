import random

potion_health_counter = 3
potion_health = "potion of health x"+str(potion_health_counter)

backpack = [potion_health,
"item2",
"item3",]

hero_health = 70
hero_damage = 10

direction = ["forward",
"right",
"backward",
"left"]

item_word = ""
if len(backpack) == 1:
    item_word = "item"
else: 
    item_word = "items"

actions = ["backpack",
"healing",
"move",
"quit"]

ghoul_name = "ghoul"
ghoul_health = 30
ghoul_damage = 12
ghoul = [ghoul_name,
         ghoul_health,
         ghoul_damage]

rat_name = "rat"
rat_health = 7
rat_damage = 3
rat = [rat_name,
       rat_health,
       rat_damage]

mutated_rat_name = "mutated rat"
mutated_rat_health = 12
mutated_rat_damage = 6
mutated_rat = [mutated_rat_name,
               mutated_rat_health,
               mutated_rat_damage]

feral_cat_name = "feral cat"
feral_cat_health = 15
feral_cat_damage = 8
feral_cat = [feral_cat_name,
             feral_cat_health,
             feral_cat_damage]

feral_dog_name = "feral dog"
feral_dog_health = 17
feral_dog_damage = 8
feral_dog = [feral_dog_name,
             feral_dog_health,
             feral_dog_damage]

mutated_snake_name = "mutated snake"
mutated_snake_health = 10
mutated_snake_damage = 5
mutated_snake = [mutated_snake_name,
                 mutated_snake_health,
                 mutated_snake_damage]

coyote_name = "coyote"
coyote_health = 20
coyote_damage = 10
coyote = [coyote_name,
          coyote_health,
          coyote_damage]

scorpion_name = "scorpion"
scorpion_health = 28
scorpion_damage = 14
scorpion = [scorpion_name,
            scorpion_health,
            scorpion_damage]

happenings = [ghoul[0], 
              rat[0],
              mutated_rat[0],
              feral_cat[0],
              feral_dog[0],
              mutated_snake[0],
              coyote[0],
              scorpion[0],
              "someone's cache",
              "an broken house",
              "nothing"]

current_action = "beginning"

while current_action != "quit" and current_action != "" and hero_health > 0:                        #main menu cycle
    print("\nYour health:", str(hero_health) +"/100")
    print("What do you want to do? Available actions: ")
    for item in actions:
        print(item)
    current_action = input("\n>>> ")

    while current_action == "backpack":                                         #backpack menu cycle
        print("\nYour backpack contain", len(backpack), item_word +":")
        for item in backpack:
            print(item)
        print("Choose item to use or print \"back\" to leave backpack")
        backpack_choose = input("\n>>>")
        if backpack_choose == "back":
            break

    if current_action == "healing":                                             #healing menu cycle
        if (hero_health < 100 and potion_health_counter > 0):
            hero_health = 100
            potion_health_counter = potion_health_counter -1  
            print("\nYou have been healed")
            backpack[0] = "potion of health x"+str(potion_health_counter)
        elif (hero_health < 100 and potion_health_counter < 1):
            print("\nYou don't have potion of health")
        else:
            print("\nYou don't need to be healed")

    while current_action == "move" and hero_health > 0:                                             #moving menu cycle
        print("\nAvailable direction:")
        for item in direction:
            print(item)
        print("Choose direction or print \"back\" to leave direction menu")
        direction_choose = input("\n>>>")

        if direction_choose == "back":
            print("You choose to stay here for a while")
            break

        elif direction_choose == direction[0]:                                  #move forward
            print("You have moved", direction[0])
            current_happening = random.choice(happenings)
            if current_happening == happenings[0]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[0] and ghoul_health > 0 and hero_health > 0):
                    hero_health -= ghoul_damage
                    print("\n" + current_happening + " damage you "+ str(str(ghoul_damage)) + " points! Your health now is " + str(hero_health) + "/100")
                    ghoul_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if ghoul_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[1]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[1] and rat_health > 0 and hero_health > 0):
                    hero_health -= rat_damage
                    print("\n" + current_happening + " damage you "+ str(rat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    rat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if rat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[2]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[2] and mutated_rat_health > 0 and hero_health > 0):
                    hero_health -= mutated_rat_damage
                    print("\n" + current_happening + " damage you "+ str(mutated_rat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    mutated_rat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if mutated_rat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[3]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[3] and feral_cat_health > 0 and hero_health > 0):
                    hero_health -= feral_cat_damage
                    print("\n" + current_happening + " damage you "+ str(feral_cat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    feral_cat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if feral_cat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[4]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[4] and feral_dog_health > 0 and hero_health > 0):
                    hero_health -= feral_dog_damage
                    print("\n" + current_happening + " damage you "+ str(feral_dog_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    feral_dog_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if feral_dog_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[5]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[5] and mutated_snake_health > 0 and hero_health > 0):
                    hero_health -= mutated_snake_damage
                    print("\n" + current_happening + " damage you "+ str(mutated_snake_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    mutated_snake_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if mutated_snake_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[6]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[6] and coyote_health > 0 and hero_health > 0):
                    hero_health -= coyote_damage
                    print("\n" + current_happening + " damage you "+ str(coyote_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    coyote_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if coyote_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[7]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[7] and scorpion_health > 0 and hero_health > 0):
                    hero_health -= scorpion_damage
                    print("\n" + current_happening + " damage you "+ str(scorpion_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    scorpion_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if scorpion_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif (current_happening == happenings[8]
               or current_happening == happenings[9]):    
                print("You found " + current_happening)
            elif current_happening == happenings[10]:    
                print("There is " + current_happening + " in this place")

        elif direction_choose == direction[1]:                                  #move right
            print("You have moved", direction[1])
            current_happening = random.choice(happenings)
            if current_happening == happenings[0]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[0] and ghoul_health > 0 and hero_health > 0):
                    hero_health -= ghoul_damage
                    print("\n" + current_happening + " damage you "+ str(ghoul_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    ghoul_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if ghoul_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[1]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[1] and rat_health > 0 and hero_health > 0):
                    hero_health -= rat_damage
                    print("\n" + current_happening + " damage you "+ str(rat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    rat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if rat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[2]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[2] and mutated_rat_health > 0 and hero_health > 0):
                    hero_health -= mutated_rat_damage
                    print("\n" + current_happening + " damage you "+ str(mutated_rat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    mutated_rat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if mutated_rat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[3]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[3] and feral_cat_health > 0 and hero_health >0):
                    hero_health -= feral_cat_damage
                    print("\n" + current_happening + " damage you "+ str(feral_cat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    feral_cat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if feral_cat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[4]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[4] and feral_dog_health > 0 and hero_health >0):
                    hero_health -= feral_dog_damage
                    print("\n" + current_happening + " damage you "+ str(feral_dog_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    feral_dog_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if feral_dog_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[5]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[5] and mutated_snake_health > 0 and hero_health >0):
                    hero_health -= mutated_snake_damage
                    print("\n" + current_happening + " damage you "+ str(mutated_snake_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    mutated_snake_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if mutated_snake_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[6]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[6] and coyote_health > 0 and hero_health >0):
                    hero_health -= coyote_damage
                    print("\n" + current_happening + " damage you "+ str(coyote_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    coyote_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if coyote_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[7]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[7] and scorpion_health > 0 and hero_health >0):
                    hero_health -= scorpion_damage
                    print("\n" + current_happening + " damage you "+ str(scorpion_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    scorpion_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if scorpion_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif (current_happening == happenings[8]
               or current_happening == happenings[9]):    
                print("You found " + current_happening)
            elif current_happening == happenings[10]:    
                print("There is " + current_happening + " in this place")

        elif direction_choose == direction[2]:                                  #move backward
            print("You have moved", direction[2])
            current_happening = random.choice(happenings)
            if current_happening == happenings[0]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[0] and ghoul_health > 0 and hero_health >0):
                    hero_health -= ghoul_damage
                    print("\n" + current_happening + " damage you "+ str(ghoul_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    ghoul_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if ghoul_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[1]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[1] and rat_health > 0 and hero_health >0):
                    hero_health -= rat_damage
                    print("\n" + current_happening + " damage you "+ str(rat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    rat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if rat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[2]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[2] and mutated_rat_health > 0 and hero_health >0):
                    hero_health -= mutated_rat_damage
                    print("\n" + current_happening + " damage you "+ str(mutated_rat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    mutated_rat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if mutated_rat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[3]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[3] and feral_cat_health > 0 and hero_health >0):
                    hero_health -= feral_cat_damage
                    print("\n" + current_happening + " damage you "+ str(feral_cat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    feral_cat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if feral_cat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[4]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[4] and feral_dog_health > 0 and hero_health >0):
                    hero_health -= feral_dog_damage
                    print("\n" + current_happening + " damage you "+ str(feral_dog_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    feral_dog_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if feral_dog_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[5]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[5] and mutated_snake_health > 0 and hero_health >0):
                    hero_health -= mutated_snake_damage
                    print("\n" + current_happening + " damage you "+ str(mutated_snake_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    mutated_snake_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if mutated_snake_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[6]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[6] and coyote_health > 0 and hero_health >0):
                    hero_health -= coyote_damage
                    print("\n" + current_happening + " damage you "+ str(coyote_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    coyote_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if coyote_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[7]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[7] and scorpion_health > 0 and hero_health >0):
                    hero_health -= scorpion_damage
                    print("\n" + current_happening + " damage you "+ str(scorpion_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    scorpion_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if scorpion_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif (current_happening == happenings[8]
               or current_happening == happenings[9]):    
                print("You found " + current_happening)
            elif current_happening == happenings[10]:    
                print("There is " + current_happening + " in this place")

        elif direction_choose == direction[3]:                                  #move left
            print("You have moved", direction[3])
            current_happening = random.choice(happenings)
            if current_happening == happenings[0]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[0] and ghoul_health > 0 and hero_health >0):
                    hero_health -= ghoul_damage
                    print("\n" + current_happening + " damage you "+ str(ghoul_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    ghoul_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if ghoul_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[1]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[1] and rat_health > 0 and hero_health >0):
                    hero_health -= rat_damage
                    print("\n" + current_happening + " damage you "+ str(rat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    rat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if rat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[2]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[2] and mutated_rat_health > 0 and hero_health >0):
                    hero_health -= mutated_rat_damage
                    print("\n" + current_happening + " damage you "+ str(mutated_rat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    mutated_rat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if mutated_rat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[3]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[3] and feral_cat_health > 0 and hero_health >0):
                    hero_health -= feral_cat_damage
                    print("\n" + current_happening + " damage you "+ str(feral_cat_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    feral_cat_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if feral_cat_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[4]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[4] and feral_dog_health > 0 and hero_health >0):
                    hero_health -= feral_dog_damage
                    print("\n" + current_happening + " damage you "+ str(feral_dog_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    feral_dog_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if feral_dog_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[5]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[5] and mutated_snake_health > 0 and hero_health >0):
                    hero_health -= mutated_snake_damage
                    print("\n" + current_happening + " damage you "+ str(mutated_snake_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    mutated_snake_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if mutated_snake_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[6]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[6] and coyote_health > 0 and hero_health >0):
                    hero_health -= coyote_damage
                    print("\n" + current_happening + " damage you "+ str(coyote_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    coyote_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if coyote_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif current_happening == happenings[7]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[7] and scorpion_health > 0 and hero_health >0):
                    hero_health -= scorpion_damage
                    print("\n" + current_happening + " damage you "+ str(scorpion_damage) + " points! Your health now is " + str(hero_health) + "/100")
                    scorpion_health -= hero_damage
                    print("\nYou damage " + current_happening + + str(hero_damage) + " points!")
                    if scorpion_health < 1:
                        print("You win " + current_happening + ". Your health now is " + str(hero_health) + "/100")
                        input("\npress any key to continue")
                        break
                    elif hero_health < 1:
                        print(current_happening + "killed you")
                        break
                    else:
                        input("\npress any key to continue")
                        continue
            elif (current_happening == happenings[8]
               or current_happening == happenings[9]):    
                print("You found " + current_happening)
            elif current_happening == happenings[10]:    
                print("There is " + current_happening + " in this place")

        else:
            continue

input("Press Enter again to leave")