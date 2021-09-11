#Will make all of the info about pokemon such as their moves type ect
from damage_calc import *
from move import Move

class Pokemon():
    def __init__(self, name, level, hp, atk, special_atk, defense, special_def, speed, moves, types):
        self.name = name
        self.level = level
        self.hp = hp
        self.atk = atk
        self.special_atk = special_atk
        self.defense = defense
        self.special_def = special_def
        self.speed = speed
        self.moves = [Move(moves[0]), Move(moves[1]), Move(moves[2]), Move(moves[3])]
        self.type = (types[0], types[1])
        self.is_fainted = False
        self.available_moves = [0, 1, 2, 3]

    def take_damage(self, my_mon, move_data, weather):
        if (move_data.attack_type == 'physical'):
            damage = get_total_damage(my_mon.level, my_mon.type, move_data.type, self.type, my_mon.atk, self.defense, my_mon.speed, move_data.power, weather)
        else:
            damage = get_total_damage(my_mon.level, my_mon.type, move_data.type, self.type, my_mon.special_atk, self.special_def, my_mon.speed, move_data.power, weather)
        self.hp -= damage
        if self.hp <= 0:
            self.is_fainted = True
