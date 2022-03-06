import random
from pokemon import Pokemon

Pokemon.instantiate_from_csv()

# Fixed Parameters
opp_name = "Gary"                           # opponent's name
max_num_poke = 6                            # max. amount of Pokemon a player can select to play with
max_train = 3                               # max. amount of trainings
max_healings = 3                            # max. amount of healings
train_plus = 2                              # +damage when trained
heal_plus = 3                               # +health when healed
width_board = len(str(Pokemon.all[0])) - 20 # length of the lines displayed during the game, alligned with length of Pokemon displayed
print(len(str(Pokemon.all[0])))

# Variables
number_pokemon = len(Pokemon.all)           # number of instantiated Pokemon
assigned_to_player = []                     # list of Pokemon assigned to the player
assigned_to_opp = []                        # list of Pokemon assigned to the opponent
pko = 0                                     # number of KO-Pokemon of the player (KO-counter)
gko = 0                                     # number of KO-Pokemon of the opponent (KO-counter)
train_count = 0                             # current number of trainings used
heal_count = 0                              # current number of healthpotions used


# Checks the Inputs (must be Digits and in given Range) and checks existing number in your list and if active for action decisions
def val_input(num_name, interval, list):
    num = ""
    within_interval = False
    in_list = True
    temp_num = []
    temp_status = []
    temp_lost_HP = []
    status = True
    lost_HP = True
    if num_name == "pick_heal":
        lost_HP = False
    if list != None:
        in_list = False
        status = False
        for i in range(len(list)):
            temp_num.append(list[i].num)
            temp_status.append(list[i].status)
            if list[i].hp < list[i].max_hp:
                temp_lost_HP.append(list[i].num)

    while num.isdigit() == False or within_interval == False or in_list == False or status == False or lost_HP == False:
        if num_name == "player_mode":
            num = input("Do you play agains the Computer (1) or another Player (2): ")
        if num_name == "num_poke":
            num = input(f"Enter the Number of Pokemon (1-{max_num_poke}): ")
        elif num_name == "mode":
            num = input("Select your Game-Mode:\n1  Pokemon Picked Randomly\n2  Pokemon Selecton\n")
        elif num_name == "select":
            num = input("Select your next Pokomon: ")
        elif num_name == "action":
            num = input(f"\nWhat do you want to do?\
                \n1  Fight\
                \n2  Train ({int(train_count)}/{max_train})\
                \n3  Heal  ({int(heal_count)}/{max_healings})\
                \n4  Show Pokemon-Type-Relationships\
                \n5  Show\
                \n6  Quit\n")
        elif num_name == "pick_battle":
            num = input("\nWhich Pokemon will Fight (#): ")
        elif num_name == "pick_train":
            num = input("\nWhich Pokemon will be Trained (#): ")
        elif num_name == "pick_heal":
            num = input("\nWhich Pokemon will be Healed (#): ")

        if num.isdigit() == False:
            print("Input must be a Number!")

        if num.isdigit() == True:
            if int(num) in interval:
                within_interval = True

                if num_name == "pick_battle" or num_name == "pick_train" or num_name == "pick_heal":
                    if int(num) in temp_num:
                        in_list = True

                        if temp_status[temp_num.index(int(num))] == "active":
                            status = True

                            if num_name == "pick_heal":
                                if int(num) in temp_lost_HP:
                                    lost_HP = True
                                else:
                                    print("Your chosen Pokemon has already full HP.")

                        else:
                            status = False
                            print("Chosen Pokemon is KO!\nChoose an active One!")

                    else:
                        in_list = False
                        print("Chosen Pokemon is not in your list.")

            else:
                within_interval = False
                if num_name == "num_poke":
                    print(f"Number of Pokemon must be 1-{max_num_poke}!")
                elif num_name == "mode" or num_name == "player_mode":
                    print("Select between Option 1 and 2!")
                elif num_name == "select":
                    print(f"Selected Number must be 1-{number_pokemon}!")
                elif num_name == "action":
                    print("Choose beween Option 1-6!")
                elif num_name == "pick_battle" or num_name == "pick_train" or num_name == "pick_heal":
                    print(f"Number must be 1-{number_pokemon}.")

    return int(num)


