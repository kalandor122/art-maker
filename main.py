import random
import numpy as np
import cv2
from art import *
import time

tprint("-------------")
tprint("Magor Software")
tprint("                Art Maker")
tprint("-------------")
time.sleep(2)

for o in range(int(input("how many you want to make:"))):
    blank_image = np.zeros((500,500,3), np.uint8)

    direction = ["right", "left", "up" "down", "upright","upleft","downright","downleft"]
    colors = ["0,0,0","192,192,192","128,128,128","128,0,0","255,0,0","128,0,128","255,0,255","0,128,0","0,255,0","255,255,0","0,0,128","0,0,255", "0,128,128", "0,255,255" ]
    startpointx = random.randrange(0, 500)
    startpointy = random.randrange(0, 500)
    startlenght = random.randrange(50,250)
    startwidht = random.randrange(10,60)
    startcolor = random.randrange(0,len(colors)-1)
    startdirection = random.randrange(0, len(direction))

    j = 0
    img = cv2.bitwise_not(blank_image) 
    y = str(colors[startcolor].replace(' " ', ''))
    g = y.split(",")

    for b in range(8):
        startpointx = random.randrange(0, 500)
        startpointy = random.randrange(0, 500)
        startlenght = random.randrange(50,250)
        startwidht = random.randrange(10,60)
        startcolor = random.randrange(0,15)
        try:
            y = str(colors[startcolor].replace(' " ', ''))
            g = y.split(",")

        except Exception as e:
                j = 0
        for i in range(startlenght):
            for x in range(startwidht):
                try:
                    if startpointx+i+x and startpointy+i < 500:
                        img[startpointx+i+x][startpointy+i] = g
                
                except Exception as e:
                    j = 0

    print("done")

    cv2.imwrite(f"{o+1}.png", img)
    cv2.waitKey(0)