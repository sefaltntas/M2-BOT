from python_imagesearch.imagesearch import imagesearch

import time
import keyword
import pyautogui

while True:
    time.sleep(0.05)

    metin_adi = imagesearch("metin_adi.png")
    if metin_adi[0] != -1:
        print("position : ", metin_adi[0], metin_adi[1])
        pyautogui.moveTo(metin_adi[0]+70,metin_adi[1]+70)
        time.sleep(0.5)
        pyautogui.click(metin_adi[0]+70,metin_adi[1]+70)
        time.sleep(1)
    else:
        print("metin yok")
