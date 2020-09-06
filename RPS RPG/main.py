from player import Player


def combat(player_one: Player, player_two: Player) -> None:
    print("round start:")
    player_one.get_move()
    player_two.get_move()

    player_one.calculate_combat_modifiers(player_two)
    player_two.calculate_combat_modifiers(player_one)

    player_one.update_health(player_two)
    player_two.update_health(player_one)
    print("round end\n---------------\n")


def main():
    npc_win_count: int = 0
    player_win_count: int = 0
    turns_in_rounds: int = 0
    # input("Welcome to Rock Paper Scissor RPG! (Press Enter to Start)")
    skills: list = ["risk", "regen", "thorns", "dodge", "leech", "block", "heal", "insurance"]
    skill_descriptions: dict = {"regen": "On a win or tie, you gain 1 health, but you lose your max hp decreases by 1.",
                                "leech": "When u win u gain 50% of atk in hp, lose 0.5 atk on lose.",
                                "thorns": "Reflect 50% of damage taken but take 25% more damage",
                                "dodge": "Dodge atk 30% of the times but don't do damage 20% of the times",
                                "block": "When you win block the opponent's next attack next turn, but halves your damage this turn",
                                "risk": "If you win,  +2 to your attack this round, if you lose, -2 to your hp",
                                "heal": "If you win/tie, +1 to hp, but -1 to attack",
                                "insurance": "Take 50% less damage, but adds 1 to enemy atk next round"}

    for _ in range(100):
        player = Player(num_skills=6, num_points=3, skill_list=skills, skill_descriptions=skill_descriptions, npc=True,
                        name="player")
        npc = Player(num_skills=6, num_points=3, npc=True, skill_list=skills, skill_descriptions=skill_descriptions,
                     name="npc")

        count_turns = 0

        while player.current_health > 0 and npc.current_health > 0:
            combat(player, npc)
            count_turns += 1

        if player.current_health <= 0:
            npc_win_count += 1
        elif npc.current_health <= 0:
            player_win_count += 1

        turns_in_rounds += count_turns

    average_turns = turns_in_rounds / 100
    print(average_turns, player_win_count, npc_win_count)

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
