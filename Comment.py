import pyautogui
import time

comments = ["Hi","I am Barbarian","Just for fun","I am just checking my Python skill","Python is awesome"]

time.sleep(5)

for i in range(5):
    pyautogui.typewrite(comments[i%5])
    pyautogui.typewrite("\n")
    time.sleep(2)
    
    
