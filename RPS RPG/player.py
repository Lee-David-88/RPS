import random


class Player:
    rockSkills = []
    paperSkills = []
    scissorsSkills = []

    health = 0
    attack = 0
    skillToFuncMap = {}

    def __init__(self, num_skills=0, num_points=0, npc=False, skill_list=None):
        if skill_list is None:
            skill_list = []
        self.map_functions(skill_list)

        self.health = 12
        self.attack = 2
        self.allocate_starting_points(num_points, npc)
        self.pick_skills(num_skills, npc)

    # assigns skills to functions regardless of order skills are in
    def map_functions(self, skill_list):
        func_list = [func for func in dir(self) if callable(getattr(self, func)) and not func.startswith("__")]
        for func in func_list:
            for skill in skill_list:
                if func.startswith(skill):
                    self.skillToFuncMap[skill] = self.lambda_generator(func)

    def lambda_generator(self, func):
        return lambda: getattr(self, func)()

    def allocate_starting_points(self, num_points, npc):
        if npc:
            for i in range(num_points):
                if random.randint(0, 1) == 0:
                    self.health += 2
                else:
                    self.attack += 1
        else:
            while num_points > 0:
                print("\"hp\" to add 2 health or \"attack\" to add 1 attack")
                print(f"current health: {self.health}, current attack: {self.attack}")
                choice = input()
                if choice.lower() == "hp":
                    self.health += 2
                    print("added 2 to health")
                elif choice.lower() == "attack":
                    self.attack += 1
                    print("added 1 to attack")
                else:
                    print("Invalid choice, please choose either \"hp\" or \"attack\"")
                    num_points += 1
                num_points -= 1

    def pick_skills(self, num_skills, npc):
        if npc:
            pass

    def regen_logic(self):
        print("regen")

    def leech_logic(self):
        print("leech")

    def thorns_logic(self):
        print("thorns")

    def dodge_logic(self):
        print("dodge")

    def block_logic(self):
        print("block")

    def risk_logic(self):
        print("risk")

    def heal_logic(self):
        print("heal")
