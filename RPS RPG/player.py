import random
import time


class Player:
    def __init__(self, num_skills: int = 0,
                 num_points: int = 0,
                 npc: bool = False,
                 skill_list=None,
                 skill_descriptions=None,
                 name: str = "",
                 debug: bool = False,
                 debug_max_health: float = 0,
                 debug_max_attack: float = 0,
                 debug_chosen_skills=None):

        if skill_list is None:
            skill_list = []
        if skill_descriptions is None:
            skill_descriptions = {}
        if debug_chosen_skills is None:
            debug_chosen_skills = []

        self.name = name
        self.npc: bool = npc

        # list of the two skills currently assigned to rock, paper, or scissors
        self.rock_skills: list = []
        self.paper_skills: list = []
        self.scissor_skills: list = []

        # list of all skills that have been chosen
        self.chosen_skills: list = []

        # caps of health and attack
        self.max_health: float = 12.0
        self.max_attack: float = 2.0

        # values of health and attack used for calculations against self
        self.current_health: float = 1.0
        self.current_attack: float = 0.0

        # backup values used for calculations against other player
        self.backup_health: float = 0.0
        self.backup_attack: float = 0.0

        # round specific modifiers
        self.attack_modifier_percentage: float = 1
        self.attack_modifier_static: float = 0

        self.health_modifier_percentage: float = 0
        self.health_modifier_static: float = 0

        self.damage_modifier_percentage: float = 1
        self.damage_reflection_percentage: float = 0
        self.block_damage: bool = False

        self.dodge_chance = 0

        # map of skill names to the methods that deal with the logic of those skills
        self.skillToFuncMap: dict = {}

        # list of skills the payer has chosen
        self.skill_list: list = skill_list

        self.map_functions()
        # if debug:
        #     if debug_max_health > 0:
        #         self.max_health = debug_max_health
        #     elif debug_max_attack > 0:
        #         self.max_attack = debug_max_attack
        #     if len(debug_chosen_skills) > 0:
        #         self.chosen_skills = debug_chosen_skills
        # else:
        self.allocate_starting_points(num_points)
        self.current_health = self.max_health
        self.current_attack = self.max_attack

        self.pick_skills(num_skills, skill_descriptions)
        self.shuffle_skill()

        # List where 1st element is choice and 2nd element is ability
        self.current_move: list = []

        # Stores "win", "lose", or "tie"
        self.result: str = ""

    # assigns skills to functions regardless of order skills are in
    def map_functions(self) -> None:
        func_list: list = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")]
        for func in func_list:
            for skill in self.skill_list:
                if func.startswith(skill):
                    self.skillToFuncMap[skill] = self.lambda_generator(func)

    def lambda_generator(self, func: str):
        return lambda other_player: getattr(self, func)(other_player)

    # allocations initial skill points into max_health or max_attack
    def allocate_starting_points(self, num_points: int) -> None:
        if self.npc:
            for _ in range(num_points):
                if random.randint(0, 1) == 0:
                    self.max_health += 2
                else:
                    self.max_attack += 1
        else:
            while num_points > 0:
                print("\"hp\" to add 2 health or \"attack\" to add 1 attack")
                print(f"current health: {self.max_health}, current attack: {self.max_attack}")
                choice: str = input(">: ")
                if choice.lower() == "hp":
                    self.max_health += 2
                    print("added 2 to health")
                elif choice.lower() == "attack":
                    self.max_attack += 1
                    print("added 1 to attack")
                else:
                    print("Invalid choice, please choose either \"hp\" or \"attack\"")
                    num_points += 1
                num_points -= 1

    # picks the <default 6> number of skills for use in game
    def pick_skills(self, num_skills: int, skill_descriptions: dict) -> None:
        remaining_skills = self.skill_list.copy()
        if self.npc:
            random.shuffle(remaining_skills)
            self.chosen_skills = remaining_skills[0:6]
            self.rock_skills = remaining_skills[0:2]
            self.paper_skills = remaining_skills[2:4]
            self.scissor_skills = remaining_skills[4:6]
            return
        while num_skills > 0:
            self.print_skills(remaining_skills, skill_descriptions)
            while True:
                choice = input("Pick a skill: ").lower()
                if choice in remaining_skills:
                    self.chosen_skills.append(remaining_skills.pop(remaining_skills.index(choice)))
                    num_skills -= 1
                    break
                elif choice in self.skill_list:
                    print("You already picked this")
                else:
                    print("Invalid choice")

    def print_skills(self, remaining_skills: list, skill_descriptions: dict) -> None:
        print("skills to pick from")
        for skill in remaining_skills:
            print(f"{skill.capitalize()} - {skill_descriptions[skill]}")

    # randomly assigns skills to rock, paper, or scissors
    def shuffle_skill(self) -> None:
        random.shuffle(self.chosen_skills)
        self.rock_skills = self.chosen_skills[0:2]
        self.paper_skills = self.chosen_skills[2:4]
        self.scissor_skills = self.chosen_skills[4:6]

    def reset_modifiers(self):
        self.attack_modifier_percentage = 1
        self.attack_modifier_static = 0

        self.health_modifier_percentage = 0
        self.health_modifier_static = 0

        self.damage_modifier_percentage = 1
        self.damage_reflection_percentage = 0
        self.dodge_chance = 0

    def get_move(self) -> None:
        choice: list = [None, None]
        choices: list = ["rock", "paper", "scissors"]
        choice_map: dict = {"rock": self.rock_skills,
                            "paper": self.paper_skills,
                            "scissors": self.scissor_skills}
        if self.npc:
            choice[0] = choices[random.randint(0, 2)]
            choice[1] = choice_map[choice[0]][random.randint(0, 1)]
            self.current_move = choice
            return
        while True:
            print(f"Available rock skills: {self.rock_skills[0]} and {self.rock_skills[1]}")
            print(f"Available paper skills: {self.paper_skills[0]} and {self.paper_skills[1]}")
            print(f"Available scissor skills: {self.scissor_skills[0]} and {self.scissor_skills[1]}")
            choice[0] = input("Enter a move of \"rock\", \"paper\", or \"scissors\": ").lower()
            if choice[0] in choices:
                while True:
                    choice[1] = input(
                        f"Which skill do you want to use? {choice_map[choice[0]][0]} or {choice_map[choice[1]][1]}").lower()
                    if choice[1] in choice_map[choices[0]]:
                        self.current_move = choice
                        return
                    print("Invalid choice")
            print("invalid choice")

    # determines whether the player won, lost, or tied
    def round_result(self, other_player_choice: list) -> str:
        if self.current_move[0] == other_player_choice[0]:
            return "tie"
        elif self.current_move[0] == "rock":
            return "win" if other_player_choice[0] == "scissors" else "lose"
        elif self.current_move[0] == "paper":
            return "win" if other_player_choice[0] == "rock" else "lose"
        else:
            return "win" if other_player_choice[0] == "paper" else "lose"

    # phase 1 of end-of-round logic
    def calculate_combat_modifiers(self, other_player: 'Player') -> None:
        self.result = self.round_result(other_player.current_move)
        self.backup_attributes()
        self.skillToFuncMap[self.current_move[1]](other_player)

        print(f"{self.name}'s code")
        print(self.current_health, other_player.current_health)
        print(self.current_move[1])
        print()

    def backup_attributes(self):
        self.backup_health = self.current_health
        self.backup_attack = self.current_attack

    def update_health(self, other_player: 'Player'):
        total_damage = 0
        random.seed(time.time())
        rng = random.random()

        # damage sources
        if rng > self.dodge_chance or self.block_damage:
            total_damage = other_player.backup_attack
            total_damage *= other_player.attack_modifier_percentage
            total_damage += other_player.attack_modifier_static
            total_damage += self.backup_attack * self.damage_reflection_percentage
            total_damage *= self.damage_modifier_percentage
        self.block_damage = False
        # regen sources
        total_damage -= self.current_health * self.health_modifier_percentage
        total_damage -= self.health_modifier_static

        self.current_health = min(self.current_health - total_damage, self.max_health)

    # if win: regen 3 HP over 3 turns (1hp per turn)
    # if lose: -1 to max health, min of 3
    def regen_logic(self, other_player: 'Player') -> None:
        if self.result == "win":
            # TO IMPLEMENT
            pass
        elif self.result == "lose":
            self.max_health = max(self.max_health - 1, 1)

    # if win: heal for 50% of max attack
    # if lose: lose 0.5 max attack, min of 1
    def leech_logic(self, other_player: 'Player') -> None:
        if self.result == "win":
            self.health_modifier_static = self.backup_attack * 0.5
        elif self.result == "lose":
            self.max_attack = max(self.max_attack - 0.5, 1)

    # if win: nothing special
    # if lose: reflect 50% of damage, take 25% more damage
    #           enemy takes enemy damage/2, you take 1.25*enemy damage
    def thorns_logic(self, other_player: 'Player') -> None:
        if self.result == "lose":
            self.damage_modifier_percentage = 1.25
            other_player.damage_reflection_percentage = 0.5

    # if win: 20% chance of missing
    # if lose: 30% chance of dodging
    def dodge_logic(self, other_player: 'Player') -> None:
        if self.result == "win":
            other_player.dodge_chance = 0.2
        elif self.result == "lose":
            self.dodge_chance = 0.3

    # if win: do only half damage, don't take damage next turn
    # if lose: nothing special
    def block_logic(self, other_player: 'Player') -> None:
        if self.result == "win":
            self.attack_modifier_percentage = 0.5
            self.block_damage = True

    # if win: do +3 attack
    # if tie: take +1 damage
    # if lose: take +1 damage
    def risk_logic(self, other_player: 'Player') -> None:
        if self.result == "win":
            self.attack_modifier_static += 3
        elif self.result == "tie":
            self.health_modifier_static -= 1
        elif self.result == "lose":
            self.health_modifier_static -= 1

    # if win: heal 2 health
    # if tie: heal 1 health
    # if lose: take +1 damage
    def heal_logic(self, other_player: 'Player') -> None:
        if self.result == "win":
            self.health_modifier_static += 2
        elif self.result == "tie":
            self.health_modifier_static += 1
        elif self.result == "lose":
            self.health_modifier_static -= 1

    # if win: nothing special
    # if lose: take 50% less damage, enemy deals +2 attack next turn if they win
    def insurance_logic(self, other_player: 'Player') -> None:
        if self.result == "lose":
            self.damage_modifier_percentage = 0.5
            # TO IMPLEMENT: enemy deals +2 attack next turn if win
