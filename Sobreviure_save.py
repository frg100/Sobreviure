__author__ = 'frg100'

#!/usr/bin/env python2.7
# coding: utf-8
from random import randint
from random import choice
#import pickle
import sys
import time


from tinydb import TinyDB, where
from user_class import user
from enemy_class import enemy
from enemies_classes import wizard, troll, bat, bandit, hydra, goblin
from fight_dungeons import fight_dungeon, fight_dungeon1, fight_dungeon2
import json
import ast
'''
import pdb
pdb.set_trace()
'''

def print_slow(str):
    print str
    '''
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    '''

intro = """
        You wake up one day...no idea of where you are.\n
        You wake in a cottage in the woods with a fire burning...
        You have no idea of how you got there. \n
        For now, you must try to survive by gathering. \n
        Type help for more options
        """
print_slow(intro)


crafting_possibilities = {"sticks" : "string",
                          "string" : "sticks",
                          "sticks" : "stones",
                          "stones" : "sticks"}

product_dict = {"sticksstring" : "bow",
                "stringsticks" : "bow",
                "sticksstones" : "arrow",
                "stonessticks" : "arrow"}

forging_cost = {"sword" : 100,
                "dagger": 20}

market_cost = {"cooked meat" : 15,
               "pelt" : 20,
                "heal potion" : 20}

market_sell = {"cooked meat" : 5,
               "pelt" : 10,
               "sticks" : 0.25,
               "stones" : 0.25,
               "bow" : 2.5,
               "arrow": 0.5,
               "meat": 2.5,
               "fur" : 0.25,
               "string" : 0.25,
               "sword" : 50,
               "dagger" : 10}

weapon_levels = {"hand" : 0,
                 "bow" : 1,
                 "sword" : 1}
hours = 0
encounter = 0

name_input = str(raw_input("\nWhat is your name? >>"))
print_slow("So my name is %s"  %name_input)
player = user()

def save():
    db = TinyDB('db.json')
    player_stats = db.table(name_input)
    if db.get(where('name') == name_input):
        player_stats.update({'time_advance' : player.time_advance}, eids=[1])
        player_stats.update({'bow_message': player.bow_message}, eids=[2])
        player_stats.update({'hunt_message': player.hunt_message}, eids=[3])
        player_stats.update({'can_hunt': player.can_hunt}, eids=[4])
        player_stats.update({'exploration1_message': player.exploration1_message}, eids=[5])
        player_stats.update({'sword_message': player.sword_message}, eids=[6])
        player_stats.update({'can_go_to_town': player.can_go_to_town}, eids=[7])
        player_stats.update({'health': player.health}, eids=[8])
        player_stats.update({'weapon': player.weapon}, eids=[9])
        player_stats.update({'energy': player.energy}, eids=[10])
        player_stats.update({'exploration_count': player.exploration_count}, eids=[11])
        player_stats.update({'town_count': player.town_count}, eids=[12])
        player_stats.update({'money': player.money}, eids=[13])
        player_stats.update(player.inventory, eids=[14])
        print "Saved"

    else:
        player_stats.insert({'time_advance' : player.time_advance})
        player_stats.insert({'bow_message': player.bow_message})
        player_stats.insert({'hunt_message': player.hunt_message})
        player_stats.insert({'can_hunt': player.can_hunt})
        player_stats.insert({'exploration1_message': player.exploration1_message})
        player_stats.insert({'sword_message': player.sword_message})
        player_stats.insert({'can_go_to_town': player.can_go_to_town})
        player_stats.insert({'health': player.health})
        player_stats.insert({'weapon': player.weapon})
        player_stats.insert({'energy': player.energy})
        player_stats.insert({'exploration_count': player.exploration_count})
        player_stats.insert({'town_count': player.town_count})
        player_stats.insert({'money': player.money})
        player_stats.insert(player.inventory)
        db.insert({'name' : name_input})
        print "First save"



def load():
    db = TinyDB('db.json')
    player_stats = db.table(name_input)
    player.time_advance = (player_stats.get(eid=1))['time_advance']
    player.bow_message = (player_stats.get(eid=2))['bow_message']
    player.hunt_message = (player_stats.get(eid=3))['hunt_message']
    player.can_hunt = (player_stats.get(eid=4))['can_hunt']
    player.exploration1_message = (player_stats.get(eid=5))['exploration1_message']
    player.sword_message = (player_stats.get(eid=6))['sword_message']
    player.can_go_to_town = (player_stats.get(eid=7))['can_go_to_town']
    player.health = (player_stats.get(eid=8))['health']
    player.weapon = (player_stats.get(eid=9))['weapon']
    player.energy = (player_stats.get(eid=10))['energy']
    player.exploration_count = (player_stats.get(eid=11))['exploration_count']
    player.town_count = (player_stats.get(eid=12))['town_count']
    player.money = (player_stats.get(eid=13))['money']
    player.inventory = player_stats.get(eid=14)
    print "Your inventory has %r" %player.inventory





