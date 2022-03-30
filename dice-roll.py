# nécessite Python 3 et le module pyttsx3 : python -m pip install pyttsx3
# -*- coding: utf-8 -*-
import os
import random
import time
import pyttsx3
import re
import sys

# argument to
if "--mute" in sys.argv or "-m" in sys.argv or "mute" in sys.argv:
    mute = True
else:
    mute = False

if "--timecode" in sys.argv or "-t" in sys.argv or "timecode" in sys.argv:
    timecode = True
else:
    timecode = False

# Moteur de synthèse vocale
history = []
rerollPlease = ""


def say(phrase, rate=280, log=True):
    print(phrase)
    global history
    if log:
        history.append(phrase)
    global mute
    if(not mute):
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.say(phrase)
        engine.runAndWait()


def repeatPlease():
    global history
    if len(history) > 0:
        say(history.pop(), 130)


def timelog():
    say(time.strftime("%H:%M:%S", time.gmtime()), 280)


def roll(diceText):
    global rerollPlease
    rerollPlease = diceText
    launches = diceText.split(";")
    toSay = ""
    for launch in launches:
        # replace shortcuts with values
        if(launch[:1].upper() == "A"):
            launch = "1d20" + launch[1:]
        if(launch[:1].upper() == "Z"):
            launch = "1d12" + launch[1:]
        if(launch[:1].upper() == "E"):
            launch = "1d10" + launch[1:]
        if(launch[:1].upper() == "R"):
            launch = "1d8" + launch[1:]
        if(launch[:1].upper() == "T"):
            launch = "1d6" + launch[1:]
        if(launch[:1].upper() == "Y"):
            launch = "1d4" + launch[1:]
        # determine modifier sign
        modifierSign = 1
        if launch.__contains__('-'):
            modifierSign = -1
        # get the 2 or 3 values in dice special form
        diceInfo = re.split("[^\d]+", launch)
        if len(diceInfo) < 2 or diceInfo[0] == "" or diceInfo[1] == "":
            say("Erreur, valeur saisie invalide.", 280, False)
            return False
        else:
            diceInfo[0] = int(diceInfo[0])  # number of dice
            diceInfo[1] = int(diceInfo[1])  # dice type
            if len(diceInfo) > 2:  # result modifier
                if diceInfo[2] != '':
                    diceInfo[2] = int(diceInfo[2])
                else:
                    diceInfo[2] = 0
            else:
                diceInfo.append(0)
            if diceInfo[0] > 0 and diceInfo[1] > 0:
                results = ""
                for i in range(diceInfo[0]):
                    results = results + " " + \
                        str(random.randrange(
                            1, diceInfo[1]+1)+(modifierSign*diceInfo[2]))
                toSay = toSay + str(diceInfo[0]) + "d" + str(diceInfo[1]) + ("" if diceInfo[2] == 0 else (
                    "+" if modifierSign > 0 else"-") + str(diceInfo[2])) + " :" + results + "\n"
            else:
                say("Erreur, valeur saisie invalide.", 280, False)
                return False
    global timecode
    if(timecode):
        timelog()
    say(toSay)


def help():
    say("Pour lancer vos dés, saisissez des formes abrégées séparées par des point-virgules.\n" +
        "exemple : 1d6, 2d20+3, 4d6... \n" +
        "Touches Raccourcies AZERTY : A (Alpha) - 1d20; Z (Zoulou) - 1d12 ; E (Echo) - 1d10 ; R (Romeo) - 1d8 ; T (Tango) - 1d6 ; Y (Yankee) - 1d4 \n" +
        "Autres commandes : P (Papa) ou Entrée - Répéter la dernière phrase; O (Oscar) - Refaire le dernier lancé; I (India) - Ouvrir le fichier des 5 derniers lancés; U (Uniform) - Ouvrir le fichier historique complet; Q (Quebec) - Quitter le programme;", 200, False)


def historyOpen(number=0):

    # if timecode is on we need to double the number of lines
    global timecode
    if(timecode):
        number = 2*number

    # open 5 last launch or everything
    global history
    if number > 0:
        extract = history[(-1*number):]
    else:
        extract = history

    # write file
    f = open("history.log", "w+")
    for line in extract:
        f.write(line + "\n")
    f.close()

    # Open file with default text program
    os.startfile("history.log")


say("Bonjour, Appuyer sur H (Hotel) pour lire l'aide.", 280, False)

inputText = ""
while True:
    inputText = input()
    # Ouvrir l'aide
    if inputText[:1].upper() == "H":
        help()
    elif len(inputText) == 0 or inputText[:1].upper() == "P":
        repeatPlease()
    elif inputText[:1].upper() == "O":
        roll(rerollPlease)
    elif inputText[:1].upper() == "I":
        historyOpen(5)
    elif inputText[:1].upper() == "U":
        historyOpen()
    elif inputText[:1].upper() == "Q":
        break
    else:
        roll(inputText)

say("Au revoir, merci d'avoir joué.", 280, False)
