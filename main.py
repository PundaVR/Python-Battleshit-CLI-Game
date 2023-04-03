import os
import time
import random

board = []
x = 10
y = 10
cpuBoats = 0
plyBoats = 0
lastCpuMove = 'n/a'
lastCpuHit = False
boatLengths = {0:5, 1: 4, 2: 3, 3:2}

def CreateBoard():
    global board
    global x
    global y
    board = [['[ ]' for i in range(y)] for j in range(x)]

def PrintBoard():
    j = 0
    k = 0
    count = 0
    countX= 0
    coordX = [['[ ]' for i in range(y)] for j in range(x)]
    coordY = [['[ ]' for i in range(y)] for j in range(x)]
    while j < x:
        #Create X and Y labels array
        coordX[j] = f'[{count}]'
        while k < y:
            coordY[k] = f'[{countX}]'
            k = k + 1
            countX = countX + 1
        countX = 0
        k = 0
        count = count + 1
        j = j + 1

    # Print X label
    newLine = ''
    for item in coordX:
        newLine = newLine + item
    print("[+]"+newLine)
    newLine = ''

    # Print board
    newLine = ''
    for line in board:
        for item in line:
            newLine = newLine + item
        print(coordY[k] + newLine) # Print Y label
        k = k +1 
        newLine = ''

def NumberBoard():
    j = 0
    k = 0
    count = 0
    countX= 0
    while j < x:
        board[j][0] = f'[{count}]'
        while k < y:
            board[j][k] = f'[{countX}]'
            k = k + 1
            countX = countX + 1
        countX = 0
        k = 0
        count = count + 1
        j = j + 1
    
def PlaceBoats():
    os.system('cls')
    PrintBoard()
    placed = 0
    for item, boat in boatLengths.items():
        plyInput = input(f"Enter boat {placed}/{len(boatLengths)} coord (in XY i.e. 43): ")
        while (len(plyInput) != 2 or plyInput.isnumeric() is False):
            plyInput = input(f"Enter boat {placed}/{len(boatLengths)} coord (in XY i.e. 43): ")    
        boatX = int(plyInput[0])
        boatY = int(plyInput[1])
        #plyInput = input("Enter the rotation boat coord: (in XY i.e. 43)")
        i = 0
        while i < boat: 
            board[boatY][boatX + i] = "[=]"
            i = i +1
        os.system('cls')
        PrintBoard()
        placed = placed+1

def CPUBoats():
    print("CPUBoats")

def CheckHit(x,y, cpuMove):
    if (board[y][x] == '[=]'):
        board[y][x] = '[X]'
        return True
    elif (board[y][x] == '[ ]'):
        if(cpuMove):
            board[y][x] = '[-]'
        else:
            board[y][x] = '[~]'

def GameUI():
    PrintBoard()
    print("\n=================================") 
    print(f"CPU Boats Left: {cpuBoats}")  
    print(f"CPU Bombed cell: {lastCpuMove}")    
    

def Attack(x,y, cpuMove):
    if(cpuMove):
        if(CheckHit(x,y, cpuMove)):
            CPU()
            return True
    else:
        if(CheckHit(x,y, cpuMove)):
            Move()
            return True
        else:
            CPU()

    
def CPU():
    # lol = input("cpu mimic?")
    #print("cpu mimic prunt?")
    cpuX = random.randint(0,9)
    cpuY = random.randint(0,9)
    global lastCpuMove
    lastCpuMove = f'{cpuX}{cpuY}'
    while(Attack(cpuX, cpuY, True)):
        cpuX = cpuX+1
        cpuY = cpuY
        
    

def CreateCpuBoats():
    print("createcpuboats")    

def Move():
    os.system('cls')
    GameUI()
    plyInput = input("Enter move (in XY i.e. 43)") 
    while (len(plyInput) != 2 or plyInput.isnumeric() is False):
        plyInput = input("Enter move (in XY i.e. 43)") 
    atkX = int(plyInput[0])
    atkY = int(plyInput[1])
    Attack(atkX,atkY,False)

def Game():
    os.system('cls')
    GameUI()
    Move()


CreateBoard()
#NumberBoard()
#plyInput = input("Are you ready to start? y/n:\n")
#while (plyInput.lower() != 'y' and plyInput.lower() != 'n'):
#    plyInput = input("Are you ready to start? y/n:\n")
if(True):#"y" in plyInput):
    PlaceBoats()
    alive = True
    plyInput = input("Enter first move (in XY i.e. 43)") 
    while (len(plyInput) != 2 or plyInput.isnumeric() is False):
        plyInput = input("Enter first move (in XY i.e. 43)") 
    atkX = int(plyInput[0])
    atkY = int(plyInput[1])
    Attack(atkX,atkY,False)
    while(alive):
        Game()