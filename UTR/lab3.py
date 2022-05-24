import sys
from sys import stdin

global ulazniNizovi
global skupStanja
global skupUlaznihZnakova
global skupZnakovaStoga
global skupPrihvatljivihStanja
global pocStanje
global pocZnakStoga
global dict1
dict1 = {}
global stack
stack = []
global trenutnoStanje
global ispisRez
global naStogu


def getUlazniNizovi(linija1):
    pojedinacno = []
    ulazniNizovi = linija1.split("|")
    for i in ulazniNizovi:
        ulaz = i.split(",")
        pojedinacno.append(ulaz)
    return pojedinacno

def splitLine(stanja):
    skupStanja = stanja.split(",")
    return skupStanja

def unesiPrijelaz(string):
    string = string.split("->")
    stringL = string[0]
    stringR = string[1]
    stringL = stringL.split(",")
    stringR = stringR.split(",")
    dict1[stringL[0]][stringL[1]][stringL[2]] = stringR

def prijelazFunc(znak):         #OVO PREPRAVITI
    #print("funkcija")
    global trenutnoStanje
    global ispisRez
    global naStogu
    index = 0
    novoStanje = dict1[trenutnoStanje][znak][naStogu][0]
    for val in dict1[trenutnoStanje][znak][naStogu][1]:
        if val == "$" and len(stack) > 0:
            continue
        else:
            stack.insert(index,val)
        index += 1
    trenutnoStanje = novoStanje
    ispisRez += "|" + trenutnoStanje + "#" + "".join(stack)


        # MAIN
    #--------------

data = sys.stdin.readlines()
funkcije_prijelaza = {}
n = 0
for i in data:
    data[n] = i.rstrip('\n')
    n = n + 1

ulazniNizovi = getUlazniNizovi(data[0]) # [['0'], ['0', '2', '0'], ['1', '2', '0']]
skupStanja = splitLine(data[1]) # ['q1', 'q2', 'q3']
skupUlaznihZnakova = splitLine(data[2]) # ['0', '1', '2']
skupZnakovaStoga = splitLine(data[3]) # ['J', 'N', 'K']
skupPrihvatljivihStanja = splitLine(data[4]) # ['q3']
pocStanje = data[5] # q1
pocZnakStoga = data[6] # K

prijelazi = data[7:]

#stvaranje dictionaryja i punjenje s '/'
for stanje in skupStanja:
    dict1[stanje] = {}
    dict1[stanje]["$"] = {}
    for znak in skupUlaznihZnakova:
        dict1[stanje][znak] = {}
        for znakSt in skupZnakovaStoga:
            dict1[stanje][znak][znakSt] = '/'
            dict1[stanje]["$"][znakSt] = '/'
        dict1[stanje][znak]["$"] = '/'
    dict1[stanje]["$"]["$"] = '/'

#unos prijelaza u dictionary
for prijelaz in prijelazi:
    unesiPrijelaz(prijelaz)

#print(dict1)

#obradi niz znakova
for niz in ulazniNizovi:
    trenutnoStanje = pocStanje
    stack = [pocZnakStoga]
    ispisRez = pocStanje + "#" + pocZnakStoga
    #obradi znakove pojedinacno
    for i in niz:
        naStogu = stack.pop(0)
        kraj = False
        while (dict1[trenutnoStanje][i][naStogu] == '/'):
            if(dict1[trenutnoStanje]["$"][naStogu] == '/'):
                    ispisRez = ispisRez + "|fail"
                    kraj = True
                    break
            prijelazFunc("$")
            naStogu = stack.pop(0)
        if(kraj == True): break
        prijelazFunc(i)
        kraj = False
    if (kraj == True):
        ispisRez = ispisRez + "|0"
    else:
        if trenutnoStanje in skupPrihvatljivihStanja:
                ispisRez = ispisRez + "|1"
        else:
            while (1==1):
                naStogu = stack.pop(0)
                if(dict1[trenutnoStanje]["$"][naStogu] == '/'):
                    ispisRez = ispisRez + "|0"
                    break
                prijelazFunc("$")
                if (trenutnoStanje in skupPrihvatljivihStanja):
                    ispisRez = ispisRez + "|1"
                    break
    
    print(ispisRez)
