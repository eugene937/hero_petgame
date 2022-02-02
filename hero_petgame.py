import random

#HEADER

class Loot:
    def __init__(self, name, add_damage, add_health, count):
        self.name = name
        self.add_damage = add_damage
        self.add_health = add_health
        self.count = count
        global potion_health
        global potion_strength
        global new_sword
        global knife
        global stylish_hat
        global patent_shoes
        global knitted_mittens
        global nothing_loot

potion_health = Loot("potion of health", 0, 30, 5)
potion_strength = Loot("potion of strength", 3, 0, 0)
new_sword = Loot("new sword", 2, 0, 0)
knife = Loot("knife", 1, 0, 0)
stylish_hat = Loot("stylish hat", 0, 3, 1)
patent_shoes = Loot("patent shoes", 0, 5, 1)
knitted_mittens = Loot("knitted mittens", 0, 1, 1)
nothing_loot = Loot("nothing", 0, 0, 0)

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

backpack = [(potion_health.name + " x" + str(potion_health.count)),
            (potion_strength.name + " x" + str(potion_strength.count)),
            (new_sword.name + " x" + str(new_sword.count)),
            (knife.name + " x" + str(knife.count)),
            (stylish_hat.name + " x" + str(stylish_hat.count)),
            (patent_shoes.name + " x" + str(patent_shoes.count)),
            (knitted_mittens.name + " x" + str(knitted_mittens.count))]

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

actions = ["backpack",
"healing",
"move",
"quit"]

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

def health_info():
    global hero_health
    global hero_health_max
    print("Your health:", str(hero_health) + "/" + str(hero_health_max))

def winning_info():
    global current_happening
    print("You win " + current_happening + ". ")
    health_info()

