from trainer import Trainer

class Battle():
    def __init__(self, team1, team2):
        self.trainers = [Trainer(team1), Trainer(team2)]
        self.weather = 'clear'
        self.current_trainer = 0
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

'''
battle.prt_pp(3)
#Uses move 3(which is really 4) on the opponents current pokemon
battle.use_move(battle.trainers[0], battle.trainers[1], 3)
battle.prt_pp(3)
print('+------------------+')'''