#DUNGEONS
#REMOVE THE TIME_ADVANCE = FALSE WHEN DUNGEONS ARE READY
def dungeon1():
    dungeon1_script = '''
You are walking through the woods and you see an old man walk by y ...\n 
He comes up to you and asks you who you are. \n 
He introduces himself as the Wanderer. \n 
He says he's helpful and can give you advice. \n 
Then he disappears back into the forest. \n \n 
You are tired from your journey and head back home.\n
                      '''
    print_slow(dungeon1_script)

def dungeon2():
    dungeon2_script = '''
You are walking through the woods and you come across the Wanderer again. \n
He says he can show you the Town. \n
"Here is the blacksmith where you can forge strong items... \n
Here is the market where you can buy or sell wares...\n
Here is the inn where you can recuperate your energy." \n
You thank him for his help. \n
"I'm only here to help" He says. \n
He tips his hat and walks away, his bag slung over his shoulder.\n\n
You are tired from your journey and head back home.\n
You can now travel to "town"\n
                      '''
    print_slow(dungeon2_script)
    player.can_go_to_town = True



#DUNGEONS



def heal(quantity):
    if (player.inventory.get("heal_potion") >= quantity) and (quantity > 0):
        player.health += (quantity * 20)
        player.inventory["heal_potion"] = (player.inventory.get("heal_potion") - quantity)
        print "\nYour health is %r" %(player.health)
    elif quantity == 0:
        print "\nNo potions consumed"
    else:
        print "You don't have that many potions"
        print "You have %r potions in inventory" %(player.inventory.get("heal_potion"))

def weapon_probability():
    roller = randint(0, 100)
    if roller > 81:
        return "critical hit"
    elif roller < 24:
        return "miss"
    else:
        return "hit"

def attack_multiplier(level):
    if level == 1:
        return 0
    elif level == 2:
        return 1
    elif level == 3:
        return 3
    elif level == 4:
        return 6
    elif level == 5:
        return 10
    elif level == 6:
        return 14
    elif level == 7:
        return 20


#CRAFTING FUNCTION
def craft(input1, input2, quantity):
    if (crafting_possibilities.get(input1) == input2\
        or crafting_possibilities.get(input2) == input1)\
        and (player.inventory.get(input1) > 0\
        and player.inventory.get(input2) > 0):

        mid_product = str(input1) + str(input2)
        product = product_dict.get(mid_product)
        player.inventory[str(input1)] = (player.inventory.get(str(input1)) - (1 * int(quantity)))
        player.inventory[str(input2)] = (player.inventory.get(str(input2)) - (1 * int(quantity)))
        if ((player.inventory.get(input1) >= 0) and (player.inventory.get(input1) >= 0)):
            player.inventory[product] = (player.inventory.get(product) + (1 * int(quantity)))
            print "\nYou turned %r %r and %r %r into %r %r" %(str(quantity), input1, str(quantity), input2, str(quantity), product)
        else:
            player.inventory[str(input1)] = (player.inventory.get(str(input1)) + (1 * int(quantity)))
            player.inventory[str(input2)] = (player.inventory.get(str(input2)) + (1 * int(quantity)))
            print "You don't have enough materials!"
            player.time_advance = False
    elif (crafting_possibilities.get(input1) != input2) and (player.inventory.get(input1) > 0 and player.inventory.get(input2) > 0):
        print "Error1"
    else:
        print "\nUnable to craft"
        player.time_advance = False
#Prevents time from going on if you didnt make anything
#CRAFTING FUNCTION



#FORGING FUNCTION
def forge(tool):
    forge_cost = (forging_cost.get(tool))
    if forge_cost < player.money:
        try:
            player.money = player.money - forge_cost
            player.inventory[tool] = (player.inventory.get(tool) + 1)
        except ValueError:
            print "Invalid"
            player.time_advance = False
        except TypeError:
            print "Invalid"
            player.time_advance = False
    else:
        print "Not enough money"
        player.time_advance = False
    print "\nYou have %r money" %player.money
#FORGING FUNCTION



