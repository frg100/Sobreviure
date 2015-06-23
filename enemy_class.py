class enemy:
    def __init__(self,name,level,health):
        self.name = name
        self.level = level
        self.health = health
    def attack(self):
        print "A %r appears! It wants to fight!" % (self.name)
        player.weapon = (raw_input("What do you attack with? >>").lower())
        while (player.health > 0) or (self.health > 0):
            if (player.inventory.get(player.weapon) > 0):
                player.health = player.health - ( ( randint(0,5) ) +  attack_multiplier(self.level) )
                print "%r strikes! Your health is down to %r" %(self.name, player.health)
                if (player.health > 0) and (self.health > 0):
                    if weapon_probability() == "critical hit":
                        self.health -= (((randint(5,10))) +  (attack_multiplier(weapon_levels.get(player.weapon))) * 2)
                        print_slow( "Critical Hit!")
                    elif weapon_probability() == "hit":
                        self.health -=((((randint(2,5))) +  (attack_multiplier(weapon_levels.get(player.weapon)))))
                        print_slow( "Hit!")
                    elif weapon_probability() == "miss":
                        print_slow( "Miss")
                    print_slow("Enemy health down to %r !" % self.health )
                elif player.health <= 0:
                    print_slow("Your health...it's falling. You see a flash of light and a figure standing over you as your vision fades...You awake at your house, your bag empty. You wonder who she was...")
                    break
                elif self.health <= 0:
                    print_slow( "Enemy vanquished!")
                    break
            else:
                print "You don't have that!"
                player.weapon = (raw_input("What do you attack with? >>").lower())