# Show Pokemon-Type-Relationships (which Type has advantge over which Type)
def show_admap():
    col_width = (width_board - 1) // 6
    blocks = col_width * u"\u2588"
    print("")
    print(" POKEMON-TYPE-RELATIONSHIPS ".center(width_board, "-"))
    empty = "".center(col_width)
    a = "\033[0;31mfire\033[0;0m".center(col_width + 13)
    b = "\033[0;34mwater\033[0;0m".center(col_width + 13)
    c = "\033[0;32mgrass\033[0;0m".center(col_width + 13)
    d = "\033[0;33melectric\033[0;0m".center(col_width + 13)
    e = "\033[0;35mrock\033[0;0m".center(col_width + 13)
    ad = f"\033[0;32m{blocks}\033[0;0m".center(col_width + 13)
    disad = f"\033[0;31m{blocks}\033[0;0m".center(col_width + 13)
    print((empty + "|" + a + b + c + d + e).center(width_board + 65))
    print(((6 * col_width + 1) * "-").center(width_board))
    print((a + "|" + empty + disad + ad + ad + disad).center(width_board + 65))
    print((b + "|" + ad + empty + disad + disad + ad).center(width_board + 65))
    print((c + "|" + disad + ad + empty + disad + ad).center(width_board + 65))
    print((d + "|" + disad + ad + ad + empty + disad).center(width_board + 65))
    print((e + "|" + ad + disad + disad + ad + empty).center(width_board + 65))
    print("")


# Show Status of assined Pokemon for Player and Opponent
def show():
    print(f"\n\033[0;33m{player_name}'s Pokemon:\033[0;0m")
    print((width_board) * "\033[0;34m-\033[0;0m")
    for i in range(num_poke):
        print(assigned_to_player[i])
    print(f"\n\033[0;33m{opp_name}'s Pokemon:\033[0;0m")
    print((width_board) * "\033[0;34m-\033[0;0m")
    for i in range(num_poke):
        print(assigned_to_opp[i])


# Returns the indicies of your assigned Pokemon List for the Pokemon that are active or are active and lost HP
def active(list, funct):
    actives = []
    if funct == 1:
        for i in range(len(list)):
            if list[i].status == 'active':
                actives.append(i)
    elif funct == 2:
        for i in range(len(list)):
            if list[i].status == 'active' and list[i].hp < list[i].max_hp:
                actives.append(i)
    return actives


# Translates assigned Pokemon-Number (Input) to Positon in List (assigned_to_player)
def pick_player(list, pick):
    for i in range(len(list)):
        if list[i].num == pick:
            return i


# Introduction and some Parameters are set by User
print("\n" + width_board * "-")
print("\033[0;33m WELCOME TO THE POKEMON GAME \033[0;0m".center(width_board + 13, "-"))
print(width_board * "-")
player_name = input("\nEnter your Name: ")
print(f"You will fight against {opp_name}!")
num_poke = val_input("num_poke", range(1, max_num_poke + 1), None)
show_admap()
mode = val_input("mode", range(1, 3), None)

# Random Assignment of Pokemon
if mode == 1:
    for i in range(num_poke):
        assigned_to_player.append(Pokemon.all[random.randint(0, number_pokemon - 1 - i)])
        Pokemon.all.remove(assigned_to_player[i])
    for i in range(num_poke):
        assigned_to_opp.append(Pokemon.all[random.randint(0, number_pokemon - 1 - num_poke - i)])
        Pokemon.all.remove(assigned_to_opp[i])

# Player selects Pokemon from a List
# Opponent gets randomly assigned Pokemon
elif mode == 2:
    print("\n")
    print("\033[0;33m AVAILABLE POKEMON \033[0;0m".center(width_board + 13, "_"))
    for i in range(number_pokemon):
        print(Pokemon.all[i])
    print(f"\nSelect your {num_poke} Pokemon from the List: ")
    selection = []
    for i in range(num_poke):
        next_select = val_input("select", range(1, number_pokemon + 1), None)
        selection.append(next_select)
        if i > 0:
            while selection[i] in selection[:-1]:
                print("Number already selected!")
                selection.pop()
                next_select = val_input("select", range(1, number_pokemon + 1), None)
                selection.append(next_select)
    print("\n")
    for i in range(num_poke):
        print(
            f" selected: #{str(Pokemon.all[selection[i] - 1].num).rjust(2)} {Pokemon.all[selection[i] - 1].name.ljust(11)}{Pokemon.all[selection[i] - 1].type.ljust(28)}")
        assigned_to_player.append(Pokemon.all[selection[i] - 1])
    for i in range(num_poke):
        Pokemon.all.remove(assigned_to_player[i])
    for i in range(num_poke):
        assigned_to_opp.append(Pokemon.all[random.randint(0, (len(Pokemon.all) - 1) - num_poke - i)])
        Pokemon.all.remove(assigned_to_opp[i])

# Status of Assignment
show()

