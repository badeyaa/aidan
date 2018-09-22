# keep these three import statements
import game_API
import fileinput
import json

# your import statements here
import random

first_line = True # DO NOT REMOVE

# global variables or other functions can go here
stances = ["Rock", "Paper", "Scissors"]

path = [10, 9, 8, 14, 19, 23, 24, 23, 19, 20]
idx = 0
waited = False

def get_winning_stance(stance):
    if stance == "Rock":
        return "Paper"
    elif stance == "Paper":
        return "Scissors"
    elif stance == "Scissors":
        return "Rock"

# main player script logic
# DO NOT CHANGE BELOW ----------------------------
for line in fileinput.input():
    if first_line:
        game = game_API.Game(json.loads(line))
        first_line = False
        continue
    game.update(json.loads(line))
# DO NOT CHANGE ABOVE ---------------------------

    # code in this block will be executed each turn of the game

    me = game.get_self()

    if me.location == me.destination and idx < len(path): # check if we have moved this turn
        if me.location == 8:
            destination_node = 9
            idx += 1
        else:
            destination_node = path[idx]
            idx += 1
    elif me.location == 8 and destination_node == 9:
        destination_node = 14
    else:
        destination_node = me.destination

    if game.has_monster(me.location):
        # if there's a monster at my location, choose the stance that damages that monster
        chosen_stance = get_winning_stance(game.get_monster(me.location).stance)
    else:
        # otherwise, pick a random stance
        chosen_stance = stances[random.randint(0, 2)]
    if me.movement_counter == me.speed + 1:
        if game.has_monster(destination_node):
            monster = game.get_monster(destination_node)
            chosen_stance = get_winning_stance(monster.stance)

    # submit your decision for the turn (This function should be called exactly once per turn)
    game.submit_decision(destination_node, chosen_stance)
