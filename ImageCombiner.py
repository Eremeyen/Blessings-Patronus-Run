from PIL import Image
import os
from os import listdir
from random import random
import csv

#attribute folders:

#folder paths will have to change
backgrounds = r"Backgrounds"
back_wings = r"Back_Wings"
tail = r"Tail"
bodies = r"Bodies"
eyes = r"Eye"
accessories = r"accessories"
front_wings = r"Front_Wings"
hair = r"Hair"
crown = r"crown"
horn = r"Horn"
orbs = r"orbs"

#dictionaries
background_names = {
    "PATRONUS BACKGROUND 1.png":"Purple",
    "PATRONUS BACKGROUND 2.png":"Purple blue",
    "PATRONUS BACKGROUND 3.png":"Navy",
    "PATRONUS BACKGROUND 4.png":"Blue in the dark",
    "PATRONUS BACKGROUND 5.png":"Neon blue in the dark"
}
backW_names = {
    "PATRONUS BACK WING 1.png":"Blue wings",
    "PATRONUS BACK WING 2.png":"Sky blue wings",
    "PATRONUS BACK WING 3.png":"Purple wings",
    "PATRONUS BACK WING 4.png":"Pink sparkle wings",
    "PATRONUS BACK WING 5.png":"Blue green glow wings",
    "PATRONUS BACK WING 6.png":"Purple blue glow wings"
}
tail_names = {
    "PATRONUS TAIL 1.png":"White purple glow tail",
    "PATRONUS TAIL 1.png":"Blue tail",
    "PATRONUS TAIL 1.png":"Pink blue glow tail"
}
body_names = {

}

eye_names = {

}

accessory_names = {

}

fWing_names = {

}

hair_names = {

}

crown_names = {

}

horn_names = {
    
}

orb_names = {
    "PATRONUS ORBS 1.png":"Blue sOrbs",
    "PATRONUS ORBS 2.png":"Purple Orbs",
    "PATRONUS ORBS 3.png":"Cyan Orbs",
    "PATRONUS ORBS 4.png":"Green Orbs"
}

#final images destination
finalImages = r"Blessings"

#defining an empty images array which we'll use to come up with each final image
images = []
for i in range(len(os.listdir("."))-3):
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







Metadata = []

while(bCounter < 116):
    blessing = {}

    if(bCounter < 10):
        id = "000" + str(bCounter)
    elif(bCounter < 100):
        id = "00" + str(bCounter)
    elif(bCounter < 1000):
        id = "0" + str(bCounter)
    else:
        id = str(bCounter)
    blessing["id"] = int(id)

    backG = whichBackground()
    images[0] = Image.open(backgrounds + "/" + backG).convert("RGBA")
    blessing["Background"] = background_names[backG]

    backW = whichBackWing()
    images[1] = Image.open(back_wings + "/" + backW).convert("RGBA")
    blessing["Back Wing"] = backW_names[backW]
    
    wTail = whichTail()
    images[2] = Image.open(tail + "/" + wTail).convert("RGBA")
    blessing["Tail"] = tail_names[wTail]

    wBody = whichBody()
    images[3] = Image.open(bodies + "/" + wBody).convert("RGBA")
    blessing["Body"] = body_names[wBody]

    wEye = whichEye()
    images[4] = Image.open(eyes + "/" + wEye).convert("RGBA")
    blessing["Eyes"] = eye_names[wEye]

    wAccessory = whichAccessory()
    images[5] = Image.open(accessories + "/" + wAccessory).convert("RGBA")
    blessing["Accessory"] = accessory_names[wAccessory]


    #determining which front wing to use
    fWing = "PATRONUS FRONT WING " + backW[-5] + ".png"
    images[6] = Image.open(front_wings + "/" + fWing).convert("RGBA") #front wing
    blessing["Front Wing"] = fWing_names[fWing]

    #determining which hair to use
    wHair = "PATRONUS HAIR " + wTail[-5] + ".png"
    images[7] = Image.open(hair + "/" + wHair).convert("RGBA") #hair
    blessing["Hair"] = hair_names[wHair]

    wCrown = whichCrown()
    images[8] = Image.open(crown + "/" + wCrown).convert("RGBA")
    blessing["Crown"] = crown_names[wCrown]

    wHorn = whichHorn()
    images[9] = Image.open(horn + "/" + wHorn).convert("RGBA")
    blessing["Horn"] = horn_names[wHorn]

    wOrb = whichOrbs()
    images[10] = Image.open(orbs + "/" + wOrb).convert("RGBA")
    blessing["Orbs"] = orb_names[wOrb]


    final_image = images[0]

    #combining all layers
    for i in range(1,len(images)):
        final_image = Image.alpha_composite(final_image,images[i])
    
    #saving the image with the correct name and directory
    #print(str(bCounter) + " images generated")
    final_image.save(finalImages+"/Blessings Patronus " +str(bCounter)+".png")
    
    
    Metadata.append(blessing)


    bCounter += 1

    
#writing csv file
main_info = ["id","Background","Back Wing","Tail","Body","Eyes","Accessory","Front Wing","Hair","Crown","Horn","Orbs"]

with open("metadata.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames= main_info)
    writer.writeHeader()
    writer.writerows(Metadata)





