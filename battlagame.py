# José Santiago Echevarria
# Python Fundamentals Week 1: Battle Game
# May 13,2023


wizard = "Wizard"
wizard_damage = 150
wizard_hp = 70

elf = "Elf"
elf_damage = 100
elf_hp = 100

human = "Human"
human_damage = 20
human_hp = 150

orc = "Orc"
orc_damage = 95
orc_hp = 150


replay = "yes"
exit = "no"

while replay == "yes":

    while True:
        print("Welcome to Dragonic Battle! \nYou can exit the game anytime when making choices by typing \'exit\' \nYou are reborn into a faraway kingdom where a menacing dragon has long been wreaking havoc on the lives of its people; your mission is to defeat the dragon, for if you fail, the kingdom shall fall, but if you succeed, the kingdom shall flourish once again.")
        print("The fate of the kingdom rests on your choice of race, so choose wisely among the available options of humans, orcs, elves, or wizards.")
        character = input(
            "1) Wizard: A powerful spellcaster with an affinity for manipulating arcane forces. \n2) Elf: A graceful and agile creature with a deep connection to nature and magical abilities.  \n3) Human: A versatile and adaptable race capable of excelling in a variety of roles, from skilled craftsmen to powerful knights.\n4) Orc: A brutish and fierce warrior with an innate talent for combat and a love for battle. \nChoose your race:")
        if character.strip() == "1" or character.lower().strip() == 'wizard':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if character.strip() == "2" or character.lower().strip() == 'elf':
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if character.strip() == "3" or character.lower().strip() == 'human':
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        if character.strip() == "4" or character.lower().strip() == 'orc':
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        if character.strip() == "exit" or character.lower().strip() == 'exit':
            break
        print("Unknown race")
    if character.strip() == "exit" or character.lower().strip() == 'exit':
        break
    character_name = input("Name your character: ")
    if character_name.strip() == "exit" or character_name.lower().strip() == 'exit':
        break
    print(
        f"You have choosen the character : {character_name} a {character} \nHealth: {my_hp}\nDamage: {my_damage}\n")
    dragon_hp = 300
    dragon_damage = 50

    while True:
        dragon_hp -= my_damage
        print(
            f"{character_name} damaged the Dragon! \nThe Dragon\'s hitpoints are now : {dragon_hp}\n")
        if dragon_hp <= 0:
            print("The Dragon has lost the battle")
            break
        my_hp -= dragon_damage
        print(
            f"The Dragon strikes back at {character_name}\n{character_name}\'s hitpoints are now : {my_hp}\n")
        if my_hp <= 0:
            print(f"{character_name} has lost the battle")
            break
    while True:
        replay = input(
            "Would you like to play again? (yes or no) ").lower().strip()
        if replay != "yes" and replay != "no":
            print("Invalid option")
        else:
            break

print("Thanks for playing!")
