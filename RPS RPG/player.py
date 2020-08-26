import random

class Player:
    rockSkills = []
    paperSkills = []
    scissorsSkills = []

    max_health = 0
    current_health = 0
    max_attack = 0
    current_attack = 0
    skillToFuncMap = {}

    def __init__(self, num_skills=0, num_points=0, npc=False, skill_list=None):
        if skill_list is None:
            skill_list = []
        self.map_functions(skill_list)
        self.npc = npc
        self.max_health = 12
        self.max_attack = 2
        self.allocate_starting_points(num_points)
        self.pick_skills(num_skills)
        self.current_move = None
        self.result = None

    def start_round(self):
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

    def end_round(self, other_player):
        self.result = self.round_result(other_player.current_move)
        if self.result == "win":
            # self won, other_player lost
            other_player.result = "win"
            pass
        elif self.result == "lose":
            # self lost, other player won
            other_player.result = "win"
            pass
        else:
            # tie
            other_player.result = "tie"
            pass

    # assigns skills to functions regardless of order skills are in
    def map_functions(self, skill_list):
        func_list = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")]
        for func in func_list:
            for skill in skill_list:
                if func.startswith(skill):
                    self.skillToFuncMap[skill] = self.lambda_generator(func)

    def lambda_generator(self, func):
        return lambda other_player: getattr(self, func)(other_player)

    def allocate_starting_points(self, num_points):
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

    def pick_skills(self, num_skills):
        if self.npc:
            pass

    def get_move(self):
        choices = ["rock", "paper", "scissors"]
        if self.npc:
            return choices[random.randint(0, 2)]
        while True:
            choice = input("Enter a move of \"rock\", \"paper\", or \"scissors\": ")
            if choice.lower() in choices:
                return choice.lower()
            print("invalid choice")

    def regen_logic(self, other_player):
        print("regen")

    def leech_logic(self, other_player):
        print("leech")

    def thorns_logic(self, other_player):
        print("thorns")

    def dodge_logic(self, other_player):
        print("dodge")

    def block_logic(self, other_player):
        print("block")

    def risk_logic(self, other_player):
        print("risk")

    def heal_logic(self, other_player):
        print("heal")
