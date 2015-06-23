class fight_dungeon:
    def __init___(self,enemy_list,message):
        global encounter
    	global hours
    	print_slow( message)
    	while (encounter < 3) and (player.health > 0):
            random_enemy = choice(enemy_list)
            enemy = random_enemy()
            enemy.attack()
            if player.health > 0:
                print "You have %r potions in your inventory" %(player.inventory.get("heal_potion"))
                heal(int(raw_input("How many potions would you like to consume? >>").lower()))
            else:
                pass
            encounter = encounter + 1
            hours += 1
        else:
            prize = "$ %r" % randint(10,100)
            print_slow ("You see daylight...Finally you're out...The creature you just defeated dropped its bag...It had %r inside!" % prize)
            print_slow ("You head back home...")
        encounter = 0





class fight_dungeon1(fight_dungeon):
    def __init__(self):
        fight_dungeon.__init__(self,[wizard,troll,bat,bandit], "You find a mysterious cave on the side of the mountain...Its pull is too strong...\n")

class fight_dungeon2(fight_dungeon):
    def __init__(self):
        fight_dungeon.__init__(self,[hydra,goblin,wizard,bat], "You come across a small castle that seems to be abandones...there might be treasure inside...\n")

