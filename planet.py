import math
import random

current_planet = 0 

name = []
desc = []
xPos = []
yPos = []

def add_planet(n, d, x, y):
    global name, desc, xPos, yPos

    name += [n]
    desc += [d]
    xPos += [x]
    yPos += [y]

def random_pos():
    return random.uniform(-10, 10);

def init():
    add_planet("Earth", "A pale blue dot", 0.0, 0.0)
    add_planet("Alpha Proxima", "Earth's nearest neighbor", 0.000, -4.755)
    add_planet("Kessel", "A planet known for its spice mines", 3.7, 2.0)
    add_planet("Tatooine", "A hostile desert planet known for its two suns", random_pos(), random_pos()) 
    add_planet("Coruscant", "A planet whose surface is strictly one giant city", random_pos(), random_pos())

def total_planets():
    return len(name)

def description():
    description_str = "Planet: " + name[current_planet]
    description_str += "\n\n"
    description_str += desc[current_planet]
    description_str += "\n\n"

    return description_str

def travel_targets():
    travel_str = ""
    
    skip = 0

    for i in range(total_planets()):
        if i == current_planet:
            skip += 1
        else:
            travel_str += " " + str((i + 1) - skip) + ". " + name[i]
            travel_str += " (" + "{0:.2f}".format(distance_to(i)) + " ly)\n"

    return travel_str

def distance_to(to):
    deltaX = xPos[current_planet] - xPos[to]
    deltaY = yPos[current_planet] - yPos[to]

    sum_of_squares = deltaX ** 2 + deltaY ** 2

    return math.sqrt(sum_of_squares)
