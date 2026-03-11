#libraries needed
from minescript import *
import math
import time
import keyboard

max_hit_range = 4 #maximum hitrange in mc is 3 blocks

def attack():
    entity = player_get_targeted_entity() #checks if we're looking at entity
    if not entity:
        return
    Px, Py, Pz = player_position() #gets player position
    Ex, Ey, Ez = entity.position #gets entity position
    distance = math.sqrt((Ex - Px)**2 + (Ey - Py)**2 + (Ez - Pz)**2) #math to check how much distane is between us
    if distance <= max_hit_range:   #
        player_press_attack(True)   #
        time.sleep(0.02)            # if entity is in hit range (4 blocks) press left click
        player_press_attack(False)  #
        time.sleep(0.01)            #

if __name__ == "__main__":
    print("running")
    while True:
        attack()
        time.sleep(0.1)

        if keyboard.is_pressed(']'):  #stopping the script
            break