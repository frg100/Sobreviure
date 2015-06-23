from enemy_class import enemy




class wizard(enemy):
    def __init__(self):
        enemy.__init__(self, "Wizard", 2, 30)
class troll(enemy):
    def __init__(self):
        enemy.__init__(self, "Troll", 2, 50)
class bat(enemy):
    def __init__(self):
        enemy.__init__(self, "Bat", 1, 15)
class bandit(enemy):
    def __init__(self):
        enemy.__init__(self, "Bandit", 1, 20)
class hydra(enemy):
    def __init__(self):
        enemy.__init__(self, "Hydra", 1, 15)
class goblin(enemy):
    def __init__(self):
        enemy.__init__(self, "Goblin",2, 25)

