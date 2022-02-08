import random
import json

#HEADER

class Loot:
    def __init__(self, position, name, add_damage, add_health, count):
        self.position = position
        self.name = name
        self.add_damage = add_damage
        self.add_health = add_health
        self.count = count
        global potion_health, potion_strength, new_sword, knife, stylish_hat, patent_shoes, knitted_mittens, nothing_loot

potion_health = Loot(1, "potion of health", 0, 30, 5)
potion_strength = Loot(2, "potion of strength", 3, 0, 0)
new_sword = Loot(3, "new sword", 2, 0, 0)
knife = Loot(4, "knife", 1, 0, 0)
stylish_hat = Loot(5, "stylish hat", 0, 3, 0)
patent_shoes = Loot(6, "patent shoes", 0, 5, 0)
knitted_mittens = Loot(7, "knitted mittens", 0, 1, 0)
nothing_loot = Loot(8, "nothing", 0, 0, 0)

looting = [potion_health.name,      
           potion_strength.name,
           new_sword.name,
           knife.name,
           stylish_hat.name,
           patent_shoes.name,
           knitted_mittens.name,
           nothing_loot.name,
           nothing_loot.name,
           nothing_loot.name,
           nothing_loot.name,
           nothing_loot.name,
           nothing_loot.name]

backpack = [(str(potion_health.position) + ". " + potion_health.name + " x" + str(potion_health.count)),
            (str(potion_strength.position) + ". " + potion_strength.name + " x" + str(potion_strength.count)),
            (str(new_sword.position) + ". " + new_sword.name + " x" + str(new_sword.count)),
            (str(knife.position) + ". " + knife.name + " x" + str(knife.count)),
            (str(stylish_hat.position) + ". " + stylish_hat.name + " x" + str(stylish_hat.count)),
            (str(patent_shoes.position) + ". " + patent_shoes.name + " x" + str(patent_shoes.count)),
            (str(knitted_mittens.position) + ". " + knitted_mittens.name + " x" + str(knitted_mittens.count))]

def show_backpack():
    global backpack, potion_health, potion_strength, new_sword, knife, stylish_hat, patent_shoes, knitted_mittens
    backpack = [(str(potion_health.position) + ". " + potion_health.name + " x" + str(potion_health.count)),
            (str(potion_strength.position) + ". " + potion_strength.name + " x" + str(potion_strength.count)),
            (str(new_sword.position) + ". " + new_sword.name + " x" + str(new_sword.count)),
            (str(knife.position) + ". " + knife.name + " x" + str(knife.count)),
            (str(stylish_hat.position) + ". " + stylish_hat.name + " x" + str(stylish_hat.count)),
            (str(patent_shoes.position) + ". " + patent_shoes.name + " x" + str(patent_shoes.count)),
            (str(knitted_mittens.position) + ". " + knitted_mittens.name + " x" + str(knitted_mittens.count))]
    print("\nYour backpack contain", len(backpack), item_word +":")
    for item in backpack:
        print(item)

hero_health_max = 100
hero_health = 100
hero_damage = random.randint(6,14)
hero_damage_add = 0
hero_damage_summ = hero_damage + hero_damage_add

direction = ["forward",
             "right",
             "backward",
             "left"]

item_word = ""
if len(backpack) == 1:
    item_word = "item"
else: 
    item_word = "items"

actions = ["1. backpack",
           "2. healing",
           "3. move",
           "4. save",
           "5. load",
           "6. quit"]

leave_choose = ""
def leave_input():
    global leave_choose
    leave_choose = input("Are you shure want to leave game?(y/n)\n>>> ").lower()
    return leave_choose

class Creatures:
  def __init__(self, name, health, damage, health_default):
    self.name = name
    self.health = health
    self.damage = damage
    self.health_default = health_default

ghoul = Creatures("ghoul", 30, random.randint(7,13), 30)
rat = Creatures("rat", 7, random.randint(2,5), 7)
mutated_rat = Creatures("mutated rat", 12, random.randint(2,10), 12)
feral_cat = Creatures("feral cat", 15, random.randint(4,10), 15)
feral_dog = Creatures("feral dog", 17, random.randint(4,10), 17)
mutated_snake = Creatures("mutated snake", 10, random.randint(1,9), 10)
coyote = Creatures("coyote", 20, random.randint(6,12), 20)
scorpion = Creatures("scorpion", 28, random.randint(8,16), 28)

