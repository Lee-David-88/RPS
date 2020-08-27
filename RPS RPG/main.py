from player import Player


def combat(player, other_player):
    player.start_round()
    other_player.start_round()
    player.end_round(other_player)


def main():
    input("Welcome to Rock Paper Scissor RPG! (Press Enter to Start)")
    skills = ["risk", "regen", "thorns", "dodge", "leech", "block", "heal", "insurance"]
    skill_descriptions = {"regen": "On a win or tie, you gain 1 health, but you lose your max hp decreases by 1.",
                          "leech": "When u win u gain 50% of atk in hp, lose 0.5 atk on lose.",
                          "thorns": "Reflect 50% of damage taken but take 25% more damage",
                          "dodge": "Dodge atk 30% of the times but don't do damage 20% of the times",
                          "block": "When you win block the opponent's next attack next turn, but halfs your damage this\
                                    turn",
                          "risk": "If you win,  +2 to your attack this round, if you lose, -2 to your hp",
                          "heal": "If you win/tie, +1 to hp, but -1 to attack",
                          "insurance": "Take 50% less damage, but adds 1 to enemy atk next round"}
    npc = Player(num_skills=6, num_points=3, npc=True, skill_list=skills, skill_descriptions=skill_descriptions)
    player = Player(num_skills=6, num_points=3, skill_list=skills, skill_descriptions=skill_descriptions)
    combat(player, npc)
    # player = character_stats()
    # allocate_stats(player)
    # foe = {"Hp": 10, "Attack": 2}
    # combat(player, foe)


if __name__ == "__main__":
    main()
# def character_stats():
#     character = {}
#     character["Hp"] = 12
#     character["Attack"] = 2
#
#     return character


# def allocate_stats(character):
#     setting_up = True
#     starting_points = 3
#     stat_points = starting_points
#
#     while setting_up:
#         print(character)
#
#         options = input(
#             "Would you like to put in points for Hp or Attack (Enter Hp or Attack or Press x to exit): ").capitalize().strip()
#         if options.lower() == "hp":
#             allocate_hp = int(
#                 input("How many points would you like to put into your Hp (Current Points:" + str(stat_points) + "): "))
#             if allocate_hp > stat_points:
#                 print("You cannot do that!")
#             elif stat_points >= allocate_hp > 0:
#                 character["Hp"] += allocate_hp * 2
#                 stat_points -= allocate_hp
#         elif options.lower() == "attack":
#             allocate_attack = int(
#                 input("How many points would you like to put into your attack (Current Points: " + str(
#                     stat_points) + "): "))
#             if allocate_attack > stat_points:
#                 print("You cannot do that!")
#             elif stat_points >= allocate_attack > 0:
#                 character["Attack"] += allocate_attack
#                 stat_points -= allocate_attack
#         elif options == "X":
#             setting_up = False
#         else:
#             return
#

# def combat(player, foe):
# playing = True

# choice = ["Rock", "Paper", "Scissor"]

# while playing:
# npc_choice = choice[random.randint(0, 2)]
#
# if player["Hp"] == 0:
#     print("You Lose!")
#     playing = False
# elif foe["Hp"] == 0:
#     print("You Win!")
#     playing = False
# else:
#     player_choice = str(input("Rock, Paper, Scissor? ")).capitalize().strip()
#
#     if player_choice == npc_choice:
#         print("Tie")
#     elif player_choice == "Rock":
#         if npc_choice == "Paper":
#             player["Hp"] -= foe["Attack"]
#             print("You took " + str(foe["Attack"]) + " damage! Player Hp: " + str(player["Hp"]))
#         elif npc_choice == "Scissor":
#             foe["Hp"] -= player["Attack"]
#             print("Npc took " + str(player["Attack"]) + " damage! Npc Hp: " + str(foe["Hp"]))
#     elif player_choice == "Paper":
#         if npc_choice == "Scissor":
#             player["Hp"] -= foe["Attack"]
#             print("You took " + str(foe["Attack"]) + " damage! Player Hp: " + str(player["Hp"]))
#         elif npc_choice == "Rock":
#             foe["Hp"] -= player["Attack"]
#             print("Npc took " + str(player["Attack"]) + " damage! Npc Hp: " + str(foe["Hp"]))
#     elif player_choice == "Scissor":
#         if npc_choice == "Rock":
#             player["Hp"] -= foe["Attack"]
#             print("You took " + str(foe["Attack"]) + " damage! Player Hp: " + str(player["Hp"]))
#         elif npc_choice == "Paper":
#             foe["Hp"] -= player["Attack"]
#             print("Npc took " + str(player["Attack"]) + " damage! Npc Hp: " + str(foe["Hp"]))