# The Game goes on, until the KO-Counter for one of the Players equals his number of Pokemon
while pko < num_poke and gko < num_poke:
    pko = 0
    gko = 0

    # Option Selection
    action = val_input("action", range(1, 7), None)
    # ----------------------------------------------------------------------------------------------
    # 1. Fight
    if action == 1:
        valids = active(assigned_to_player, 1)
        valids_opp = active(assigned_to_opp, 1)
        pick2 = random.choice(valids_opp)
        if len(valids) == 1:
            pick1 = valids[0]
            print("\n")
            print(f"Your last remaining Pokemon ({assigned_to_player[valids[0]].name}) is sent into battle")
        elif len(valids) > 1:
            pick = val_input("pick_battle", range(1, number_pokemon + 1), assigned_to_player)
            pick1 = pick_player(assigned_to_player, pick)

        assigned_to_player[pick1].battle(assigned_to_opp[pick2], width_board)

        for i in range(num_poke):
            if assigned_to_player[i].status == "KO":
                pko += 1
            if assigned_to_opp[i].status == "KO":
                gko += 1
    # ----------------------------------------------------------------------------------------------
    # 2. Train
    elif action == 2:
        if train_count < max_train:
            valids = active(assigned_to_player, 1)
            valids_opp = active(assigned_to_opp, 1)
            pick2 = random.choice(valids_opp)
            if len(valids) == 1:
                pick1 = valids[0]
                print(f"\nYour last remaining Pokemon ({assigned_to_player[valids[0]].name}) will be trained")
            elif len(valids) > 1:
                pick = val_input("pick_train", range(1, number_pokemon + 1), assigned_to_player)
                pick1 = pick_player(assigned_to_player, pick)

            assigned_to_player[pick1].train(player_name, train_plus, width_board)
            assigned_to_opp[pick2].train(opp_name, train_plus, width_board)
            train_count += 1
        else:
            print("\nYou used all your Trainings!")
    # ----------------------------------------------------------------------------------------------
    # 3. Heal
    elif action == 3:
        if heal_count < max_healings:
            valids = active(assigned_to_player, 2)
            valids_opp = active(assigned_to_opp, 2)
            if len(valids) > 0:
                if len(valids) == 1 and len(valids_opp) == 0:
                    print(
                        f"\nYour only Pekomen that is active and has not full HP is {assigned_to_player[valids[0]].name}")
                    pick1 = valids[0]
                    assigned_to_player[pick1].heal(player_name, heal_plus, width_board)
                    print(f"{opp_name} has no Pokemon to heal!")
                    heal_count += 1
                elif len(valids) == 1 and len(valids_opp) > 0:
                    print(
                        f"\nYour only Pekomen that is active and has not full HP is {assigned_to_player[valids[0]].name}")
                    pick1 = valids[0]
                    pick2 = random.choice(valids_opp)
                    assigned_to_player[pick1].heal(player_name, heal_plus, width_board)
                    assigned_to_opp[pick2].heal(opp_name, heal_plus, width_board)
                    heal_count += 1
                elif len(valids) > 1 and len(valids_opp) == 0:
                    pick = val_input("pick_heal", range(1, number_pokemon + 1), assigned_to_player)
                    pick1 = pick_player(assigned_to_player, pick)
                    assigned_to_player[pick1].heal(player_name, heal_plus, width_board)
                    print(f"{opp_name} has no Pokemon to heal!")
                    heal_count += 1
                elif len(valids) > 1 and len(valids_opp) > 0:
                    pick = val_input("pick_heal", range(1, number_pokemon + 1), assigned_to_player)
                    pick1 = pick_player(assigned_to_player, pick)
                    pick2 = random.choice(valids_opp)
                    assigned_to_player[pick1].heal(player_name, heal_plus, width_board)
                    assigned_to_opp[pick2].heal(opp_name, heal_plus, width_board)
                    heal_count += 1
            else:
                print("\nAll your active Pokemon have full HP!")
        else:
            print("\nYou used all your Healthpotions!")
    # ----------------------------------------------------------------------------------------------
    # 4. Show Pokemon-Type-Relationships
    elif action == 4:
        show_admap()
    # ----------------------------------------------------------------------------------------------
    # 4. Show
    elif action == 5:
        show()
    # ----------------------------------------------------------------------------------------------
    # 4. Quit
    elif action == 6:
        break
    # ----------------------------------------------------------------------------------------------
    show()

print("\n")
if pko == num_poke and gko != num_poke:
    print("\033[0;31m All your Pokemon went KO - LOOSE \033[0;0m".center(width_board + 13, "-"))
elif pko != num_poke and gko == num_poke:
    print(f"\033[0;32m All of {opp_name}'s Pokemon went KO - WIN \033[0;0m".center(width_board + 13, "-"))
elif pko == num_poke and gko == num_poke:
    print("\033[0;33m All Pokemon went KO - TIE \033[0;0m".center(width_board + 13, "-"))
print("\n")
