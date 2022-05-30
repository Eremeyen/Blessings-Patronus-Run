from PIL import Image
import os
from os import listdir
from random import random

#attribute folders:
backgrounds = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\Backgrounds"
back_wings = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\Back_Wings"
tail = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\Tail"
bodies = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\Bodies"
eyes = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\Eye"
accessories = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\accessories"
front_wings = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\Front_Wings"
hair = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\Hair"
crown = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\crown"
horn = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\Horn"
orbs = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\orbs"

#final images destination
finalImages = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run\Blessings"

#defining an empty images array which we'll use to come up with each final image
images = []
for i in range(len(os.listdir(r"C:\Users\meren\OneDrive\Masaüstü\Blessings Patronus Run"))-2):
    images.append("")




bCounter = 1

def whichBackground():
    n = random()
    if (n < 0.2):
        return "PATRONUS BACKGROUND 1.png"
    elif (n < 0.4):
        return "PATRONUS BACKGROUND 2.png"
    elif (n < 0.6):
        return "PATRONUS BACKGROUND 3.png"
    elif (n < 0.8):
        return "PATRONUS BACKGROUND 4.png"
    else:
        return "PATRONUS BACKGROUND 5.png"

def whichBackWing():
    n = random()
    if(n < 0.24):
        return "PATRONUS BACK WING 1.png"
    elif(n < 0.47):
        return "PATRONUS BACK WING 2.png"
    elif(n < 0.70):
        return "PATRONUS BACK WING 6.png"
    elif(n < 0.8):
        return "PATRONUS BACK WING 3.png"
    elif(n < 0.9):
        return "PATRONUS BACK WING 4.png"
    else:
        return "PATRONUS BACK WING 5.png"
def whichTail():
    n = random()
    if (n < 0.34):
        return "PATRONUS TAIL 1.png"
    elif (n < 0.68):
        return "PATRONUS TAIL 2.png"
    else:
        return "PATRONUS TAIL 3.png"

def whichBody():
    n = random()
    if(n < 0.25):
        return "PATRONUS BODY 1.png"
    elif(n < 0.5):
        return "PATRONUS BODY 2.png"
    elif(n < 0.75):
        return "PATRONUS BODY 3.png"
    else:
        return "PATRONUS BODY 4.png"

def whichEye():
    n = random()
    if(n < 0.09):
        return "PATRONUS EYE F1.png"
    elif(n < 0.18):
        return "PATRONUS EYE F2.png"
    elif(n < 0.27):
        return "PATRONUS EYE F3.png"
    elif(n < 0.36):
        return "PATRONUS EYE F4.png"
    elif(n < 0.52):
        return "PATRONUS EYE M1.png"
    elif(n < 0.68):
        return "PATRONUS EYE M2.png"
    elif(n < 0.84):
        return "PATRONUS EYE M3.png"
    else:
        return "PATRONUS EYE M4.png"

def whichAccessory():
    n = random()
    if (n < 0.15):
        return "PATRONUS ACC 1.png"
    elif (n < 0.3):
        return "PATRONUS ACC 2.png"
    elif (n < 0.45):
        return "PATRONUS ACC 3.png"
    elif(n < 0.6):
        return "PATRONUS ACC 4.png"
    else:
        return "220329-0959-BOS LAYER.png"

def whichCrown():
    n = random()
    if (n < 0.17):
        return "PATRONUS CROWN 1.png"
    elif (n < 0.34):
        return "PATRONUS CROWN 2.png"
    elif (n < 0.51):
        return "PATRONUS CROWN 3.png"
    elif (n < 0.68):
        return "PATRONUS CROWN 4.png"
    elif (n < 0.83):
        return "PATRONUS CROWN 5.png"
    else:
        return "PATRONUS CROWN 6.png"

def whichHorn():
    n = random()
    if(n < 0.14):
        return "PATRONUS HORN 1.png"
    elif (n < 0.28):
        return "PATRONUS HORN 2.png"
    elif (n < 0.42):
        return "PATRONUS HORN 3.png"
    elif (n < 0.56):
        return "PATRONUS HORN 4.png"
    elif (n < 0.7):
        return "PATRONUS HORN 5.png"
    elif (n < 0.85):
        return "PATRONUS HORN 6.png"
    else:
        return "PATRONUS HORN 7.png"

def whichOrbs():
    n = random()
    if(n < 0.25):
        return "PATRONUS ORBS 1.png"
    elif(n<0.5):
        return "PATRONUS ORBS 2.png"
    elif(n<0.75):
        return "PATRONUS ORBS 3.png"
    else:
        return "PATRONUS ORBS 4.png"









while(bCounter < 116):
    images[0] = Image.open(backgrounds + "/" + whichBackground()).convert("RGBA")
    backW = whichBackWing()
    images[1] = Image.open(back_wings + "/" + backW).convert("RGBA")
    wTail = whichTail()
    images[2] = Image.open(tail + "/" + wTail).convert("RGBA")
    images[3] = Image.open(bodies + "/" + whichBody()).convert("RGBA")
    images[4] = Image.open(eyes + "/" + whichEye()).convert("RGBA")
    images[5] = Image.open(accessories + "/" + whichAccessory()).convert("RGBA")
    #determining which front wing to use
    fWing = "PATRONUS FRONT WING " + backW[-5] + ".png"
    images[6] = Image.open(front_wings + "/" + fWing).convert("RGBA") #front wing
    #determining which hair to use
    wHair = "PATRONUS HAIR " + wTail[-5] + ".png"
    images[7] = Image.open(hair + "/" + wHair).convert("RGBA") #hair
    images[8] = Image.open(crown + "/" + whichCrown()).convert("RGBA")
    images[9] = Image.open(horn + "/" + whichHorn()).convert("RGBA")
    images[10] = Image.open(orbs + "/" + whichOrbs()).convert("RGBA")
    final_image = images[0]

    #combining all layers
    for i in range(1,len(images)):
        final_image = Image.alpha_composite(final_image,images[i])
    #saving the image with the correct name and directory
    print(str(bCounter) + " images generated")
    final_image.save(finalImages+"/Blessings Patronus " +str(bCounter)+".png")
    bCounter += 1

    






