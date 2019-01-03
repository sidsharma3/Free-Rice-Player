import pyautogui, random, webbrowser, os

webbrowser.open('http://freerice.com/#/english-vocabulary/1727')

numoftimes = input("type the number of times you want to play \n")

pyautogui.doubleClick(381, 366)

for i in range(int(numoftimes) - 1):
    if random.randint(1,4) == 1:
        pyautogui.moveTo(220, 406, duration=1.5)
        pyautogui.doubleClick(220, 406)
    elif random.randint(1,4) == 2:
        pyautogui.moveTo(220, 446, duration=1.5)
        pyautogui.doubleClick(220, 446)
    elif random.randint(1,4) == 3:
        pyautogui.moveTo(220, 486, duration=1.5)
        pyautogui.doubleClick(220, 486)
    elif random.randint(1,4) == 4:
        pyautogui.moveTo(220, 526, duration=1.5)
        pyautogui.doubleClick(220, 526)

print("program is completed, ran " + numoftimes + " times.")


        
