import random
#Type match up chart used like a cordinate plane to find the multiplier
types = [
    [1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1, 0.5,   0,   1,   1, 0.5,   1], #Normal
    [1, 0.5, 0.5,   2,   1,   2,   1,   1,   1,   1,   1,   2, 0.5,   1, 0.5,   1,   2,   1], #Fire
    [1,   2, 0.5, 0.5,   1,   1,   1,   1,   2,   1,   1,   1,   2,   1, 0.5,   1,   1,   1], #Water
    [1, 0.5,   2, 0.5,   1,   1,   1, 0.5,   2, 0.5,   1, 0.5,   2,   1, 0.5,   1, 0.5,   1], #Grass
    [1,   1,   2, 0.5, 0.5,   1,   1,   1,   0,   2,   1,   1,   1,   1, 0.5,   1,   1,   1], #Electric
    [1, 0.5, 0.5,   2,   1, 0.5,   1,   1,   2,   2,   1,   1,   1,   1,   2,   1, 0.5,   1], #Ice
    [2,   1,   1,   1,   1,   2,   1, 0.5,   1, 0.5, 0.5, 0.5,   2,   0,   1,   2,   2, 0.5], #Fighting
    [1,   1,   1,   2,   1,   1,   1, 0.5, 0.5,   1,   1,   1, 0.5, 0.5,   1,   1,   0,   2], #Poison
    [1,   2,   1, 0.5,   2,   1,   1,   2,  1 ,   0,   1, 0.5,   2,   1,   1,   1,   2,   1], #Ground
    [1,   1,   1,   2, 0.5,   1,   2,   1,   1,   1,   1,   2, 0.5,   1,   1,   1, 0.5,   1], #Flying
    [1,   1,   1,   1,   1,   1,   2,   2,   1,   1, 0.5,   1,   1,   1,   1,   0, 0.5,   1], #Psychic
    [1, 0.5,   1,   2,   1,   1, 0.5, 0.5,   1, 0.5,   2,   1,   1, 0.5,   1,   2, 0.5, 0.5], #Bug
    [1,   2,   1,   1,   1,   2, 0.5,   1, 0.5,   2,   1,   2,   1,   1,   1,   1, 0.5,   1], #Rock
    [0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1,   1,   2,   1, 0.5,   1,   1], #Ghost
    [1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   2,   1, 0.5,   0], #Dragon
    [1,   1,   1,   1,   1,   1, 0.5,   1,   1,   1,   2,   1,   1,   2,   1, 0.5,   1, 0.5], #Dark
    [1, 0.5, 0.5,   1, 0.5,   2,   1,   1,   1,   1,   1,   1,   2,   1,   1,   1, 0.5,   2], #Steel
    [1, 0.5,   1,   1,   1,   1,   2, 0.5,   1,   1,   1,   1,   1,   1,   2,   2, 0.5,   1] #Fairy
]

#Attack |  Defender --

#Converts the type to a number that can be used in the type chart
type_convert = {
    "normal": 0,
    "fire": 1,
    "water": 2,
    "grass": 3,
    "electric": 4,
    "ice": 5,
    "fighting": 6,
    "poison": 7,
    "ground": 8,
    "flying": 9,
    "psychic": 10,
    "bug": 11,
    "rock": 12,
    "ghost": 13,
    "dragon": 14,
    "dark": 15,
    "steel": 16,
    "fairy": 17
}

#used to find the type match up multiplier
def get_type_mult(attack, defender): #attack will be a single string while defender will be a tuple
    atk = type_convert[attack]
    if (defender[1] == "None"): #If defender has 1 type
        return(types[atk][type_convert[defender[0]]])
    else: #If defender has 2 types
        multiplier = types[atk][type_convert[defender[0]]]
        multiplier *= types[atk][type_convert[defender[1]]]
        return(multiplier)
'''
attack = "fire"
defender = ("grass", "None")
print(get_type_mult(attack, defender))'''

#determines the weather multiplier
def get_weather_mult(attack, condition):
    if (attack == "water" and condition == "rain"):
        return(1.5)
    if (attack == "fire" and condition == "rain"):
        return(0.5)
    if (attack == "fire" and condition == "sunny"):
        return(1.5)
    if (attack == "water" and condition == "sunny"):
        return(0.5)
    return(1)

def get_total_damage(level, attacker_type, attack, defender, atk_stat, def_stat, speed_stat, move_power, condition="clear"):
    stab = 1
    crit = 1
    if (attack == attacker_type[0] or attacker_type[1]):
        stab = 1.5
    rand = random.randrange(85, 101, 2) / 100
    threshold = speed_stat / 2
    if threshold > 255:
        threshold = 255
    if (threshold / 256 > random.randrange(0, 256, 2)):
        crit = 2
    mult = get_weather_mult(attack, condition) * crit * rand * stab * get_type_mult(attack, defender)
    damage = ((2 * level / 5 + 2) * move_power * (atk_stat / def_stat) / 50 + 2) * mult
    return(round(damage))

#Level, attackers type, moves type, defender(Type1, Type2), attack stat, defenders defense, attacker speed, moves power, weather condition
#print(get_total_damage(1, "fire", ("fire", 'None'), ("grass", "None"), 52, 49, 65, 40, "clear"))