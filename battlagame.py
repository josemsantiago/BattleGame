# José Santiago Echevarria
# Python Fundamentals Week 1: Battle Game
# May 13,2023

import sys

# Character stats configuration
CHARACTERS = {
    "wizard": {"name": "Wizard", "damage": 150, "hp": 70},
    "elf": {"name": "Elf", "damage": 100, "hp": 100},
    "human": {"name": "Human", "damage": 20, "hp": 150},
    "orc": {"name": "Orc", "damage": 95, "hp": 150}
}

# Dragon stats
DRAGON_HP = 300
DRAGON_DAMAGE = 50

def get_character_choice():
    """Get and validate character choice from user."""
    while True:
        try:
            print("Welcome to Dragonic Battle!")
            print("You can exit the game anytime when making choices by typing 'exit'")
            print("You are reborn into a faraway kingdom where a menacing dragon has long been wreaking havoc on the lives of its people; your mission is to defeat the dragon, for if you fail, the kingdom shall fall, but if you succeed, the kingdom shall flourish once again.")
            print("The fate of the kingdom rests on your choice of race, so choose wisely among the available options of humans, orcs, elves, or wizards.")

            character = input(
                "1) Wizard: A powerful spellcaster with an affinity for manipulating arcane forces.\n"
                "2) Elf: A graceful and agile creature with a deep connection to nature and magical abilities.\n"
                "3) Human: A versatile and adaptable race capable of excelling in a variety of roles, from skilled craftsmen to powerful knights.\n"
                "4) Orc: A brutish and fierce warrior with an innate talent for combat and a love for battle.\n"
                "Choose your race: "
            ).strip().lower()

            if character == "exit":
                return None

            # Map input to character type
            char_map = {"1": "wizard", "wizard": "wizard", "2": "elf", "elf": "elf",
                       "3": "human", "human": "human", "4": "orc", "orc": "orc"}

            if character in char_map:
                return char_map[character]
            else:
                print("Unknown race. Please choose a valid option.")

        except (KeyboardInterrupt, EOFError):
            print("\nGame interrupted. Thanks for playing!")
            return None

def get_character_name():
    """Get and validate character name from user."""
    try:
        character_name = input("Name your character: ").strip()
        if character_name.lower() == "exit":
            return None
        if not character_name:
            character_name = "Unnamed Hero"
        return character_name
    except (KeyboardInterrupt, EOFError):
        print("\nGame interrupted. Thanks for playing!")
        return None

def battle(character_type, character_name):
    """Execute the battle between character and dragon."""
    char_stats = CHARACTERS[character_type].copy()
    my_hp = char_stats["hp"]
    my_damage = char_stats["damage"]
    character_class = char_stats["name"]

    dragon_hp = DRAGON_HP

    print(f"\nYou have chosen the character: {character_name} a {character_class}")
    print(f"Health: {my_hp}")
    print(f"Damage: {my_damage}\n")

    while True:
        # Player attacks dragon
        dragon_hp -= my_damage
        print(f"{character_name} damaged the Dragon!")
        print(f"The Dragon's hitpoints are now: {dragon_hp}\n")

        if dragon_hp <= 0:
            print("The Dragon has lost the battle! Victory is yours!")
            return True

        # Dragon attacks player
        my_hp -= DRAGON_DAMAGE
        print(f"The Dragon strikes back at {character_name}")
        print(f"{character_name}'s hitpoints are now: {my_hp}\n")

        if my_hp <= 0:
            print(f"{character_name} has lost the battle. The kingdom falls...")
            return False

def get_replay_choice():
    """Get user's choice to replay the game."""
    while True:
        try:
            replay = input("Would you like to play again? (yes or no): ").strip().lower()
            if replay in ["yes", "y"]:
                return True
            elif replay in ["no", "n"]:
                return False
            else:
                print("Invalid option. Please enter 'yes' or 'no'.")
        except (KeyboardInterrupt, EOFError):
            print("\nThanks for playing!")
            return False

def main():
    """Main game loop."""
    try:
        while True:
            # Get character choice
            character_type = get_character_choice()
            if character_type is None:
                break

            # Get character name
            character_name = get_character_name()
            if character_name is None:
                break

            # Start battle
            battle_result = battle(character_type, character_name)

            # Ask if player wants to replay
            if not get_replay_choice():
                break

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Thanks for playing!")
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
