# pip install keyboard first
# drops gold first
# Put your gold in slot 1 of inv and bronze in slot 2


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
