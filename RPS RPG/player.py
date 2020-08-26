import random


class Player:
    rockSkills = []
    paperSkills = []
    scissorsSkills = []

    health = 0
    attack = 0

    def __init__(self, num_skills=0, num_points=0, npc=False, skill_list=[]):
        self.health = 12
        self.attack = 2
        self.allocate_starting_points(num_points, npc)
        self.pick_skills(num_skills, npc)

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
