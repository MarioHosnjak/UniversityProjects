import sys
from sys import stdin

global niz
global ispis
ispis = ""
global flag
flag = False
global znak
znak = ""
global brojac
brojac = 0


def S():
    global niz, ispis, flag, brojac, znak

    ispis = "".join((ispis,"S"))
    
    if(znak == 'a'):
        if(brojac < len(niz)):
            znak = niz[brojac]
            brojac = brojac + 1
        else:
            flag = True
        A()
        B()
    elif(znak == 'b'):
        if(brojac < len(niz)):
            znak = niz[brojac]
            brojac = brojac + 1
        else:
            flag = True
        B()
        A()
    else:
        exitFunc()

def A():
    global niz, ispis, flag, brojac, znak
    
    ispis = "".join((ispis,"A"))

    if(znak == 'b'):
        if(brojac < len(niz)):
            znak = niz[brojac]
            brojac = brojac + 1
        else:
            znak = 'K'
            flag = True
        C()
    elif(znak == 'a'):
        if(brojac < len(niz)):
            znak = niz[brojac]
            brojac = brojac + 1
        else:
            flag = True
    else:
        exitFunc()

def C():
    global ispis
    ispis = "".join((ispis,"C"))
    #if flag == False:
    A()
    A()

def B():
    global niz, ispis, flag, brojac, znak

    ispis = "".join((ispis,"B"))
    
    if(znak == 'c'):
        if(brojac < len(niz)):
            znak = niz[brojac]
            brojac = brojac + 1
        else:
            flag = True
        if(znak == 'c'):
            if(brojac < len(niz)):
                znak = niz[brojac]
                brojac = brojac + 1
            else:
                flag = True
            S()
            if(znak == 'b'):
                if(brojac < len(niz)):
                    znak = niz[brojac]
                    brojac = brojac + 1
                else:
                    flag = True
                if(znak == 'c'):
                    if(brojac < len(niz)):
                        znak = niz[brojac]
                        brojac = brojac + 1
                    else:
                        flag = True
                else:
                    exitFunc()
            else:
                exitFunc()
        else:
            exitFunc()

def exitFunc():
    global ispis
    print(ispis)
    print("NE")
    exit()


#       MAIN        #

niz = input()

if(brojac < len(niz)):
    znak = niz[brojac]
    brojac = brojac + 1
else:
    znak = 'K'
    flag = True

S()

print(ispis)
if (flag != True):
    print("NE")
else:
    print("DA")
