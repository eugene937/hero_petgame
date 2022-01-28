potion_health_counter = 3
potion_health = "potion of health x"+str(potion_health_counter)

backpack = [potion_health,
"item2",
"item3",]

health = 7

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

current_action = "beginning"

while current_action != "quit" and current_action != "": #main menu cycle
    print("\nYour health:", str(health) +"/10")
    print("What do you want to do? Available actions: ")
    for item in actions:
        print(item)
    current_action = input("\n>>> ")

    while current_action == "backpack": #backpack menu cycle
        print("\nYour backpack contain", len(backpack), item_word +":")
        for item in backpack:
            print(item)
        print("Choose item to use or print \"back\" to leave backpack")
        backpack_choose = input("\n>>>")
        if backpack_choose == "back":
            break

    if current_action == "healing": #healing menu cycle
        if health < 10:
            health = 10
            potion_health_counter = potion_health_counter -1  
            print("\nYou have been healed")
        else:
            print("\nYou don't need to be healed")

    while current_action == "move": #moving menu cycle
        print("\nAvailable direction:")
        for item in direction:
            print(item)
        print("Choose direction or print \"back\" to leave direction menu")
        direction_choose = input("\n>>>")
        if direction_choose == "back":
            print("You choose to stay here for a while")
            break
        elif direction_choose == direction[0]:
            print("You have moved", direction[0])
            break
        elif direction_choose == direction[1]:
            print("You have moved", direction[1])
            break
        elif direction_choose == direction[2]:
            print("You have moved", direction[2])
            break
        elif direction_choose == direction[3]:
            print("You have moved", direction[3])
            break
        else:
            continue

input("Press Enter again to leave")