happenings = [ghoul.name, 
              rat.name,
              mutated_rat.name,
              feral_cat.name,
              feral_dog.name,
              mutated_snake.name,
              coyote.name,
              scorpion.name,
              "someone's cache",
              "an broken house",
              "nothing",
              "nothing",
              "nothing",
              "nothing",
              "nothing"]

current_action = "beginning"

def winning_info():
    global current_happening
    print("You win " + current_happening + ". ")
    health_info()

def found_info():
    global current_happening
    global current_looting
    print("You found " + current_happening + ". There was " + current_looting + ". It's added to your backpack")
    
def health_info():
    global hero_health
    global hero_health_max
    print("Your health: {}".format(hero_health) + "/" + "{}".format(hero_health_max))

def return_damage():
    global ghoul, rat, mutated_rat, feral_cat, feral_dog, mutated_snake, coyote, scorpion, hero_damage, hero_damage_add, hero_damage_summ
    ghoul.damage = random.randint(7,13)
    rat.damage = random.randint(2,5)
    mutated_rat.damage = random.randint(2,10)
    feral_cat.damage = random.randint(4,10)
    feral_dog.damage = random.randint(4,10)
    mutated_snake.damage = random.randint(1,9)
    coyote.damage = random.randint(6,12)
    scorpion.damage = random.randint(8,16)
    hero_damage = random.randint(6,14)
    hero_damage_summ = hero_damage + hero_damage_add
    
def healing():
    global hero_health, hero_health_max, potion_health, backpack
    if (hero_health < hero_health_max and potion_health.count > 0):
        if (hero_health + potion_health.add_health) >= hero_health_max:
            hero_health = hero_health_max
            potion_health.count = potion_health.count -1
        else:
            hero_health += potion_health.add_health
            potion_health.count = potion_health.count -1  
            print("\nYou have been healed.")
            health_info()
    elif (hero_health < hero_health_max and potion_health.count < 1):
        print("\nYou don't have potion of health")
    else:
        print("\nYou don't need to be healed")
        
def save_game():
    global hero_health, hero_health_max, potion_health, potion_strength, new_sword, knife, stylish_hat, patent_shoes, knitted_mittens
    saving = {
        "hero_health" : hero_health,
        "hero_health_max" : hero_health_max,
        "potion_health.count" : potion_health.count,
        "potion_strength.count" : potion_strength.count,
        "new_sword.count" : new_sword.count,
        "knife.count" : knife.count,
        "stylish_hat.count" : stylish_hat.count,
        "patent_shoes.count" : patent_shoes.count,
        "knitted_mittens.count" : knitted_mittens.count
    } 
    json_object = json.dumps(saving, indent = 9)
    with open("save.sgptg", "w") as outfile:
        outfile.write(json_object)
    print("Your progress was succesfully saved")

def load_game():
    global hero_health, hero_health_max, potion_health, potion_strength, new_sword, knife, stylish_hat, patent_shoes, knitted_mittens
    try:
        with open('save.sgptg', 'r') as openfile:
            json_object = json.load(openfile)
            hero_health = json_object["hero_health"]
            hero_health_max = json_object["hero_health_max"]
            potion_health.count = json_object["potion_health.count"]
            potion_strength.count = json_object["potion_strength.count"]
            new_sword.count = json_object["new_sword.count"]
            knife.count = json_object["knife.count"]
            stylish_hat.count = json_object["stylish_hat.count"]
            patent_shoes.count = json_object["patent_shoes.count"]
            knitted_mittens.count = json_object["knitted_mittens.count"]
        print("Your progress was succesfully loaded")
    except FileNotFoundError:
       print("You don't have any savings")
    except:
        print("Oops! Something went wrong...")        


#MAIN


print("""
       _____________________________________
       |          HERO - petgame           | 
       |          Try to survive           |
       | Explore the area, fight creatures |
       |                                   |
       |      created by @eugene937        |
       ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾""")

