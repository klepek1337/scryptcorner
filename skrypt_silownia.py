import pyautogui
import time
import os
print("silownia = 1")
wybor = int(input())
if wybor == 1:
    print("Skrypt zaczął pracę")
    print("Wyłącz go gdy skończysz, masz pięc sekund na wejście do gry.")
    time.sleep(5)
    for loop in range(100):
        pyautogui.keyDown('space')
        time.sleep(3)
        pyautogui.keyUp('space')

os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\notepad.lnk")
    
