#  jeu421-nihajer.py
#  Powered By EndMove
#  Copyright 2019 Jérémi_NIHART_-_classe5tc

from random import randrange
import os

noms = ["Agathe Zeublouse", "Alain Provist", "Alex Cité",
        "Andy Capé", "Annie Mâle", "Astérix Épéril",
        "Axel Ère", "Barack Afritt", "Beth Rave",
        "Cécile En Cieux", "Claire Hyère", "Daisy Rable",
        "Élie Coptère", "Ella Danloss", "Eric Hochet",
        "Gérard Manvussa", "Guy Yiotine", "Henri Hencor",
        "Jacques Sonne", "Jean Némard", "Jean Tanrien",
        "Justin Ptipeu", "Kelly Diote", "Karl Amelmou",
        "Marie Vière", "Médhi Khaman", "Pat Redway",
        "Sarah Pelpu", "Tarek Tifié", "Teddy Nainportekoi"]
        
#('win' ou 'lin' ou 'auto' -> pour détecter automatiquement le système)
system = "auto"
#Nombre de boots en partie normal
nbr_boot = 10

#ENDCOL powered by endmove.eu
class endcol:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0;39m'
    

#ENDCLEAR powered by endmove.eu
def endclear():
    if system == "auto":
        os.system('cls' if os.name=='nt' else 'clear')
    elif system == "win":
        os.system("cls")
    elif system == "lin":
        os.system("clear")
        
        
def de(face: int):
    if face >= 4 and face <= 20:
        if face != 10:
            return randrange(1, face)
        else:
            return randrange(0, face)
    else:
        return None


def lancerD6(nb: int, repet: bool = False):
    des = ()
    if repet:
        for y in range(0, nb):
            des += (de(6),)
        return des
    else:
        bcl = True
        check = []
        while bcl:
            if len(check) == nb:
                bcl = False
            else:
                if len(check) < 0:
                    check.append(de(6))
                else:
                    utilise = False
                    aleat = de(6)
                    for i in check:
                        if i == aleat:
                            utilise = True
                    if utilise == False:
                        check.append(aleat)
        return tuple(check)
            
    
def reassort(combi: tuple):
    ls_combi = list(combi)
    liste = []
    for i in range(0, len(ls_combi)):
        liste.append(max(ls_combi))
        ls_combi.remove(max(ls_combi))
    return tuple(liste)
    
    
def reserver_des(lances: tuple):
    dico = {4:0, 2:0, 1:0}
    if 4 in lances:
        cnt = lances.count(4)
        dico[4] = dico[4] + cnt
    elif 2 in lances:
        cnt = lances.count(2)
        dico[2] = dico[2] + cnt
    elif 1 in lances:
        cnt = lances.count(1)
        dico[1] = dico[1] + cnt
    return dico
    
    
def relancer_des(des_ok: dict):
    liste = []
    if des_ok[4] != 0:
        liste.append(4)
    else:
        jet = de(6)
        liste.append(jet)
    if des_ok[2] != 0:
        liste.append(2)
    else:
        jet = de(6)
        liste.append(jet)
    if des_ok[1] != 0:
        liste.append(1)
    else:
        jet = de(6)
        liste.append(jet)   
    return tuple(liste)
    

def jeu421(nbjoueurs: int):
    ls_player = []
    for i in range(0, nbjoueurs):
        chance = 2
        des = lancerD6(3, True)
        for y in range(0, chance):
            dico = reserver_des(des)
            lancer = relancer_des(dico)
        ls_player.append(lancer)
    return ls_player
    
    
def high_score(joueurs: list):
    if joueurs.count((4, 2, 1)) > 0:
        y = 2
    else:
        y = 1
    i = 0
    while i < len(joueurs):
        if joueurs[i] == (4, 2, 1):
            print("01.{}".format(joueurs[i]))
            joueurs.remove((4, 2, 1))
            while (4, 2, 1) in joueurs:
                print("   {}".format((4, 2, 1)))
                joueurs.remove((4, 2, 1))
        i += 1
    while 0 < len(joueurs):
        maxi = max(joueurs)
        print("{:02}.{}".format(y, maxi))
        joueurs.remove(max(joueurs))
        while maxi in joueurs:
            print("   {}".format(maxi))
            joueurs.remove(max(joueurs))
        y += 1

if __name__ == '__main__':
    start = True
    while start:
        print(endcol.GREEN,end="")
    #NOTE: Sous win un bug d'affichage des couleurs survient ici.
        print("""
          =====================================
               Welcome to the game of 421
          =====================================
        """, endcol.RESET)
        print("Choice of games:")
        print("  [1]: Boot start")
        print("  [2]: PLayer and {} boots start\n".format(nbr_boot))
        c = int(input("You choice: "))
        if c == 1 or c == 2:
            start = False
        else:
            endclear()
    if c == 1:
        nbr = int(input("How much boot do you want?: "))
        endclear()
        print(endcol.BLUE,end="")
        print("Here is the final result:",endcol.YELLOW)
        liste = jeu421(nbr)
        high_score(liste)
        print(endcol.RESET)
        input() #Pour bloquer l'arret sous win
    elif c == 2:
        chances = 2
        use_chances = True
        endclear()
        print("It's up to you to play, your first throw is: ",end="")
        lancer = lancerD6(3, True)
        print(reassort(lancer))
        while use_chances:
            if chances == 0:
                use_chances = False
            else:
                relance = input("Do you want to roll the missing dice? (O/n): ")
                endclear()
                if relance == "o" or relance == "n" or relance == "":
                    if relance == "n":
                        use_chances = False
                    else:
                        dico = reserver_des(lancer)
                        lancer = relancer_des(dico)
                        chances -= 1
                        print("Your new throw is: {}".format(lancer))
        liste = jeu421(nbr_boot)
        liste.append(lancer)
        endclear()
        print(endcol.BLUE,end="")
        print("You throw is: {}".format(lancer),endcol.YELLOW)
        high_score(liste)
        print(endcol.RESET)
        input() #Pour bloquer l'arret sous win