#MARKET FUNCTION
def buy(action, ware):
    try:
        try:
            ware_quantity = (int(raw_input("How many? >>")))
        except ValueError:
            print "Invalid"
        try:
            buy_cost = (ware_quantity)*(market_cost.get(ware))
            if (action == "buy") and (buy_cost > player.money):
                buy_cost = (ware_quantity)*(market_cost.get(ware))
                player.money = player.money - buy_cost
                player.inventory[ware] = (player.inventory.get(ware) + ware_quantity)
            elif action == "sell":
                sell_cost = (ware_quantity)*(market_sell.get(ware))
                player.money = player.money + sell_cost
                player.inventory[ware] = (player.inventory.get(ware) - ware_quantity)
        except ValueError:
            print "Invalid"
            player.time_advance = 0
        print "You have %r money" %player.money
    except UnboundLocalError:
        print "Invalid"
#MARKET FUNCTION



#EATING FUNCTION
def eat(quantity):
    player.time_advance = False
    if player.energy < 200:
        if player.inventory.get("cooked meat") > 0:
            if (player.inventory.get("cooked meat") >= quantity) and (quantity > 0) and player.energy + (quantity * 20) < 200:
                player.energy = player.energy + (quantity * 20)
                player.inventory["cooked meat"] = (player.inventory.get("cooked meat") - quantity)
                print "\nYour energy is %r" %(player.energy)
            elif (player.inventory.get("cooked meat") >= quantity) and (quantity > 0) and player.energy + (quantity * 20) > 200:
                player.energy = 200
                player.inventory["cooked meat"] = (player.inventory.get("cooked meat") - quantity)
                print "\nYour energy is %r" %(player.energy)
            elif quantity == 0:
                print "\nNo cooked meat consumed"
                player.time_advance = False
            else:
                print "You dont have that much cooked meat"
                print "You have %r cooked meat in inventory" %(player.inventory.get("cooked meat"))
                player.time_advance = False
        else:
            if (player.inventory.get("meat") >= quantity) and (quantity > 0) and player.energy + (quantity * 10) < 200:
                player.energy = player.energy + (quantity * 10)
                player.inventory["meat"] = (player.inventory.get("meat") - quantity)
                print "\nYour energy is %r" %(player.energy)
            elif quantity == 0:
                print "\nNo meat consumed"
                player.time_advance = False
            else:
                print "You dont have that much meat"
                print "You have %r meat in inventory" %(player.inventory.get("meat"))
                player.time_advance = False
    else:
        print "You already have full energy!"
#EATING FUNCTION












#MAIN LOOP
while hours <= 168:
# to keep the game going until time is up(7 days or 168 hours have gone by)


    print "----------------------------------------------------------------"
    command = raw_input("Enter a command >> ").lower()
#asks for a command(help, gather, hunt, craft, exit)



#HELP SECTION
    if command == "help":
        player.time_advance = False
        print "This is the help section.\
               Type the field you want to know more about:\
               \n\t*Craft \n\t*Gather \n\t*Hunt \n\t*Exit\
               \n\t*Cook \n\t*Explore \n\t*Eat \n\t*Town \n\t*Inventory"
        category = raw_input("\nEnter Help category: ").lower()
        if category == "craft":
            print "\n***Crafting is the way to make more complicated tools.\
                  To craft, type in 'craft' and press enter. \
                  Then type in the items you want to craft.\
                  Eg. sticks and string make bow. Crafting takes 1 hour.***"
        elif category == "gather":
            print "\n***Gathering is a way to quickly get common resources.\
                  You might get sticks, fur, or stones.\
                  Gathering takes 1 hour***"
        elif category == "hunt":
            print "\n***Hunting is a command that takes longer,\
                  from 2-4 hours.\
                  When you hunt you can get meat or pelts.***"
        elif category == "cook":
            print "\n***Cooking is a command that takes 1 hour.\
                  Cooking turns meat into cooked meat which gives \
                  you 2X the energy.***"
        elif category == "exit":
            print '\n***The "exit" command lets you exit the game***'
        elif category == "inventory":
            print "\n***You can access your inventory by typing:\
                  'inventory'***"
        elif category == "explore":
            print "\n***Once you have 10 cooked meat you can go exploring.\
                  You can go North, South, East, and West.\
                  When you explore you can fight enemies and get \
                  rewards at the end of the dungeon.\
                  Heal potions are always good to have. \
                  You can get them at the market.***"
        elif category == "eat":
            print "\n***To recuperate your energy,\
                  you can eat meat for 10 energy or cooked meat\
                  (if you have it) for 20 energy.***"
        elif category == "town":
            print "\n***Once you discover the town, you can go\
                  to the Blacksmith, the Market, the Inn, or you\
                  can talk to the people.***"
        else:
            print "\nThis is not a help topic"