while hero_health > 0:              #main menu cycle
    print("\n")
    health_info()
    print("\nWhat do you want to do? Available actions: ")
    for item in actions:
        print(item)
    current_action = input("\n>>> ").lower()

    if current_action == "quit" or current_action == "6":
        leave_input()  
        if leave_choose == "y":
            break
        elif leave_choose == "n":
            continue
    
    if current_action == "save" or current_action == "4":
        save_game()  
        
    if current_action == "load" or current_action == "5":
        load_game()

    while (current_action == "backpack" or current_action == "1") and hero_health > 0:              #backpack menu cycle
        show_backpack()
        print("Choose item to use or print \"back\" to leave backpack")
        backpack_choose = input("\n>>> ").lower()
        if backpack_choose == "back":
            break
        elif (backpack_choose == potion_health.name or backpack_choose == "{}".format(potion_health.position)):
            healing()
        elif (backpack_choose == potion_strength.name or backpack_choose == "{}".format(potion_strength.position)):
            if (potion_strength.count > 0):
                hero_damage_add += potion_strength.add_damage
                potion_strength.count -= 1
                print("\nYou feel stronger! Your damage was increased")
            elif (potion_strength.count < 1):
                print("\nYou don't have potion of strength")
        elif (backpack_choose == new_sword.name or backpack_choose == "{}".format(new_sword.position)):
            if (new_sword.count > 0):
                hero_damage_add += new_sword.add_damage
                new_sword.count -= 1
                print("\nYou look epic! Your damage was increased")
            elif (new_sword.count < 1):
                print("\nYou don't have any sword")
        elif (backpack_choose == knife.name or backpack_choose == "{}".format(knife.position)):
            if (knife.count > 0):
                hero_damage_add += knife.add_damage
                knife.count -= 1
                print("\nYou look scary! Your damage was increased")
            elif (knife.count < 1):
                print("\nYou don't have any knife")
        elif (backpack_choose == stylish_hat.name or backpack_choose == "{}".format(stylish_hat.position)):
            if (stylish_hat.count > 0):
                hero_health_max += stylish_hat.add_health
                stylish_hat.count -= 1
                print("\nYou look cool! Your health was increased")
            elif (stylish_hat.count < 1):
                print("\nYou don't have any hat")
        elif (backpack_choose == patent_shoes.name or backpack_choose == "{}".format(patent_shoes.position)):
            if (patent_shoes.count > 0):
                hero_health_max += patent_shoes.add_health
                patent_shoes.count -= 1
                print("\nNice shoes! Your health was increased")
            elif (patent_shoes.count < 1):
                print("\nYou don't have any shoes")
        elif (backpack_choose == knitted_mittens.name or backpack_choose == "{}".format(knitted_mittens.position)):
            if (knitted_mittens.count > 0):
                hero_health_max += knitted_mittens.add_health
                knitted_mittens.count -= 1
                print("\nOooh, that's so cute! Your health was increased")
            elif (knitted_mittens.count < 1):
                print("\nYou don't have any mittens")
        else:
            print("There is no such item")

    if (current_action == "healing" or current_action == "heal" or current_action == "2") and hero_health > 0:              #healing menu cycle
        healing()

    while (current_action == "move" or current_action == "3") and hero_health > 0:              #moving menu cycle
        print("\nAvailable directions:")
        for item in direction:
            print(item)
        print("Choose direction or print \"back\" to leave direction menu")
        direction_choose = input("\n>>>").lower()

        if direction_choose == "back":
            print("You choose to stay here for a while")
            break

        elif direction_choose in direction:
            print("You have moved {}".format(direction_choose))
            current_happening = random.choice(happenings)
            match current_happening:
                case ghoul.name:
                    print("You will have a fight with {}!".format(current_happening))
                    while (current_happening == happenings[0] and ghoul.health > 0 and hero_health > 0):
                        return_damage()
                        hero_health -= ghoul.damage
                        ghoul.health -= hero_damage_summ
                        if hero_health < 1:
                            print("\n{} damage you {} points!".format(current_happening, ghoul.damage))
                            print("{} killed you\n".format(current_happening))
                            break
                        elif ghoul.health < 1:
                            print("\n{} damage you {} points! ".format(current_happening, ghoul.damage))
                            health_info()
                            print("\nYou damage {} {} points! ".format(current_happening, hero_damage_summ))                        
                            winning_info()
                            input("\npress Enter to continue")
                            break
                        else:
                            print("\n{} damage you {} points! ".format(current_happening, ghoul.damage))
                            health_info()
                            print("\nYou damage {} {} points!".format(current_happening, hero_damage_summ))
                            input("\npress Enter to attack")
                            continue
                    ghoul.health = ghoul.health_default
                case rat.name:
                    print("You will have a fight with {}!".format(current_happening))
                    while (current_happening == happenings[1] and rat.health > 0 and hero_health > 0):
                        return_damage()
                        hero_health -= rat.damage
                        rat.health -= hero_damage
                        if hero_health < 1:
                            print("\n{} damage you {} points!".format(current_happening, rat.damage))
                            print("{} killed you\n".format(current_happening))
                            break
                        elif rat.health < 1:
                            print("\n{} damage you {} points! ".format(current_happening, rat.damage))
                            health_info()
                            print("\nYou damage {} {} points! ".format(current_happening, hero_damage_summ))                        
                            winning_info()
                            input("\npress Enter to continue")
                            break
                        else:
                            print("\n{} damage you {} points! ".format(current_happening, rat.damage))
                            health_info()
                            print("\nYou damage {} {} points!".format(current_happening, hero_damage_summ))
                            input("\npress Enter to attack")
                            continue
                    rat.health = rat.health_default
                case mutated_rat.name:
                    print("You will have a fight with {}!".format(current_happening))
                    while (current_happening == happenings[2] and mutated_rat.health > 0 and hero_health > 0):
                        return_damage()
                        hero_health -= mutated_rat.damage
                        mutated_rat.health -= hero_damage
                        if hero_health < 1:
                            print("\n{} damage you {} points!".format(current_happening, mutated_rat.damage))
                            print("{} killed you\n".format(current_happening))
                            break
                        elif mutated_rat.health < 1:
                            print("\n{} damage you {} points! ".format(current_happening, mutated_rat.damage))
                            health_info()
                            print("\nYou damage {} {} points! ".format(current_happening, hero_damage_summ))                        
                            winning_info()
                            input("\npress Enter to continue")
                            break
                        else:
                            print("\n{} damage you {} points! ".format(current_happening, mutated_rat.damage))
                            health_info()
                            print("\nYou damage {} {} points!".format(current_happening, hero_damage_summ))
                            input("\npress Enter to attack")
                            continue
                    mutated_rat.health = mutated_rat.health_default
                case feral_cat.name:
                    print("You will have a fight with {}!".format(current_happening))
                    while (current_happening == happenings[3] and feral_cat.health > 0 and hero_health > 0):
                        return_damage()                    
                        hero_health -= feral_cat.damage
                        feral_cat.health -= hero_damage
                        if hero_health < 1:
                            print("\n{} damage you {} points!".format(current_happening, feral_cat.damage))
                            print("{} killed you\n".format(current_happening))
                            break
                        elif feral_cat.health < 1:
                            print("\n{} damage you {} points! ".format(current_happening, feral_cat.damage))
                            health_info()
                            print("\nYou damage {} {} points! ".format(current_happening, hero_damage_summ))                        
                            winning_info()
                            input("\npress Enter to continue")
                            break
                        else:
                            print("\n{} damage you {} points! ".format(current_happening, feral_cat.damage))
                            health_info()
                            print("\nYou damage {} {} points!".format(current_happening, hero_damage_summ))
                            input("\npress Enter to attack")
                            continue
                    feral_cat.health = feral_cat.health_default
                case feral_dog.name:
                    print("You will have a fight with {}!".format(current_happening))
                    while (current_happening == happenings[4] and feral_dog.health > 0 and hero_health > 0):
                        return_damage()
                        hero_health -= feral_dog.damage
                        feral_dog.health -= hero_damage
                        if hero_health < 1:
                            print("\n{} damage you {} points!".format(current_happening, feral_dog.damage))
                            print("{} killed you\n".format(current_happening))
                            break
                        elif feral_dog.health < 1:
                            print("\n{} damage you {} points! ".format(current_happening, feral_dog.damage))
                            health_info()
                            print("\nYou damage {} {} points! ".format(current_happening, hero_damage_summ))                        
                            winning_info()
                            input("\npress Enter to continue")
                            break
                        else:
                            print("\n{} damage you {} points! ".format(current_happening, feral_dog.damage))
                            health_info()
                            print("\nYou damage {} {} points!".format(current_happening, hero_damage_summ))
                            input("\npress Enter to attack")
                            continue
                    feral_dog.health = feral_dog.health_default
                case mutated_snake.name:
                    print("You will have a fight with {}!".format(current_happening))
                    while (current_happening == happenings[5] and mutated_snake.health > 0 and hero_health > 0):
                        return_damage()
                        hero_health -= mutated_snake.damage
                        mutated_snake.health -= hero_damage
                        if hero_health < 1:
                            print("\n{} damage you {} points!".format(current_happening, mutated_snake.damage))
                            print("{} killed you\n".format(current_happening))
                            break
                        elif mutated_snake.health < 1:
                            print("\n{} damage you {} points! ".format(current_happening, mutated_snake.damage))
                            health_info()
                            print("\nYou damage {} {} points! ".format(current_happening, hero_damage_summ))                        
                            winning_info()
                            input("\npress Enter to continue")
                            break
                        else:
                            print("\n{} damage you {} points! ".format(current_happening, mutated_snake.damage))
                            health_info()
                            print("\nYou damage {} {} points!".format(current_happening, hero_damage_summ))
                            input("\npress Enter to attack")
                            continue
                    mutated_snake.health = mutated_snake.health_default
                case coyote.name:
                    print("You will have a fight with {}!".format(current_happening))
                    while (current_happening == happenings[6] and coyote.health > 0 and hero_health > 0):
                        return_damage()
                        hero_health -= coyote.damage
                        coyote.health -= hero_damage
                        if hero_health < 1:
                            print("\n{} damage you {} points!".format(current_happening, coyote.damage))
                            print("{} killed you\n".format(current_happening))
                            break
                        elif coyote.health < 1:
                            print("\n{} damage you {} points! ".format(current_happening, coyote.damage))
                            health_info()
                            print("\nYou damage {} {} points! ".format(current_happening, hero_damage_summ))                        
                            winning_info()
                            input("\npress Enter to continue")
                            break
                        else:
                            print("\n{} damage you {} points! ".format(current_happening, coyote.damage))
                            health_info()
                            print("\nYou damage {} {} points!".format(current_happening, hero_damage_summ))
                            input("\npress Enter to attack")
                            continue
                    coyote.health = coyote.health_default
                case scorpion.name:
                    print("You will have a fight with {}!".format(current_happening))
                    while (current_happening == happenings[7] and scorpion.health > 0 and hero_health > 0):
                        return_damage()
                        hero_health -= scorpion.damage
                        scorpion.health -= hero_damage
                        if hero_health < 1:
                            print("\n{} damage you {} points!".format(current_happening, scorpion.damage))
                            print("{} killed you\n".format(current_happening))
                            break
                        elif scorpion.health < 1:
                            print("\n{} damage you {} points! ".format(current_happening, scorpion.damage))
                            health_info()
                            print("\nYou damage {} {} points! ".format(current_happening, hero_damage_summ))                        
                            winning_info()
                            input("\npress Enter to continue")
                            break
                        else:
                            print("\n{} damage you {} points! ".format(current_happening, scorpion.damage))
                            health_info()
                            print("\nYou damage {} {} points!".format(current_happening, hero_damage_summ))
                            input("\npress Enter to attack")
                            continue
                    scorpion.health = scorpion.health_default
                case ("someone's cache" | "an broken house"):
                    current_looting = random.choice(looting)
                    match current_looting:
                        case potion_health.name:
                            potion_health.count += 1
                            found_info()
                        case potion_strength.name:
                            potion_strength.count += 1
                            found_info()
                        case new_sword.name:
                            new_sword.count += 1
                            found_info()
                        case knife.name:
                            knife.count += 1
                            found_info()
                        case stylish_hat.name:
                            stylish_hat.count += 1
                            found_info()
                        case patent_shoes.name:
                            patent_shoes.count += 1
                            found_info()
                        case knitted_mittens.name:
                            knitted_mittens.count += 1
                            found_info()
                        case nothing_loot.name:
                            print("You found " + current_happening + ". There was " + current_looting)
                case ("nothing"):
                    print("There is " + current_happening + " in this place")
        else:
            print("There is no such direction")

input("Press Enter again to leave")