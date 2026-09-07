"""
Name: Adham Farag
Last updated: September 6, 2026
Description: Interactive choose-your-own-adventure game to rescue Ally.
"""

def adventure():
    """ This function runs one session of a choose your own adventure.
        Arguments: None
        Returns: 
            - int: 1 to end the game loop, 0 to restart the loop
    """

    print()
    print("Welcome, worthy adventurer, to The Swamp,")
    print("home to Ally the Golden Gator and sourdough bread!")
    print()

    player_name, player_class = create_player()

    print()
    
    # 4.b Refactor: The 'else' block was removed since 4.a guarantees only Warrior or Mage
    if player_class == "Warrior":
        health = 100
        mana = 50
        print("A brave warrior, ready to confront any challenge.")
    elif player_class == "Mage":
        health = 50
        mana = 100
        print("A cunning mage, capable of outwitting the strongest foe.")

    print()
    print("Here are your beginning stats:")
    print("Health: {}".format(health))
    print("Mana: {}".format(mana))
    print()

    print(player_name, "your quest is to rescue Ally from the Spartans")
    print("who hold her captive.")
    print("Let us begin...")
    print()

    # 4.c / 4.d Decision Point 1
    choice1 = input("You arrive at the Spartan camp gates. Do you [attack] or [sneak]? ").strip().lower()

    if choice1 == "attack":
        # 4.e Modify health
        health -= 40
        print(f"\nYou charge in! The guards hit you, losing 40 health. Current Health: {health}")
        
        # 4.c Decision Point 2
        choice2 = input("Do you push forward to the [dungeon] or [retreat]? ").strip().lower()
        if choice2 == "dungeon":
            print("\nYou kick the dungeon door down, defeat the warden, and rescue Ally!")
            print("[ENDING 1] YOU WIN!")
            return 1  # 4.f Return 1 to change 'win' and break the infinite loop
        else:
            print("\nYou flee the camp to rest. The quest continues...")
            return 0  # Return 0 to restart the infinite loop

    elif choice1 == "sneak":
        # 4.e Modify mana
        mana -= 30
        print(f"\nYou use an invisibility spell, draining 30 mana. Current Mana: {mana}")
        
        choice2 = input("You find Ally's cage. Do you use [magic] to pick the lock or [smash] it? ").strip().lower()
        if choice2 == "magic":
            print("\nThe lock clicks open silently! You escape with Ally.")
            print("[ENDING 2] YOU WIN!")
            return 1  # 4.f Return 1 to change 'win' and break the loop
        else:
            health -= 100
            print("\nThe smash alerts the guards. You are overwhelmed.")
            print("[ENDING 3] GAME OVER.")
            return 1  # 4.f Return 1 to change 'win' and break the loop
            
    else:
        print("\nYou hesitated. The Spartans spotted you! Try again.")
        return 0


def create_player():
    """ Prompts the user for their name and class.
        Arguments: None
        Returns:
            - player_name (string): Name of the player
            - player_class (string): Class of the player
    """

    player_name = input("Before we begin, what should I call you? ")
    
    # 4.a Update input to re-prompt until "Warrior" or "Mage" is entered
    player_class = ""
    while player_class not in ["Warrior", "Mage"]:
        player_class = input("What is your specialty? [Warrior / Mage] ").strip().capitalize()
        if player_class not in ["Warrior", "Mage"]:
            print("Invalid choice! Please type exactly 'Warrior' or 'Mage'.\n")

    return player_name, player_class

win = 0
while win == 0:
    win = adventure()