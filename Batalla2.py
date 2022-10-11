# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 08:28:33 2022
Proyecto: Batalla Naval
@author: Christian Zavaleta
Ejercicio para: NICE CXone

Reglas y caracteristicas del juego:
El juego consiste en que dos jugadores (la PC es uno de ellos).
Ambos jugadores tienen 5 naves:
    1 Portaviones 5 espacios
    1 Acorazado 4 espacios
    1 Crucero 3 espacios
    1 Submarino 3 espacios
    1 Destructor 2 espacios
en sus tableros respectivos y tienen un 2do tablero para 
registrar los disparos que realizan al otro jugador.
Cada disparo al contrario puede ser "al agua" o "Impacto"
Cuando una nave ha recibido impactos igual a su tamaño esta
"hundida", gana el juego el jugador que logre hundir todas
las naves del otro jugador.
"""
import random
import sys

''' Variables globales '''
''''el tamaño de la nave es igual a sus vidas '''
filas = ['A','B','C','D','E','F','G','H','I','J']
columnas = [1,2,3,4,5,6,7,8,9,10]

t1 = [["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"]]

t2 = [["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"]]

t3 = [["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"],
     ["▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒","▒▒"]]
'''Vidas flota jugador'''
Por1 = 5
Aco1 = 4
Cru1 = 3
Sub1 = 3
Des1 = 2
'''Vidas flota PC'''
Por2 = 5
Aco2 = 4
Cru2 = 3
Sub2 = 3
Des2 = 2
'''Flota de cada jugador'''
Naves1 = 5
Naves2 = 5
'''Coordenadas del disparo'''
coord = ''

#%%
''' Imprime la tabla mat '''
def imprime_tabla(mat):
    l1 = ''
    lf = '  1 2 3 4 5 6 7 8 9 10'
    print(lf)
    for i in range(10):
        for j in range(10):
            l1 += str(mat[i][j])
        print(filas[i],l1)
        l1 = ''

#%%
''' Imprime ambos tableros del jugador, 1 con sus naves y otro en blanco
para registrar sus tiros '''
def imprime_tablas(taux1,taux2):
    l1 = ''
    l2 = ''
    print('                 BATALLA NAVAL')
    print('       TUS NAVES                TUS DISPAROS')
    lf = '  1 2 3 4 5 6 7 8 9 10      1 2 3 4 5 6 7 8 9 10'
    print(lf)
    for i in range(10):
        for j in range(10):
            l1 += str(taux1[i][j])
            l2 += str(taux2[i][j])
        print(filas[i],l1,'  ',filas[i],l2)
        l1 = ''
        l2 = ''

#%%
''' Funcion para verificar que el espacio para acomodar la nave 
este disponible y no solape otra barco'''
def esta_disp(auxi,auxj,tam, ori,taux):
    flag = True
    if ori=='H':
        for i in range(tam):
            if taux[auxi][i+auxj]!='▒▒':
                flag = False
    if ori=='V':
        for i in range(tam):
            if taux[i+auxi][auxj]!='▒▒':
                flag = False
    return flag
    
#%%
''' Coloca la nave indicada en "nom" en tablero "taux" en las 
coordenadas "auxi,auxj" verificando disponibilidad del espacio 
y que encaje dentro delos limites del tablero '''
def naves(auxi, auxj, nom, ori, taux):
    ''' Definimos tamaños de las naves'''
    if nom=='P':
        tam = 5
    elif nom=='A':
        tam = 4
    elif nom=='C':
        tam = 3
    elif nom=='S':
        tam = 3
    else:
        tam = 2
    ''' Validamos orientación y tamaño (0-9) '''
    if ori=='H':
        if auxj+tam-1 < 10:
            if esta_disp(auxi,auxj,tam,ori,taux):
                for k in range(tam):
                    taux[auxi][k+auxj] = nom+str(k+1)
            else:
                print('Otra nave esta utilizando parte del espacio!')
        else:
            print('Espacio insuficiente! relocalice la nave')
    if ori=='V':
        if auxi+tam-1 < 10:
            if esta_disp(auxi,auxj,tam,ori,taux):
                for k in range(tam):
                    taux[k+auxi][auxj] = nom+str(k+1)
            else:
                print('Otra nave esta utilizando parte del espacio!')
        else:
            print('Espacio insuficiente! relocalice la nave')

#%%
''' Validar que las coordenadas del disparo del jugador sean validas '''
def coord_ok(c):
    if len(c)>0:
        letra = c[0]
        numero = c[1:]
        try:
            float(numero)
        except ValueError:
            print("ERROR!ingrese coord valida")
            return False
        else:
            numero = int(c[1:])
            if letra not in filas or numero not in columnas:
                print("ERROR!ingrese coord valida")
                return False
            else:
                return True
    else:
        return False

#%%
''' Validar que el tiro no sea repetido'''
def es_nuevo(num1,num2):
    if t2[num1][num2]=='▒▒':
        return True
    else:
        print('Tiro Repetido')
        return False

#%%
''' Verifica cuando una nave ha sido hundida y cuantas quedan en 
    la flota, de cada jugador. Sin no queda ninguna finaliza el juego'''
def Control_flota(nave,n):
    global Por1,Aco1,Cru1,Sub1,Des1
    global Por2,Aco2,Cru2,Sub2,Des2
    global Naves1,Naves2
    global coord
    if nave == 'P' and n == 1:
        Por1 = Por1 - 1
        if Por1 == 0:
            print('Portaviones hundido')
            Naves1 = Naves1 - 1
    if nave == 'P' and n == 2:
        Por2 = Por2 - 1
        if Por2 == 0:
            print('Portaviones hundido')
            Naves2 = Naves2 - 1
    if nave == 'A' and n == 1:
        Aco1 = Aco1 - 1
        if Aco1 == 0:
            print('Acorazado hundido')
            Naves1 = Naves1 - 1
    if nave == 'A' and n == 2:
        Aco2 = Aco2 - 1
        if Aco2 == 0:
            print('Acorazado hundido')
            Naves2 = Naves2 - 1
    if nave == 'C' and n == 1:
        Cru1 = Cru1 - 1
        if Cru1 == 0:
            print('Crucero hundido')
            Naves1 = Naves1 - 1
    if nave == 'C' and n == 2:
        Cru2 = Cru2-1
        if Cru2==0:
            print('Crucero hundido')
            Naves2 = Naves2 - 1
    if nave == 'S' and n == 1:
        Sub1 = Sub1 - 1
        if Sub1 == 0:
            print('Submarino hundido')
            Naves1 = Naves1 - 1
    if nave == 'S' and n == 2:
        Sub2 = Sub2 - 1
        if Sub2 == 0:
            print('Submarino hundido')
            Naves2 = Naves2 - 1
    if nave == 'D' and n == 1:
        Des1 = Des1 - 1
        if Des1 == 0:
            print('Destructor hundido')
            Naves1 = Naves1 - 1
    if nave == 'D' and n == 2:
        Des2 = Des2 - 1
        if Des2 == 0:
            print('Destructor hundido')
            Naves2 = Naves2 - 1
    if Naves1 == 0 and n == 1:
        print('VICTORIA!!! Has hundido toda la flota enemiga del jugador')
        coord = 'X'
    if Naves2 == 0 and n == 2:
        print('VICTORIA!!! Has hundido toda la flota enemiga de PC')
        coord = 'X'
    
#%%
''' Registra el disparo del jugador en los tableros 
de los jugadores '''
def Registra_impacto(num1,num2):
    if t3[num1][num2]=='▒▒':
        t2[num1][num2]='OO'
        t3[num1][num2]='OO'
        print('Al agua!')
    else:
        print('impacto')
        nave = t3[num1][num2]
        ''' Donde nave es la nave impactada y el digito es la PC '''
        Control_flota(nave[0],2)
        t2[num1][num2]='**'
        t3[num1][num2]='**'

#%%
''' Registra la respuesta de la PC en los tableros de
los jugadores '''
def PC_responde():
    flag1 = True
    while flag1:
        n1 = random.randint(0,9)
        n2 = random.randint(0,9)
        if t1[n1][n2]!='OO' and t1[n1][n2]!='**':
            flag1 = False
    print('PC dispara a ',filas[n1],columnas[n2])
    if t1[n1][n2]=='▒▒':
        t1[n1][n2]='OO'
    else:
        print('impacto')
        nave = t1[n1][n2]
        ''' Donde nave es la nave impactada y el digito es el jugador '''
        Control_flota(nave[0],1)
        t1[n1][n2]='**'
        print('Booom! ahi hay algo')
    print('Te toca')
    
#%%
def ini_juego():
    naves(4,2,'P','V',t1)
    naves(1,7,'A','V',t1)
    naves(0,2,'C','H',t1)
    naves(6,5,'S','H',t1)
    naves(9,5,'D','H',t1)
    imprime_tablas(t1,t2)

#%%
def ini_pc():
    naves(0,3,'P','V',t3)
    naves(1,6,'A','H',t3)
    naves(3,9,'C','V',t3)
    naves(6,0,'S','H',t3)
    naves(9,4,'D','H',t3)
#%%
def jugar():
    global coord
    coord = ''
    print('Tu empiezas')
    while coord!='X':
        coord=input('Ingresa coordenadas Ejem:"C3" o "X" para salir: ')
        c1 = coord.upper()
        if c1!='X' and coord_ok(c1):
            n1 = ord(c1[0])-65
            n2 = int(c1[1:])
            n2 = n2-1
            if es_nuevo(n1,n2):
                Registra_impacto(n1,n2)
                PC_responde()
                imprime_tablas(t1,t2)
        if coord != 'X':
            coord = c1

#%%
ini_juego()
res = input('Quieres jugar? (S/N): ')
res = res.upper()
if res == 'S':
    ini_pc()
    jugar()
print('Hasta pronto!')