#HELP SECTION

    elif command == "exit":
        break

#GATHER SECTION
    elif command == "gather":
        player.time_advance = True
        random_sticks = randint(3, 15)
        player.inventory["sticks"] = (player.inventory.get("sticks") + random_sticks)
        random_fur = randint(3, 15)
        player.inventory["fur"] = (player.inventory.get("fur") + random_fur)
        random_stones = randint(3, 15)
        player.inventory["stones"] = (player.inventory.get("stones") + random_stones)
        random_string = randint(1, 6)
        player.inventory["string"] = (player.inventory.get("string") + random_string)
        print "\nYou gathered %r sticks, %r fur, %r string and %r stones" %(random_sticks, random_fur, random_string, random_stones)
#GATHER SECTION



#HUNT SECTION
    elif (command == "hunt") and (player.can_hunt == True):
        hunt_time = randint(2, 4)
        if player.inventory.get("arrow") >= hunt_time:
            print "\nHunting takes you " + str(hunt_time + 1) + " hours"
            random_meat = randint(3, 9)
            player.inventory["meat"] = (player.inventory.get("meat") + random_meat)
            random_pelt = randint(0, 2)
            player.inventory["pelt"] = (player.inventory.get("pelt") + random_pelt)
            print "\nYou got %r meat and %r pelt" %(random_meat, random_pelt)
            hours = hours + hunt_time
            player.energy = player.energy - (hunt_time * 5)
            player.time_advance = True
            player.inventory["arrow"] = (player.inventory.get("arrow") - hunt_time)
        elif player.inventory.get("arrow") < hunt_time:
            print "You don't have enough arrows!"
            player.time_advance = False

#IDEA: ASK USER FOR HOURS SPENT HUNTING AND INCREASE PROBABILITY OF HIGH REWARDS AS TIME GOES UP (0-1 PELTS FOR 1 HOUR AND 2-4 FOR 6 HOURS)
#HUNT SECTION



#COOK SECTION
    elif command == "cook":
        print "\nYou have %r meat in inventory" %(player.inventory.get("meat"))
        player.time_advance = True
        try:
            meat_cooked = (int(raw_input("\nHow much meat would you like to cook? >>")))
        except ValueError:
            print "Invalid"
            meat_cooked = 0
        if (player.inventory.get("meat") >= meat_cooked) and (meat_cooked > 0):
            player.inventory["meat"] = (player.inventory.get("meat") - meat_cooked)
            player.inventory["cooked meat"] = (player.inventory.get("cooked meat") + meat_cooked)
            print "\nYou have %r cooked meat in inventory" %(player.inventory.get("cooked meat"))
        elif meat_cooked == 0:
            print "\nNo meat cooked"
        else:
            print "You dont have that much meat"
#COOK SECTION



#INVENTORY
    elif command == "inventory":
        print "\nYour inventory includes: " + str(player.inventory)
        player.time_advance = False
#INVENTORY



#EXPLORATION
    elif (command == "explore") and (player.inventory.get("cooked meat") >= 10):
        player.inventory["cooked meat"] = (player.inventory.get("cooked meat") - 10)
        direction = (raw_input("What direction would you like to go in?\
                 \n\t*North \n\t*East \n\t*South \n\t*West\n>>").lower())
        if player.exploration_count == 0:
            dungeon1()
            player.exploration_count = 1
        elif player.exploration_count == 1:
            dungeon2()
            player.exploration_count = 2
        elif (direction == "north") and (player.inventory.get("sword") > 0):
            fight_dungeon1.__init__(self)
            player.exploration_count = player.exploration_count + 1
        elif (direction == "east") and (player.inventory.get("sword") > 0):
            fight_dungeon2.__init__(self)
            player.exploration_count = player.exploration_count + 1
        elif (direction == "west") and (player.inventory.get("sword") > 0):
            fight_dungeon3()
            player.exploration_count = player.exploration_count + 1
        elif (direction == "south") and (player.inventory.get("sword") > 0):
            fight_dungeon4()
            player.exploration_count = player.exploration_count + 1
#EXPLORATION



#EATING
    elif command == "eat":
        print "You have %r meat and %r cooked meat in inventory" %(player.inventory.get("meat"), player.inventory.get("cooked meat"))
        if player.inventory.get("cooked meat") > 0:
            try:
                eat(int(raw_input("\nHow much cooked meat would you like to eat? >>")))
            except ValueError:
                print "Invalid"
                cooked_meat_consumed = 0
        else:
            try:
                eat(int(raw_input("\nHow much meat would you like to eat? >>")))
            except ValueError:
                print "Invalid"
                meat_consumed = 0

