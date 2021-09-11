#imports the pokemon class to construct classes for all 6 pokemon which will be taken from the team.json file
from pokemon import Pokemon
import json
import random

class Trainer():
    def __init__(self, team_name):
        #opens the teams json file and gets all info from it
        with open('./teams/'+ team_name + ".json") as json_data:
            team_data = json.load(json_data)
        #creates a list that stores all pokemon from the team json as objects
        self.pokemon = []
        #creates the right ammount of pokemon
        for x in range(team_data['size']):
            mon = team_data[str(x+1)]
            self.pokemon.append(Pokemon(mon['name'], mon['level'], mon['hp'], mon['atk'], mon['special atk'], mon['def'], mon['special def'], mon['speed'], mon['moves'], mon['types']))
        self.current_mon = 0

    #example of accessing move data
    #self.pokemon[1].moves[0].pp
    def make_move(self, move_num, op_mon, weather='clear'):
        randnum = random.randint(0, 100)
        if (randnum <= self.pokemon[self.current_mon].moves[move_num].accuracy):
            op_mon.take_damage(self.pokemon[self.current_mon], self.pokemon[self.current_mon].moves[move_num], weather)


    def prt(self):
        print(self.pokemon[1].moves[0].pp)