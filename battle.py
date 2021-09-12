from trainer import Trainer
import random

class Battle():
    def __init__(self, team1, team2):
        self.trainers = [Trainer(team1), Trainer(team2)]
        self.weather = 'clear'
        self.current_trainer = 0
        self.phase_data = []
        print("Trainers Created")

    def use_move(self, attacking_trainer, deffending_trainer, move_number):
        ##This is used if the move does physical or special damage to another pokemon
        if (attacking_trainer.pokemon[attacking_trainer.current_mon].moves[move_number].attack_type == 'physical' or 'special'):
            attacking_trainer.make_move(move_number, deffending_trainer.pokemon[deffending_trainer.current_mon], self.weather)
            attacking_trainer.pokemon[attacking_trainer.current_mon].moves[move_number].pp -= 1

    def prt_hp(self):
        print('Trainer 1: '+ str(self.trainers[0].pokemon[self.trainers[0].current_mon].hp))
        print('Trainer 2: '+ str(self.trainers[1].pokemon[self.trainers[1].current_mon].hp))

    def prt_pp(self, move_num):
        print('Selected move: '+ str(self.trainers[0].pokemon[self.trainers[0].current_mon].moves[move_num].pp))

    def do_phase(self):
        #format phase data as [['a', 1],['s', 5]
        #Handles switches first
        switch1 = False
        switch2 = False
        if (self.phase_data[0][0] == 's'):
            self.trainers[0].current_mon = self.phase_data[0][1]
            switch1 = True
        if (self.phase_data[1][0] == 's'):
            self.trainers[1].current_mon = self.phase_data[1][1]
            switch2 = True
        #Determine who goes first
        first = 0
        if (self.trainers[0].pokemon[self.trainers[0].current_mon].speed == self.trainers[1].pokemon[self.trainers[1].current_mon].speed): #If same speed
            rand = random.randint(0, 1)
            if (rand == 0):
                pkmn1 = self.trainers[0].pokemon[self.trainers[0].current_mon]
                pkmn2 = self.trainers[1].pokemon[self.trainers[1].current_mon]
            else:
                pkmn1 = self.trainers[1].pokemon[self.trainers[1].current_mon]
                pkmn2 = self.trainers[0].pokemon[self.trainers[0].current_mon]
                first = 1
        elif(self.trainers[0].pokemon[self.trainers[0].current_mon].speed > self.trainers[1].pokemon[self.trainers[1].current_mon].speed):
            pkmn1 = self.trainers[0].pokemon[self.trainers[0].current_mon]
            pkmn2 = self.trainers[1].pokemon[self.trainers[1].current_mon]
        else:
            pkmn1 = self.trainers[1].pokemon[self.trainers[1].current_mon]
            pkmn2 = self.trainers[0].pokemon[self.trainers[0].current_mon]
            first = 1
        #Who goes first based on speed
        if (first == 0):
            if (switch1 == False): #If the pokemon didnt switch attack
                self.use_move(self.trainers[0], self.trainers[1], self.phase_data[0][1])
            #If the pokemon is not fainted and they did not switch attack
            if (self.trainers[1].pokemon[self.trainers[1].current_mon].is_fainted == False and switch2 == False):
                self.use_move(self.trainers[1], self.trainers[0], self.phase_data[1][1])
        else:
            if (switch2 == False): #If the pokemon didnt switch attack
                self.use_move(self.trainers[1], self.trainers[0], self.phase_data[1][1])
            #If the pokemon is not fainted and they did not switch attack
            if (self.trainers[1].pokemon[self.trainers[1].current_mon].is_fainted == False and switch1 == False):
                self.use_move(self.trainers[0], self.trainers[1], self.phase_data[0][1])
        self.phase_data = []

#battle.use_move(battle.trainers[0], battle.trainers[1], 3)