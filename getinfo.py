from minescript import *
import keyboard
import time

def main():
    print("Press [ to get block and enity type.\nPress ] to exit.")
    try:
        while True:
            if keyboard.is_pressed('['):

                block = player_get_targeted_block() #gets the block you're looking at
                entity = player_get_targeted_entity() #gets the entity you're looking at

                print('BLOCK:\n',block, '\nENTITY:\n', entity,'\n--------------------------') #prints that info
                time.sleep(0.5) #delay so no multiple detections per button press
            
            if keyboard.is_pressed(']'): #button to stop script
                break

    except KeyboardInterrupt:
        print("\n Program interupted")

if __name__ == "__main__":
    main()