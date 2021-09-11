import json
class Move():
    def __init__(self, move_name):
        with open("./moves/"+ move_name + ".json") as json_data:
            move_data = json.load(json_data)
        self.name = move_data['name']
        self.power = move_data['power']
        self.type = move_data['type']
        self.attack_type = move_data['attack type']
        self.pp = move_data['pp']
        self.accuracy = move_data['accuracy']