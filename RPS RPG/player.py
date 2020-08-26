import random


class Player:
    rockSkills = []
    paperSkills = []
    scissorsSkills = []

    def __init__(self, num_skills, npc=False):
        self.pick_skills(num_skills, npc)

    def pick_skills(self, num_skills, npc):
        if npc:
            pass