#EATING
    elif command == "suicide":
        print "https://sites.google.com/site/readslaughterhousefive/about-slaughterhouse-five/favorite-quotes"


#STORY
    elif (command == "town") and (player.exploration_count == 1):
        print '''\n"It's a shame...he was only 17" \
                 \nYou overhear a conversation as you approach the \
                 crowd huddled over a dead body; poisoned with darkness.\
                 \n You approach one of the villagers and ask what\
                 happened\n "No one knows" He says, "The blacksmith's\
                 son found him like this this morning." \n Yo\
                 u get a wierd feeling in your stomach...'''
        building = raw_input("\nWhere do you want to do? \n\t*Market\
                        \n\t*Blacksmith \n\t*Inn \n\t*Talk\n>> ").lower()
        if building == "market":
            buy((raw_input("\nBuy or sell? >>").lower()), (raw_input("\nWhat? >>").lower()))
        elif building == "blacksmith":
            forge(raw_input("The blacksmith asks you: 'What would \
                             you like to forge? >>'").lower())
        elif building == "inn":
            inn_rest = (raw_input("Would you like to stay a night? The price is 50 >>").lower())
            try:
                if inn_rest == "yes":
                    player.energy = 100
                    player.money = player.money - 50
                elif inn_rest == "no":
                    player.time_advance = False
            except ValueError:
                print "Invalid"
                player.time_advance = False
#STORY

#SAVE
    elif command == "save":
        save()
#SAVE

#LOAD
    elif command == "load":
        load()
#LOAD




#TOWN
    elif (command == "town") and (player.can_go_to_town == True):
        building = raw_input("Where do you want to do? \n\t*Market \n\t*Blacksmith \n\t*Inn \n\t*Talk\n>> ").lower()
        if building == "market":
            print "Your inventory is" + str(player.inventory)
            buy((raw_input("\nBuy or sell? >>").lower()), (raw_input("\nWhat? >>").lower()))
        elif building == "blacksmith":
            forge(raw_input("The blacksmith asks you: 'What would you like to forge? >>'").lower())
        elif building == "inn":
            inn_rest = (raw_input("Would you like to stay a night? The price is 50 >>").lower())
            try:
                if inn_rest == "yes":
                    player.energy = 105
                    player.money = player.money - 50
                elif inn_rest == "no":
                    player.time_advance = False
            except ValueError:
                print "Invalid"
                player.time_advance = False
        #elif building == "talk"

#TOWN



#CRAFT SECTION
    elif command == "craft":
        player.time_advance = True
        craft(str(raw_input("Enter first item >>").lower()), str(raw_input("Enter second item >>").lower()), raw_input("How many?>>").lower())
# call the craft function with 2 user inputs
#CRAFT SECTION



#EXIT GAME
    elif command == "exit":
        print "Thanks for playing!"
        break
#Break stops the while loop
#EXIT GAME



#INVALID COMMAND
    else:
        print "\nYou can't do this"
        player.time_advance = False
#INVALID COMMAND


#ACHIEVEMENTS
    if (player.bow_message == False) and (player.inventory.get("sticks") > 5) and (player.inventory.get("string") > 5):
        print_slow("You have sticks and string....Maybe they could be crafted into something more useful...\n")
        player.bow_message = True
    else:
        print ""

    if (player.hunt_message == False) and (player.inventory.get("bow") > 0):
        print_slow("You now have a bow...You can now 'Hunt'\n")
        player.hunt_message = True
        player.can_hunt = True
    else:
        print ""

    if (player.exploration1_message == False) and (player.inventory.get("cooked meat") > 10):
        print_slow('''You have enough cooked meat (10) to go exploring! You can now "Explore"...\n''')
        player.exploration1_message = True
    else:
        print ""

    if (player.sword_message == False) and (player.inventory.get("sword") > 0):
        print_slow("You have forged a mighty sword! You can now explore deeper into the woods. You might want to buy some potions at the market.\n")
        player.sword_message = True
#ACHIEVEMENTS

#TIME ADVANCE TRUE
    if player.time_advance == True:
        player.energy = player.energy - 5
        print "Energy is %r" %(player.energy)
#TIME ADVANCE TRUE



        hours = hours + 1
        print "\nThe time is: " + str(hours)
    else:
        print "\nThe time is: " + str(hours)

    if player.energy <= 0:
        print_slow("Starvation's cold hand clutches you...The world fades away..........\n")
        break
    else: print "\n"