print("\n       _____________________________________\n       |          HERO - petgame           |\n       |          Try to survive           |\n       | Explore the area, fight creatures |\n       |                                   |\n       |      created by @eugene937.       |\n       ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

while current_action != "quit" and current_action != "" and hero_health > 0:                               #main menu cycle
    print("\n")
    health_info()
    print("\nWhat do you want to do? Available actions: ")
    for item in actions:
        print(item)
    current_action = input("\n>>> ").lower()
    

    while current_action == actions[0] and hero_health > 0:                                                                    #backpack menu cycle
        backpack = [(potion_health.name + " x" + str(potion_health.count)),
            (potion_strength.name + " x" + str(potion_strength.count)),
            (new_sword.name + " x" + str(new_sword.count)),
            (knife.name + " x" + str(knife.count)),
            (stylish_hat.name + " x" + str(stylish_hat.count)),
            (patent_shoes.name + " x" + str(patent_shoes.count)),
            (knitted_mittens.name + " x" + str(knitted_mittens.count))]
        print("\nYour backpack contain", len(backpack), item_word +":")
        for item in backpack:
            print(item)
        print("Choose item to use or print \"back\" to leave backpack")
        backpack_choose = input("\n>>>").lower()
        if backpack_choose == "back":
            break
        elif backpack_choose == potion_health.name:
            if (hero_health < hero_health_max and potion_health.count > 0):
                if (hero_health + potion_health.add_health) >= hero_health_max:
                    hero_health = hero_health_max
                    potion_health.count = potion_health.count -1
                else:
                    hero_health += potion_health.add_health
                    potion_health.count = potion_health.count -1  
                print("\nYou have been healed.")
                health_info()
                backpack[0] = (potion_health.name + " x" + str(potion_health.count))
            elif (hero_health < hero_health_max and potion_health.count < 1):
                print("\nYou don't have potion of health")
            else:
                print("\nYou don't need to be healed")
        elif backpack_choose == potion_strength.name:
            if (potion_strength.count > 0):
                hero_damage_add += potion_strength.add_damage
                potion_strength.count -= 1
                print("\nYou feel stronger! Your damage was increased")
                backpack[1] = (potion_strength.name + " x" + str(potion_strength.count))
            elif (potion_strength.count < 1):
                print("\nYou don't have potion of strength")
        elif backpack_choose == new_sword.name:
            if (new_sword.count > 0):
                hero_damage_add += new_sword.add_damage
                new_sword.count -= 1
                print("\nYou look epic! Your damage was increased")
                backpack[2] = (new_sword.name + " x" + str(new_sword.count))
            elif (new_sword.count < 1):
                print("\nYou don't have any sword")
        elif backpack_choose == knife.name:
            if (knife.count > 0):
                hero_damage_add += knife.add_damage
                knife.count -= 1
                print("\nYou look scary! Your damage was increased")
                backpack[3] = (knife.name + " x" + str(knife.count))
            elif (knife.count < 1):
                print("\nYou don't have any knife")
        elif backpack_choose == stylish_hat.name:
            if (stylish_hat.count > 0):
                hero_health_max += stylish_hat.add_health
                stylish_hat.count -= 1
                print("\nYou look cool! Your health was increased")
                backpack[4] = (stylish_hat.name + " x" + str(stylish_hat.count))
            elif (stylish_hat.count < 1):
                print("\nYou don't have any hat")
        elif backpack_choose == patent_shoes.name:
            if (patent_shoes.count > 0):
                hero_health_max += patent_shoes.add_health
                patent_shoes.count -= 1
                print("\nNice shoes! Your health was increased")
                backpack[5] = (patent_shoes.name + " x" + str(patent_shoes.count))
            elif (patent_shoes.count < 1):
                print("\nYou don't have any shoes")
        elif backpack_choose == knitted_mittens.name:
            if (knitted_mittens.count > 0):
                hero_health_max += knitted_mittens.add_health
                knitted_mittens.count -= 1
                print("\nOooh, that's so cute! Your health was increased")
                backpack[6] = (knitted_mittens.name + " x" + str(knitted_mittens.count))
            elif (knitted_mittens.count < 1):
                print("\nYou don't have any mittens")
        else:
            print("There is no such item")

    if current_action == actions[1] and hero_health > 0:                                                                      #healing menu cycle
        if (hero_health < hero_health_max and potion_health.count > 0):
                if (hero_health + potion_health.add_health) >= hero_health_max:
                    hero_health = hero_health_max
                    potion_health.count = potion_health.count -1
                else:
                    hero_health += potion_health.add_health
                    potion_health.count = potion_health.count -1  
                    print("\nYou have been healed")
                    backpack[0] = (potion_health.name + " x" + str(potion_health.count))
        elif (hero_health < hero_health_max and potion_health.count < 1):
                print("\nYou don't have potion of health")
        else:
            print("\nYou don't need to be healed")

    while current_action == actions[2] and hero_health > 0:                                                                   #moving menu cycle
        print("\nAvailable directions:")
        for item in direction:
            print(item)
        print("Choose direction or print \"back\" to leave direction menu")
        direction_choose = input("\n>>>").lower()

        if direction_choose == "back":
            print("You choose to stay here for a while")
            break

        elif (direction_choose == direction[0]
           or direction_choose == direction[1]
           or direction_choose == direction[2]
           or direction_choose == direction[3]):
            print("You have moved", direction_choose)
            current_happening = random.choice(happenings)
            if current_happening == happenings[0]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[0] and ghoul.health > 0 and hero_health > 0):
                    ghoul.damage = random.randint(8,16)
                    hero_damage = random.randint(6,14)
                    hero_damage_summ = hero_damage + hero_damage_add
                    hero_health -= ghoul.damage
                    ghoul.health -= hero_damage_summ
                    if hero_health < 1:
                        print("\n" + current_happening + " damage you " + str(ghoul.damage) + " points!")
                        print(current_happening + " killed you\n")
                        break
                    elif ghoul.health < 1:
                        print("\n" + current_happening + " damage you " + str(ghoul.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")                        
                        winning_info()
                        input("\npress any key to continue")
                        break
                    else:
                        print("\n" + current_happening + " damage you " + str(ghoul.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")
                        input("\npress any key to attack")
                        continue
                ghoul.health = ghoul.health_default
            elif current_happening == happenings[1]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[1] and rat.health > 0 and hero_health > 0):
                    rat.damage = random.randint(2,5)
                    hero_damage = random.randint(6,14)
                    hero_damage_summ = hero_damage + hero_damage_add
                    hero_health -= rat.damage
                    rat.health -= hero_damage
                    if hero_health < 1:
                        print("\n" + current_happening + " damage you " + str(rat.damage) + " points!")
                        print(current_happening + " killed you\n")
                        break
                    elif rat.health < 1:
                        print("\n" + current_happening + " damage you " + str(rat.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")                        
                        winning_info()
                        input("\npress any key to continue")
                        break
                    else:
                        print("\n" + current_happening + " damage you " + str(rat.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")
                        input("\npress any key to attack")
                        continue
                rat.health = rat.health_default
            elif current_happening == happenings[2]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[2] and mutated_rat.health > 0 and hero_health > 0):
                    mutated_rat.damage = random.randint(2,10)
                    hero_damage = random.randint(6,14)
                    hero_damage_summ = hero_damage + hero_damage_add
                    hero_health -= mutated_rat.damage
                    mutated_rat.health -= hero_damage
                    if hero_health < 1:
                        print("\n" + current_happening + " damage you " + str(mutated_rat.damage) + " points!")
                        print(current_happening + " killed you\n")
                        break
                    elif mutated_rat.health < 1:
                        print("\n" + current_happening + " damage you " + str(mutated_rat.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")                        
                        winning_info()
                        input("\npress any key to continue")
                        break
                    else:
                        print("\n" + current_happening + " damage you " + str(mutated_rat.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")
                        input("\npress any key to attack")
                        continue
                mutated_rat.health = mutated_rat.health_default
            elif current_happening == happenings[3]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[3] and feral_cat.health > 0 and hero_health > 0):
                    feral_cat.damage = random.randint(4,12)
                    hero_damage = random.randint(6,14)
                    hero_damage_summ = hero_damage + hero_damage_add                    
                    hero_health -= feral_cat.damage
                    feral_cat.health -= hero_damage
                    if hero_health < 1:
                        print("\n" + current_happening + " damage you " + str(feral_cat.damage) + " points!")
                        print(current_happening + " killed you\n")
                        break
                    elif feral_cat.health < 1:
                        print("\n" + current_happening + " damage you " + str(feral_cat.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")                        
                        winning_info()
                        input("\npress any key to continue")                            
                        break
                    else:
                        print("\n" + current_happening + " damage you " + str(feral_cat.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")
                        input("\npress any key to attack")
                        continue
                feral_cat.health = feral_cat.health_default
            elif current_happening == happenings[4]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[4] and feral_dog.health > 0 and hero_health > 0):
                    feral_dog.damage = random.randint(4,12)
                    hero_damage = random.randint(6,14)
                    hero_damage_summ = hero_damage + hero_damage_add
                    hero_health -= feral_dog.damage
                    feral_dog.health -= hero_damage
                    if hero_health < 1:
                        print("\n" + current_happening + " damage you " + str(feral_dog.damage) + " points!")
                        print(current_happening + " killed you\n")
                        break
                    elif feral_dog.health < 1:
                        print("\n" + current_happening + " damage you " + str(feral_dog.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")                        
                        winning_info()
                        input("\npress any key to continue")
                        break
                    else:
                        print("\n" + current_happening + " damage you " + str(feral_dog.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")
                        input("\npress any key to attack")
                        continue
                feral_dog.health = feral_dog.health_default
            elif current_happening == happenings[5]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[5] and mutated_snake.health > 0 and hero_health > 0):
                    mutated_snake.damage = random.randint(1,9)
                    hero_damage = random.randint(6,14)
                    hero_damage_summ = hero_damage + hero_damage_add
                    hero_health -= mutated_snake.damage
                    mutated_snake.health -= hero_damage
                    if hero_health < 1:
                        print("\n" + current_happening + " damage you " + str(mutated_snake.damage) + " points!")
                        print(current_happening + " killed you\n")
                        break
                    elif mutated_snake.health < 1:
                        print("\n" + current_happening + " damage you " + str(mutated_snake.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")                        
                        winning_info()
                        input("\npress any key to continue")
                        break
                    else:
                        print("\n" + current_happening + " damage you " + str(mutated_snake.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")
                        input("\npress any key to attack")
                        continue
                mutated_snake.health = mutated_snake.health_default
            elif current_happening == happenings[6]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[6] and coyote.health > 0 and hero_health > 0):
                    coyote.damage = random.randint(6,14)
                    hero_damage = random.randint(6,14)
                    hero_damage_summ = hero_damage + hero_damage_add
                    hero_health -= coyote.damage
                    coyote.health -= hero_damage
                    if hero_health < 1:
                        print("\n" + current_happening + " damage you " + str(coyote.damage) + " points!")
                        print(current_happening + " killed you\n")
                        break
                    elif coyote.health < 1:
                        print("\n" + current_happening + " damage you " + str(coyote.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")                        
                        winning_info()
                        input("\npress any key to continue")
                        break
                    else:
                        print("\n" + current_happening + " damage you " + str(coyote.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")
                        input("\npress any key to attack")
                        continue
                coyote.health = coyote.health_default
            elif current_happening == happenings[7]:
                print("You will have a fight with " + current_happening + "!")
                while (current_happening == happenings[7] and scorpion.health > 0 and hero_health > 0):
                    scorpion.damage = random.randint(10,18)
                    hero_damage = random.randint(6,14)
                    hero_damage_summ = hero_damage + hero_damage_add
                    hero_health -= scorpion.damage
                    scorpion.health -= hero_damage
                    if hero_health < 1:
                        print("\n" + current_happening + " damage you " + str(scorpion.damage) + " points!")
                        print(current_happening + " killed you\n")
                        break
                    elif scorpion.health < 1:
                        print("\n" + current_happening + " damage you " + str(scorpion.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")                        
                        winning_info()
                        input("\npress any key to continue")
                        break
                    else:
                        print("\n" + current_happening + " damage you " + str(scorpion.damage) + " points! ")
                        health_info()
                        print("\nYou damage " + current_happening + " " + str(hero_damage_summ) + " points!")
                        input("\npress any key to attack")
                        continue
                scorpion.health = scorpion.health_default
            elif (current_happening == happenings[8]
               or current_happening == happenings[9]):
                current_looting = random.choice(looting)
                if current_looting == potion_health.name:
                    potion_health.count += 1
                    print("You found " + current_happening + ". There was " + current_looting + ". It's added to your backpack")
                elif current_looting == potion_strength.name:
                    potion_strength.count += 1
                    print("You found " + current_happening + ". There was " + current_looting + ". It's added to your backpack")
                elif current_looting == new_sword.name:
                    new_sword.count += 1
                    print("You found " + current_happening + ". There was " + current_looting + ". It's added to your backpack")
                elif current_looting == knife.name:
                    knife.count += 1
                    print("You found " + current_happening + ". There was " + current_looting + ". It's added to your backpack")
                elif current_looting == stylish_hat.name:
                    stylish_hat.count += 1
                    print("You found " + current_happening + ". There was " + current_looting + ". It's added to your backpack")
                elif current_looting == patent_shoes.name:
                    patent_shoes.count += 1
                    print("You found " + current_happening + ". There was " + current_looting + ". It's added to your backpack")
                elif current_looting == knitted_mittens.name:
                    knitted_mittens.count += 1
                    print("You found " + current_happening + ". There was " + current_looting + ". It's added to your backpack")
                elif current_looting == nothing_loot.name:
                    print("You found " + current_happening + ". There was " + current_looting)
            elif (current_happening == happenings[10]
               or current_happening == happenings[11]
               or current_happening == happenings[12]
               or current_happening == happenings[13]
               or current_happening == happenings[14]):    
                print("There is " + current_happening + " in this place")
        else:
            print("There is no such direction")

input("Press Enter again to leave")