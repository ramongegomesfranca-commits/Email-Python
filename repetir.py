import pyautogui
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for i in range(1, 11):
    #pyautogui.alert(f"Numero gerado: {i}")
    print(f"Número gerado: {i}")
    time.sleep(0.5)