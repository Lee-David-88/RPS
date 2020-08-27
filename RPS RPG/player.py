import random


class Player:
    rockSkills = []
    paperSkills = []
    scissorsSkills = []

    max_health = 0.0
    current_health = 0.0
    max_attack = 0.0
    current_attack = 0.0
    skillToFuncMap = {}
    blocked = False

    def __init__(self, num_skills: int = 0,
                 num_points: int = 0,
                 npc: bool = False,
                 skill_list: list = None,
                 skill_descriptions: dict = None):

        if skill_list is None:
            skill_list = []
        self.skill_list = skill_list
        self.map_functions()
        self.npc = npc
        self.max_health = 12.0
        self.max_attack = 2.0
        self.allocate_starting_points(num_points)
        self.pick_skills(num_skills, skill_descriptions)
        self.current_move = None
        self.result = None

    # assigns skills to functions regardless of order skills are in
    def map_functions(self) -> None:
        func_list = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")]
        for func in func_list:
            for skill in self.skill_list:
                if func.startswith(skill):
                    self.skillToFuncMap[skill] = self.lambda_generator(func)

    def lambda_generator(self, func: str):
        return lambda other_player: getattr(self, func)(other_player)

    def allocate_starting_points(self, num_points: int) -> None:
        if self.npc:
            for i in range(num_points):
                if random.randint(0, 1) == 0:
                    self.max_health += 2
                else:
                    self.max_attack += 1
        else:
            while num_points > 0:
                print("\"hp\" to add 2 health or \"attack\" to add 1 attack")
                print(f"current health: {self.max_health}, current attack: {self.max_attack}")
                choice = input(">: ")
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

    def pick_skills(self, num_skills: int, skill_descriptions: dict) -> None:
        chosen_skills = []
        remaining_skills = self.skill_list.copy()
        if self.npc:
            random.shuffle(remaining_skills)
            self.rockSkills = remaining_skills[0:2]
            self.paperSkills = remaining_skills[2:4]
            self.scissorsSkills = remaining_skills[4:6]
            return
        while num_skills > 0:
            self.print_skills(remaining_skills, skill_descriptions)
            while True:
                choice = input("Pick a skill: ").lower()
                if choice in remaining_skills:
                    chosen_skills.append(remaining_skills.pop(remaining_skills.index(choice)))
                    num_skills -= 1
                    break
                elif choice in self.skill_list:
                    print("You already picked this")
                else:
                    print("Invalid choice")
        random.shuffle(chosen_skills)
        self.rockSkills = chosen_skills[0:2]
        self.paperSkills = chosen_skills[2:4]
        self.scissorsSkills = chosen_skills[4:6]

    def print_skills(self, remaining_skills: list, skill_descriptions: dict) -> None:
        print("skills to pick from")
        for skill in remaining_skills:
            print(f"{skill.capitalize()} - {skill_descriptions[skill]}")

    def start_round(self) -> None:
        self.current_health = self.max_health
        self.current_attack = self.max_attack
        self.current_move = self.get_move()

    def round_result(self, other_player_choice: str) -> str:
        if self.current_move == other_player_choice:
            return "tie"
        elif self.current_move == "rock":
            return "win" if other_player_choice == "scissors" else "lose"
        elif self.current_move == "paper":
            return "win" if other_player_choice == "rock" else "lose"
        else:
            return "win" if other_player_choice == "paper" else "lose"

    def end_round(self, other_player: 'Player'):
        self.result = self.round_result(other_player.current_move)
        if self.result == "win":
            # self won, other_player lost
            print("win")
            other_player.result = "win"
            pass
        elif self.result == "lose":
            # self lost, other player won
            print("lose")
            other_player.result = "win"
            pass
        else:
            # tie
            print("tie")
            other_player.result = "tie"
            pass

    def get_move(self) -> str:
        choices = ["rock", "paper", "scissors"]
        if self.npc:
            return choices[random.randint(0, 2)]
        while True:
            choice = input("Enter a move of \"rock\", \"paper\", or \"scissors\": ")
            if choice.lower() in choices:
                return choice.lower()
            print("invalid choice")

    def regen_logic(self, other_player: 'Player'):
        if self.result == "win":
            self.current_health += 2
            other_player.current_health -= self.current_attack
        elif self.result == "tie":
            self.current_health += 1
        else:
            self.max_health -= 1
            self.current_health -= other_player.current_attack

    def leech_logic(self, other_player: 'Player'):
        if self.result == "win":
            self.current_health += self.current_attack / 2
        elif self.result == "lose":
            self.max_attack -= 0.5
            self.current_health -= other_player.current_attack

    def thorns_logic(self, other_player: 'Player'):
        if self.result == "lose":
            other_player.current_health -= other_player.current_attack / 2
            self.current_health -= other_player.current_attack * 1.25

    def dodge_logic(self, other_player: 'Player'):
        chance = random.randint(1, 10)
        if self.result == "win":
            if chance > 2:
                other_player.current_health -= self.current_attack
        elif self.result == "lose":
            if chance <= 3:
                self.current_health -= other_player.current_attack

    def block_logic(self, other_player: 'Player'):
        print("block")

    def risk_logic(self, other_player: 'Player'):
        if self.result == "win":
            other_player.current_health -= self.current_attack + 2
        elif self.result == "lose":
            self.current_health -= other_player.current_attack + 2

    def heal_logic(self, other_player: 'Player'):
        if self.result == "win":
            self.current_health += 2
            other_player.current_health -= self.current_attack
        elif self.result == "tie":
            self.current_health += 1
        else:
            self.current_health -= other_player.current_attack + 1

    def insurance_logic(self, other_player: 'Player'):
        print("insurance")
