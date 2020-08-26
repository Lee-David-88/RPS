import random


class Player:
    rockSkills = []
    paperSkills = []
    scissorsSkills = []

    # should I add temp attack for one round only ?
    max_health = 0
    health = max_health
    attack = 0

    def __init__(self, num_skills=0, num_points=0, npc=False, skill_list=[]):
        self.skillToFuncMap = {skill_list[0]: lambda: self.skill1(),
                               skill_list[1]: lambda: self.skill2(),
                               skill_list[2]: lambda: self.skill3(),
                               skill_list[3]: lambda: self.skill4(),
                               skill_list[4]: lambda: self.skill5(),
                               skill_list[5]: lambda: self.skill6(),
                               skill_list[6]: lambda: self.skill7()}

        self.skillToFuncMap[skill_list[1]]()
        self.max_health = 12.0
        self.attack = 2.0
        self.allocate_starting_points(num_points, npc)
        self.pick_skills(num_skills, npc)

    def skill1(self, result):
        if result == "Win" or "Tie":
            self.health += 1
        elif result == "Lose":
            self.max_health -= 1

    def skill2(self, result):
        if result == "Win":
            self.health += self.attack / 2
        elif result == "Lose":
            self.attack -= 0.5

    def skill3(self, result):
        if result == "Lose":
            self.attack += 0

    def skill4(self, result):
        chance = random.randint(1, 100)
        if result == "Win":
            if chance <= 20:
                self.attack = 0
        elif result == "Lose":
            if chance <= 30:
                self.health -= 0

    def allocate_starting_points(self, num_points, npc):
        if npc:
            for i in range(num_points):
                if random.randint(0, 1) == 0:
                    self.max_health += 2
                else:
                    self.attack += 1
        else:
            while num_points > 0:
                print("\"hp\" to add 2 health or \"attack\" to add 1 attack")
                print(f"current health: {self.max_health}, current attack: {self.attack}")
                choice = input()
                if choice.lower() == "hp":
                    self.max_health += 2
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
