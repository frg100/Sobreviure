class user:
    time_advance = True
    bow_message = False
    hunt_message = False
    can_hunt = False
    exploration1_message = False
    sword_message = False
    can_go_to_town = False
    health = 100
    weapon = "hand"
    energy = 100
    exploration_count = 0
    town_count = 0
    money = 0
    inventory = { "bow" : 0, "fur" : 0, "stones" : 0, "meat" : 0, "pelt" : 0, "string" : 0, "sticks" : 0, "arrow" : 0, "cooked meat" : 0, "sword" : 0, "dagger" : 0, "heal_potion" : 0}
    def __init__(self):
        pass
