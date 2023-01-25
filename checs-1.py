import random
import os
import json

chemin = r"C:\Users\Duranty-PC\Desktop\Python\Chess_Game"

if not os.path.exists(chemin):
    os.makedirs(chemin)
chemin_trace = chemin + r"\trace_chess.json"

with open(chemin_trace,"w") as f:
    pass

#Création des pièces Blanche

P_w = [0,'Pion']
T_w = [0,'Tour']
C_w = [0,'Cava']
F_w = [0,'Fou ']
Q_w = [0,'Damm']
K_w = [0,'Roi ']

#Création des pièces noires
P_b = [1,'Pion']
T_b = [1,'Tour']
C_b = [1,'Cava']
F_b = [1,'Fou ']
Q_b = [1,'Damm']
K_b = [1,'Roi ']


#Création du plateau
vide = '     -   '
table_chess = [[vide for i in range(8)] for i in range(8)]

#Positionnement des Tours Blanche
table_chess[0][0] = table_chess[0][-1] = T_w
table_chess[0][1] = table_chess[0][-2] = C_w
table_chess[0][2] = table_chess[0][-3] = F_w   
table_chess[0][3] = Q_w
table_chess[0][-4] = K_w
table_chess[1] = [ P_w for i in range(8)]

#Position des pièces noires
table_chess[-1][0] = table_chess[-1][-1] = T_b
table_chess[-1][1] = table_chess[-1][-2] = C_b
table_chess[-1][2] = table_chess[-1][-3] =F_b
table_chess[-1][-4] = Q_b
table_chess[-1][3] = K_b
table_chess[-2] = [ P_b for i in range(8)]

o = 0
while o != -1:
    [print(table_chess[i]) for i in range(8)]
    if o % 2 == 0:
        in_u = input("Les blancs jouent : \n")
    else:
        in_u = input("Les noirs jouent : \n")
    if (not (len(in_u) == 5) or not in_u[0:2].isdigit() or not in_u[-2:].isdigit()):
        print("error")
    elif in_u[0:2] == in_u[-2:]:
        print("error")
    else:
        a,b,c,d = int(in_u[1]),int(in_u[0]),int(in_u[-1]),int(in_u[-2]),
        if table_chess[a][b][0] != o % 2:
            print("ce n'est pas votre tour de jouer !")
            o -= 1
        elif a not in range(8) or b not in range(8) or c not in range(8) or d not in range(8):
            print("Houlala")
        elif table_chess[c][d][0] == table_chess[a][b][0]:
            print("error")
        elif table_chess[a][b] == vide:
            print("error")
        #if (table_chess[a][b] == P_b or table_chess[a][b] == P_w) and a != c:
        #    print("damn")
         #   o -= 1
        else:
            with open(chemin_trace,"a") as f:
                json.dump((a,b,c,d),f)
            table_chess[c][d] = table_chess[a][b]
            table_chess[a][b] = vide
    o +=1