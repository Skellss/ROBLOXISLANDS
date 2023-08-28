# Make sure to enter the command pip install keyboard in your terminal before running. 
# Make sure that you have your gold slot in your hand before you run the code.
# Put your gold in your first slot of your inv, and your copper in the second.
# Once those are checked off, just run the code and tab to back to the game.


import keyboard
import time

def simulate_key_press(key, times=1, delay=0.1):
    for _ in range(times):
        keyboard.press(key)
        keyboard.release(key)
        time.sleep(delay)

while True:
    
    simulate_key_press('q', times=2)

   
    simulate_key_press('2')

    
    simulate_key_press('q', times=30)

    
    simulate_key_press('1')

    
    time.sleep(1)