from ctypes import resize
from sys import stdin
import sys

from numpy import array

global ulaz
global skupStanja
global pocStanje
global dict1
dict1 = {}
global trenutnaStanja
trenutnaStanja = []
global trenutnoStanje
trenutnoStanje = ""
global privremenaStanja
privremenaStanja = []
global strPrSt
strPrSt = ""
global rez
rez = ""

def getUlazniNizovi(linija1):
    pojedinacno = []
    ulazniNizovi = linija1.split("|")
    for i in ulazniNizovi:
        ulaz = i.split(",")
        #print(ulaz)
        pojedinacno.append(ulaz)
    #print(pojedinacno)
    return pojedinacno


def splitLine(stanja):
    skupStanja = stanja.split(",")
    return skupStanja

def unesiPrijelaz(string):
    string = string.split("->")
    stringL = string[0].split(",")
    stringR = string[1].split(",")
    dict1[stringL[0]][stringL[1]] = stringR


def epsilonOkruzenje(trenutnoStanje):
    if (trenutnoStanje == "#"):
        return

    if (str(dict1[str(trenutnoStanje)]["$"]) == "#"):
        return

    if (str(dict1[str(trenutnoStanje)]["$"]) != "#"):
        privremenaStanja.append((dict1[str(trenutnoStanje)]["$"])[0])
        stanje = (dict1[str(trenutnoStanje)]["$"])[0]
        if type(stanje) == list:
            stanje = stanje[0]
        epsilonOkruzenje(str(stanje))
    return

def prijelaz2(znak):
    pomocniArray = []
    global trenutnaStanja
    for x in trenutnaStanja:
        for y in dict1[x][znak]:
            if (y == "#"):
                continue
            pomocniArray.append(y)
    if pomocniArray:
        trenutnaStanja = sorted(set(pomocniArray))
    else:
        trenutnaStanja.clear()
        trenutnaStanja.append("#")

def prijelaz1(znak):
        global trenutnaStanja
        if (trenutnaStanja[0] == "#"):
            return
        prijelaz2(znak)
        if (trenutnaStanja[0] == "#"):
            return

    


#MAIN

data = sys.stdin.readlines()
funkcije_prijelaza = {}
n = 0
for i in data:
    data[n] = i.rstrip('\n')
    n = n + 1

# ULAZ = ARRAY ARRAYA ulaznih znakova
ulaz = getUlazniNizovi(data[0])

skupStanja = splitLine(data[1])

abeceda = splitLine(data[2])
abeceda.append("$")

pocStanje = data[4]

prijelazi = data[5:]

#stvori dictionary u dictionaryu
for y in skupStanja:
    dict2 = {}
    for x in abeceda:
        dict2[x] = "#"
    dict1[y] = dict2

#napuni dictionary prijelazima
for x in prijelazi:
    unesiPrijelaz(x)

trenutnaStanja.append(pocStanje)

for i in ulaz:
    
    for j in i:
        strPrSt = ""
        trenutnaStanja = sorted(set(trenutnaStanja))
        for x in trenutnaStanja:
            strPrSt = strPrSt + "," + x
        strPrSt = strPrSt[1:]
        rez = rez + "|" + strPrSt
        #print("|" + strPrSt)
        strPrSt = ""
        privremenaStanja.clear()
        
        prijelaz1(j)

        for x in trenutnaStanja:
            epsilonOkruzenje(x)
        for y in privremenaStanja:
            trenutnaStanja.append(y)

        trenutnaStanja = sorted(set(trenutnaStanja))
        
    strPrSt = ""
    trenutnaStanja = sorted(set(trenutnaStanja))
    for x in trenutnaStanja:
        strPrSt = strPrSt + "," + x
    strPrSt = strPrSt[1:]
    rez = rez + "|" + strPrSt
    strPrSt = ""
    privremenaStanja.clear()

    rez = rez[1:]
    print(rez)
    rez = ""
    trenutnaStanja.clear()
    trenutnaStanja.append(pocStanje)


