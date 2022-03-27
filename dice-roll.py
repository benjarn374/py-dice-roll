# nécessite Python 3 et le module pyttsx3 : python -m pip install pyttsx3
# -*- coding: utf-8 -*-
import random
from tkinter import W
import pyttsx3
import re

# Moteur de synthèse vocale
repeatPlease = ""
rerollPlease = ""


def say(phrase,rate = 280):
    print(phrase)
    global repeatPlease
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    repeatPlease = phrase
    engine.say(phrase)
    engine.runAndWait()

def roll(diceText):
    diceInfo = re.split("[^\d]+", diceText)
    if diceInfo[0] == "" or diceInfo[1] =="" :
        say("Erreur, valeur saisie invalide.")
        return False
    else :
        diceInfo[0] = int(diceInfo[0])
        diceInfo[1] = int(diceInfo[1])
        if diceInfo[0] > 0 and diceInfo[1] > 0 :
            global rerollPlease
            rerollPlease = diceText
            results = ""
            for i in range(diceInfo[0]): results = results + " " + str(random.randrange(1,diceInfo[1]+1)) 
            say(str(diceInfo[0]) + "d" + str(diceInfo[1]) + " :" + results)
        else :
            say("Erreur, valeur saisie invalide.")
            return False;

def help():
    say("Pour lancer un dé, saisissez sa forme abrégée. exemple : 1d6, 2d20, 4d6... \nTouches Raccourcies AZERTY : A (Alpha) - 1d20; Z (Zoulou) - 1d12 ; E (Echo) - 1d10 ; R (Romeo) - 1d8 ; T (Tango) - 1d6 ; Y (Yankee) - 1d4 \nAutres commandes : P (Papa) ou Entrée - Répéter la dernière phrase; O (Oscar) - Refaire le dernier lancé; Q (Quebec) - Quitter le programme;",200)

say("Bonjour, Appuyer sur H (Hotel) pour lire l'aide.");

inputText = ""
while True :
    inputText = input()
    # Ouvrir l'aide
    if  inputText[:1].upper() == "H" :
        help()
    elif len(inputText) == 0 or inputText[:1].upper() == "P" : say(repeatPlease,130);
    elif inputText[:1].upper() == "A" : roll("1d20")
    elif inputText[:1].upper() == "Z" : roll("1d12")
    elif inputText[:1].upper() == "E" : roll("1d10")
    elif inputText[:1].upper() == "R" : roll("1d8")
    elif inputText[:1].upper() == "T" : roll("1d6")
    elif inputText[:1].upper() == "Y" : roll("1d4")
    elif inputText[:1].upper() == "O" : roll(rerollPlease)
    elif inputText[:1].upper() == "Q" : break
    else : roll(inputText)
    
say("Au revoir, merci d'avoir joué.")