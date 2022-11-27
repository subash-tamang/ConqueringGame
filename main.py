# print("Welcome my king, in order to protect our kingdom from threat of East India Company,"
#       " we have to unify petty kingdoms into one great Kingdom.")
# choice1 = input("Press 'Start' to begin your conquest or 'Quit' to end in good.\n").lower()
#
# if choice1 == "start":
#     choice2 = input("You have an army of 5000. Which kingdom would you like to conquer first - 'Nuwakot'"
#                     " or 'Lamjung'?\n").lower()
#     if choice2 == "nuwakot":
#         print("Hurray! You conquered Nuwakot.")
#     elif choice2 == "lamjung":
#         print("Lamjung is too strong to be defeated. You lost.")
# elif choice1 == "quit":
#     print("Enjoy your reign over your Kingdom.")


# from gorkha import Gorkha
import gorkha
from nuwakot import Nuwakot
from lamjung import Lamjung
from kantipur import Kantipur
from battle import Battle

game_is_on = True

gorkha = gorkha.Gorkha()  # creating object

while game_is_on:

    start = input("Press 'Start' to begin your conquest or 'Quit' to end in good.\n").lower()

    if start == "start":

        # gorkha = gorkha.Gorkha()  # creating object

        print("### Press ###")
        print("# Attack # to attack enemy kingdom")
        print("# Military # to see your military")

        choice = input().lower()

        if choice == "attack":
            foe_kingdom = input("Which kingdom do you want to conquer?\nNuwakot/Lamjung/Kantipur\n").lower()

            # gorkha = gorkha.Gorkha()  # creating object

            if foe_kingdom == "nuwakot":
                foe = Nuwakot()  # creating object
            elif foe_kingdom == "lamjung":
                foe = Lamjung()  # creating object
            else:
                foe = Kantipur()
            # elif foe_kingdom == "kantipur":
            #     foe = Kantipur()
            # else:
            #     print(f"You cannot afford to attack {foe_kingdom}.")

            battle = Battle(gorkha.army, foe.army, foe_kingdom)

            game_is_on = battle.war()

        elif choice == "military":
            print(f"You have an army of {gorkha.army}.")
    else:
        game_is_on = False
        print("Enjoy your reign over your Kingdom.")
