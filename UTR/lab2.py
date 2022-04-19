from sys import stdin
import sys


global skupStanja
global skupSimbola
global skupPrihStanja
global pocStanje
global dict1
dict1 = {}


def splitLine(stanja):
    skupStanja = stanja.split(",")
    return skupStanja

def unesiPrijelaz(string):
    string = string.split("->")
    stringL = string[0].split(",")
    stringR = string[1].split(",")
    dict1[stringL[0]][stringL[1]] = stringR


def izbaciNedohvatljiva():
    dohvatljivaStanja = set()
    dohvatljivaStanja.add(pocStanje)
    
    while True:
        dodanoJeStanje = False
        novaStanja = set()
        for stanje in dohvatljivaStanja:
            for abc in skupSimbola:
                stanje1 = dict1[stanje][abc]
                if((stanje1[0] in dohvatljivaStanja) == False):
                    dodanoJeStanje = True
                    novaStanja.add(stanje1[0])
        dohvatljivaStanja = dohvatljivaStanja | novaStanja

        if dodanoJeStanje == False:
            break
    nedohvatljivaStanja = set()
    for stanje in skupStanja:
        if((stanje in dohvatljivaStanja) == False):
            nedohvatljivaStanja.add(stanje)
    for stanje in nedohvatljivaStanja:
        skupStanja.remove(stanje)
        if stanje in skupPrihStanja:
            skupPrihStanja.remove(stanje)
        dict1.pop(stanje)


#   MAIN

data = sys.stdin.readlines()

n = 0
for i in data:
    data[n] = i.rstrip('\n')
    n = n + 1

skupStanja = splitLine(data[0])
skupSimbola = splitLine(data[1])
skupPrihStanja = splitLine(data[2])
pocStanje = data[3]
prijelazi = data[4:]


#stvori dictionary u dictionaryu
for y in skupStanja:
    dict2 = {}
    for x in skupSimbola:
        dict2[x] = "#"
    dict1[y] = dict2

#napuni dictionary prijelazima
for x in prijelazi:
    unesiPrijelaz(x)


izbaciNedohvatljiva()

#   MINIMIZACIJA
automat = {}

for i in skupStanja:
    for j in skupStanja:
        if (i != j) and ((i,j) not in automat.keys()) and ((j,i) not in automat.keys()):
            automat[(i, j)] = ((i in skupPrihStanja) != (j in skupPrihStanja))


prekid = True
while prekid:
    prekid = False
    for n,i in enumerate(skupStanja):
        for j in skupStanja[n+1:]:
            if automat[(i, j)] == True:
                continue
            for znak in skupSimbola:              
                prvi = dict1[i].get(znak)[0]
                drugi = dict1[j].get(znak)[0]
                if prvi == drugi: break
                else:
                    if prvi < drugi:
                        sortiraniPar = (prvi, drugi)
                    else: 
                        sortiraniPar = (drugi, prvi)
                    tempBool = automat[sortiraniPar]
                    prekid = prekid or tempBool
                    automat[(i, j)] = tempBool
                    if tempBool:
                        break

for key, val in automat.items():
    if not val:
        if pocStanje == key[1]:
            pocStanje = key[0]
        if key[1] in skupPrihStanja:
            skupPrihStanja.remove(key[1])
        for i in dict1:
            for j in dict1[i]:
                if dict1[i][j][0] == key[1]:
                    dict1[i][j][0] = key[0]
        if key[1] in skupStanja:
            skupStanja.remove(key[1])
            dict1.pop(key[1])


print(",".join(skupStanja))
print(",".join(skupSimbola))
print(",".join(skupPrihStanja))
print(pocStanje)
for k in dict1.keys():
    for v in dict1[k].keys():
        minPrijelaz = k + "," + v + "->" + dict1[k][v][0]
        print(minPrijelaz)

