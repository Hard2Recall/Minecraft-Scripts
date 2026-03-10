from minescript import *
import keyboard
import time

def main():
    print("Press [ to get block and enity type.\nPress ] to exit.")
    try:
        while True:
            if keyboard.is_pressed('['):

                block = player_get_targeted_block() 
                entity = player_get_targeted_entity() 

                print('BLOCK:\n',block, '\nENTITY:\n', entity,'\n--------------------------') #printing block and entity info that youre looking at
                time.sleep(0.5) #delay so there is no multiple detections per button press
            
            if keyboard.is_pressed(']'): #button to stop script
                break

    except KeyboardInterrupt:
        print("\n Program interupted")

if __name__ == "__main__":
    main()