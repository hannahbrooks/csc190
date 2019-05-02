import sys
from random import randint 

def getPiece(name):
    if name=="pawn":
        return 0
    elif name=="knight":
        return 1
    elif name=="bishop":
        return 2
    elif name=="rook":
        return 3
    elif name=="queen":
        return 4
    elif name=="king":
        return 5
    else:
        return -1
    
def genBoard():
    r=[0]*64
    White=10
    Black=20
    for i in [ White, Black ]:
        if i==White:
            factor=+1
            shift=0
        else:
            factor=-1
            shift=63

        r[shift+factor*7] = r[shift+factor*0] = i+getPiece("rook")
        r[shift+factor*6] = r[shift+factor*1] = i+getPiece("knight")
        r[shift+factor*5] = r[shift+factor*2] = i+getPiece("bishop")
        if i==White:
            r[shift+factor*4] = i+getPiece("queen") # queen is on its own color square
            r[shift+factor*3] = i+getPiece("king")
        else:
            r[shift+factor*3] = i+getPiece("queen") # queen is on its own color square
            r[shift+factor*4] = i+getPiece("king")

        for j in range(0,8):
            r[shift+factor*(j+8)] = i+getPiece("pawn")

    return r

def printNumbers():
    nums=[[l for l in range(8,0, -1)],[l for l in range(16,8,-1)], [l for l in range(24,16,-1)], [l for l in range(32,24,-1)], [l for l in range(40,32,-1)], [l for l in range(48,40,-1)], [l for l in range(56, 48,-1)], [l for l in range(64, 56,-1)]]
    for i in range(7,-1,-1):
        print("")
        for j in nums[i]:
            sys.stdout.write('{0: <5}'.format(j))
    return

def printBoard(board):
    accum="---- BLACK SIDE ----\n"
    max=63
    for j in range(0,8,1):
        for i in range(max-j*8,max-j*8-8,-1):
            accum=accum+'{0: <5}'.format(board[i])
        accum=accum+"\n"
    accum=accum+"---- WHITE SIDE ----"
    return accum

def GetPlayerPositions(board,player):
    listOfPlayers = board

    if (player != 10) and (player != 20):
        return False

    if player==10:
        for i in range(len(listOfPlayers)):

            if listOfPlayers[i]>=20:
                listOfPlayers[i]=0
            else:
                listOfPlayers[i]=1
    if player==20:
        for i in range(len(listOfPlayers)+1):
            if listOfPlayers[i]<20:
                listOfPlayers[i]=0
            else:
                listOfPlayers[i]=1

    return listOfPlayers

def GetPieceLegalMoves(board,position):
    accum = []
    if board[position] >=20:
        piece = board[position]-20
    else:
        piece = board[position]-10

    if piece==0: 
        accum = legalPawnMoves(board,position)
    elif piece==1:
        accum =  legalKnightMoves(board,position)
    elif piece==2:
        accum =  legalBishopMoves(board,position)
    elif piece==4:
        accum =  legalQueenMoves(board,position)
    elif piece==5:
        accum =  legalKingMoves(board,position)
    return accum

def legalPawnMoves(board, position):
    legalMoves = board

    if board[position] == 20:
        if board[position-8] == 0 and position-8 < 63 and position-8 > 0:
            legalMoves[position-8] = 1
        for i in range(10,15):
            if board[position-7] == i and  position-7 < 63 and position-7 > 0 and position != 63 and position != 55 and position != 47 and position != 39 and position != 31 and position != 23 and position != 15 and position != 7:
                legalMoves[position-7] = 2
            if board[position-9] == i and position-9 < 63 and position-9 > 0 and position != 56 and position != 48 and position != 40 and position != 32 and position != 24 and position != 16 and position != 8 and position != 0:
                legalMoves[position-9] = 2
    if board[position] == 10:
        if board[position+8] == 0 and position+8 < 63 and position+8 > 0:
            legalMoves[position+8] = 1
    for i in range(20,25):
        if board[position+7] == i and position+7 < 63 and position+7 > 0  and position != 56 and position != 48 and position != 40 and position != 32 and position != 24 and position != 16 and position != 8 and position != 0:
            legalMoves[position+7] = 2
        if board[position+9] == i and position+9 < 63 and position+9 > 0 and position != 63 and position != 55 and position != 47 and position != 39 and position != 31 and position != 23 and position != 15 and position != 7:
            legalMoves[position+9] = 2
        
    return legalMoves

def legalKingMoves(board,pos):
    legalMoves = board
    if legalMoves[pos]==15:
        if (pos!= 8 and pos !=16 and pos != 24 and pos != 32 and pos !=40 and pos !=48 and pos !=56 and pos !=64):
            if legalMoves[pos + 1] == 0:
                legalMoves[pos + 1] = 1
            elif legalMoves[pos + 1] == 20 or legalMoves[pos + 1] == 21 or legalMoves[pos + 1] == 22 or legalMoves[pos + 1] == 23 or legalMoves[pos + 1] == 24 or legalMoves[pos + 1] == 25:
                legalMoves[pos + 1] = 2
        if (pos!= 1 and pos !=9 and pos != 17 and pos != 25 and pos !=33 and pos !=41 and pos !=49 and pos !=57):
            if legalMoves[pos - 1] == 0:
                legalMoves[pos - 1] = 1
            elif legalMoves[pos - 1] == 20 or legalMoves[pos - 1] == 21 or legalMoves[pos - 1] == 22 or legalMoves[pos - 1] == 23 or legalMoves[pos - 1] == 24 or legalMoves[pos - 1] == 25:
                legalMoves[pos - 1] = 2   
        if (pos!= 64 and pos !=63 and pos != 62 and pos != 61 and pos != 60 and pos != 59 and pos !=58 and pos !=57):
            if legalMoves[pos + 8] == 0:
                legalMoves[pos + 8] = 1
            elif legalMoves[pos + 8] == 20 or legalMoves[pos + 8] == 21 or legalMoves[pos + 8] == 22 or legalMoves[pos + 8] == 23 or legalMoves[pos + 8] == 24 or legalMoves[pos + 8] == 25:
                legalMoves[pos + 8] = 2
        if (pos!= 8 and pos !=7 and pos != 6 and pos != 5 and pos !=4 and pos !=3 and pos !=2 and pos !=1):
            if legalMoves[pos -8] == 0:
                legalMoves[pos -8] = 1
            elif legalMoves[pos -8] == 20 or legalMoves[pos - 8] == 21 or legalMoves[pos - 8] == 22 or legalMoves[pos - 8] == 23 or legalMoves[pos - 8] == 24 or legalMoves[pos - 8] == 25:
                legalMoves[pos - 8] = 2
        if (pos!= 8 and pos !=16 and pos != 24 and pos != 32 and pos !=40 and pos !=48 and pos !=56 and pos !=64 and pos!= 64 and pos !=63 and pos != 62 and pos != 61 and pos != 60 and pos != 59 and pos !=58 and pos !=67):
            if legalMoves[pos + 9] == 0:
                legalMoves[pos + 9] = 1
            elif legalMoves[pos + 9] == 20 or legalMoves[pos + 9] == 21 or legalMoves[pos + 9] == 22 or legalMoves[pos + 9] == 23 or legalMoves[pos + 9] == 24 or legalMoves[pos + 9] == 25:
                legalMoves[pos + 9] = 2
        if (pos!= 8 and pos !=16 and pos != 24 and pos != 32 and pos !=40 and pos !=48 and pos !=56 and pos !=64 and pos !=7 and pos != 6 and pos != 5 and pos !=4 and pos !=3 and pos !=2 and pos !=1):
            if legalMoves[pos -7] == 0:
                legalMoves[pos - 7] = 1
            elif legalMoves[pos - 7] == 20 or legalMoves[pos - 7] == 21 or legalMoves[pos - 7] == 22 or legalMoves[pos - 7] == 23 or legalMoves[pos - 7] == 24 or legalMoves[pos - 7] == 25:
                legalMoves[pos - 7] = 2
        if (pos!= 64 and pos !=63 and pos != 62 and pos != 61 and pos != 60 and pos != 59 and pos !=58 and pos !=57 and pos!= 1 and pos !=9 and pos != 17 and pos != 25 and pos !=33 and pos !=41 and pos !=49):
            if legalMoves[pos + 7] == 0:
                legalMoves[pos + 7] = 1
            elif legalMoves[pos + 7] == 20 or legalMoves[pos + 7] == 21 or legalMoves[pos + 7] == 22 or legalMoves[pos + 7] == 23 or legalMoves[pos + 7] == 24 or legalMoves[pos + 7] == 25:
                legalMoves[pos + 7] = 2
        if (pos!= 57 and pos !=49 and pos != 41 and pos != 33 and pos != 25 and pos != 17 and pos !=9 and pos !=2 and pos!= 1 and pos !=3 and pos != 4 and pos != 5 and pos !=6 and pos !=7 and pos !=8):
            if legalMoves[pos - 9] == 0:
                legalMoves[pos - 9] = 1
            elif legalMoves[pos - 9] == 20 or legalMoves[pos - 9] == 21 or legalMoves[pos - 9] == 22 or legalMoves[pos - 9] == 23 or legalMoves[pos - 9] == 24 or legalMoves[pos - 9] == 25:
                legalMoves[pos - 9] = 2
    if legalMoves[pos]==25:
        if (pos!= 8 and pos !=16 and pos != 24 and pos != 32 and pos !=40 and pos !=48 and pos !=56 and pos !=64):
            if legalMoves[pos + 1] == 0:
                legalMoves[pos + 1] = 1
            elif legalMoves[pos + 1] == 10 or legalMoves[pos + 1] == 11 or legalMoves[pos + 1] == 12 or legalMoves[pos + 1] == 13 or legalMoves[pos + 1] == 14 or legalMoves[pos + 1] == 15:
                legalMoves[pos + 1] = 2
        if (pos!= 1 and pos !=9 and pos != 17 and pos != 25 and pos !=33 and pos !=41 and pos !=49 and pos !=57):
            if legalMoves[pos - 1] == 0:
                legalMoves[pos - 1] = 1
            elif legalMoves[pos - 1] == 10 or legalMoves[pos - 1] == 11 or legalMoves[pos - 1] == 12 or legalMoves[pos - 1] == 13 or legalMoves[pos - 1] == 14 or legalMoves[pos - 1] == 15:
                legalMoves[pos - 1] = 2   
        if (pos!= 64 and pos !=63 and pos != 62 and pos != 61 and pos != 60 and pos != 59 and pos !=58 and pos !=57):
            if legalMoves[pos + 8] == 0:
                legalMoves[pos + 8] = 1
            elif legalMoves[pos + 8] == 10 or legalMoves[pos + 8] == 11 or legalMoves[pos + 8] == 12 or legalMoves[pos + 8] == 13 or legalMoves[pos + 8] == 14 or legalMoves[pos + 8] == 15:
                legalMoves[pos + 8] = 2
        if (pos!= 8 and pos !=7 and pos != 6 and pos != 5 and pos !=4 and pos !=3 and pos !=2 and pos !=1):
            if legalMoves[pos -8] == 0:
                legalMoves[pos -8] = 1
            elif legalMoves[pos -8] == 10 or legalMoves[pos - 8] == 11 or legalMoves[pos - 8] == 12 or legalMoves[pos - 8] == 13 or legalMoves[pos - 8] == 14 or legalMoves[pos - 8] == 15:
                legalMoves[pos - 8] = 2
        if (pos!= 8 and pos !=16 and pos != 24 and pos != 32 and pos !=40 and pos !=48 and pos !=56 and pos !=64 and pos!= 64 and pos !=63 and pos != 62 and pos != 61 and pos != 60 and pos != 59 and pos !=58 and pos !=67):
            if legalMoves[pos + 9] == 0:
                legalMoves[pos + 9] = 1
            elif legalMoves[pos + 9] == 10 or legalMoves[pos + 9] == 11 or legalMoves[pos + 9] == 12 or legalMoves[pos + 9] == 13 or legalMoves[pos + 9] == 14 or legalMoves[pos + 9] == 15:
                legalMoves[pos + 9] = 2
        if (pos!= 8 and pos !=16 and pos != 24 and pos != 32 and pos !=40 and pos !=48 and pos !=56 and pos !=64 and pos !=7 and pos != 6 and pos != 5 and pos !=4 and pos !=3 and pos !=2 and pos !=1):
            if legalMoves[pos -7] == 0:
                legalMoves[pos - 7] = 1
            elif legalMoves[pos - 7] == 10 or legalMoves[pos - 7] == 11 or legalMoves[pos - 7] == 12 or legalMoves[pos - 7] == 13 or legalMoves[pos - 7] == 14 or legalMoves[pos - 7] == 15:
                legalMoves[pos - 7] = 2
        if (pos!= 64 and pos !=63 and pos != 62 and pos != 61 and pos != 60 and pos != 59 and pos !=58 and pos !=57 and pos!= 1 and pos !=9 and pos != 17 and pos != 25 and pos !=33 and pos !=41 and pos !=49):
            if legalMoves[pos + 7] == 0:
                legalMoves[pos + 7] = 1
            elif legalMoves[pos + 7] == 10 or legalMoves[pos + 7] == 11 or legalMoves[pos + 7] == 12 or legalMoves[pos + 7] == 13 or legalMoves[pos + 7] == 14 or legalMoves[pos + 7] == 15:
                legalMoves[pos + 7] = 2
        if (pos!= 57 and pos !=49 and pos != 41 and pos != 33 and pos != 25 and pos != 17 and pos !=9 and pos !=2 and pos!= 1 and pos !=3 and pos != 4 and pos != 5 and pos !=6 and pos !=7 and pos !=8):
            if legalMoves[pos - 9] == 0:
                legalMoves[pos - 9] = 1
            elif legalMoves[pos - 9] == 10 or legalMoves[pos - 9] == 11 or legalMoves[pos - 9] == 12 or legalMoves[pos - 9] == 13 or legalMoves[pos - 9] == 14 or legalMoves[pos - 9] == 15:
                legalMoves[pos - 9] = 2   
    return legalMoves

def legalKnightMoves (board, pos):
    legalMoves = board
       #1 means open move 2 means kill
    if legalMoves[pos] ==11:
        if (pos != 56 and pos != 57 and pos != 58 and pos !=59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos != 48 and pos != 49 and pos != 50 and pos != 51 and pos != 52 and pos != 53 and pos != 54 and pos != 55 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 0 and pos != 8):
            if legalMoves[pos + 15] == 0:
                legalMoves[pos + 15] = 1
            elif legalMoves[pos + 15] == 20 or legalMoves[pos + 15] == 21 or legalMoves[pos + 15] == 22 or legalMoves[pos + 15] == 23 or legalMoves[pos + 15] == 24 or legalMoves[pos + 15] == 25:
                legalMoves[pos + 15] = 2

        if (pos != 56 and pos != 57 and pos != 58 and pos !=59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos != 48 and pos != 49 and pos != 50 and pos != 51 and pos != 52 and pos != 53 and pos != 54 and pos != 55 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 7 and pos != 15):
            if legalMoves[pos + 17] == 0:
                 legalMoves[pos + 17] = 1
            elif legalMoves[pos + 17] == 20 or legalMoves[pos + 17] == 21 or legalMoves[pos + 17] == 22 or legalMoves[pos + 17] == 23 or legalMoves[pos + 17] == 24 or legalMoves[pos + 17] == 25:
                 legalMoves[pos + 17] = 2

        if (pos != 56 and pos != 57 and pos != 58 and pos !=59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 0 and pos != 9 and pos != 17 and pos != 25 and pos != 33 and pos != 41 and pos != 49 and pos != 1):
            if legalMoves[pos + 6] == 0:
                legalMoves[pos + 6] = 1
            elif legalMoves[pos + 6] == 20 or legalMoves[pos + 6] == 21 or legalMoves[pos + 6] == 22 or legalMoves[pos + 6] == 23 or legalMoves[pos + 6] == 24 or legalMoves[pos + 6] == 25:                                        legalMoves[pos + 6] = 2

        if (pos != 56 and pos != 57 and pos != 58 and pos !=59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos != 14 and pos != 22 and pos != 30 and pos != 38 and pos != 46 and pos != 54 and pos != 6 and pos != 15 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 7):
            if legalMoves[pos + 10] == 0:
                legalMoves[pos + 10] = 1
            elif legalMoves[pos + 10] == 20 or legalMoves[pos + 10] == 21 or legalMoves[pos + 10] == 22 or legalMoves[pos + 10] == 23 or legalMoves[pos + 10] == 24 or legalMoves[pos + 10] == 25:
                legalMoves[pos + 10] = 2

        if (pos != 0 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 56 and pos != 1 and pos != 9 and pos != 17 and pos != 25 and pos != 33 and pos != 41 and pos != 49 and pos != 57 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7):
            if legalMoves[pos - 10] == 0:
                legalMoves[pos - 10] = 1
            elif legalMoves[pos - 10] == 20 or legalMoves[pos - 10] == 21 or legalMoves[pos - 10] == 22 or legalMoves[pos - 10] == 23 or legalMoves[pos - 10] == 24 or legalMoves[pos - 10] == 25:
                legalMoves[pos - 10] = 2

        if (pos != 0 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 56 and pos != 0 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos != 8 and pos != 9 and pos != 10 and pos != 11 and pos != 12 and pos != 13 and pos != 14 and pos != 15):
            if legalMoves[pos - 17] == 0:
                legalMoves[pos - 17] = 1
            elif legalMoves[pos - 17] == 20 or legalMoves[pos - 17] == 21 or legalMoves[pos - 17] == 22 or legalMoves[pos - 17] == 23 or legalMoves[pos - 17] == 24 or legalMoves[pos - 17] == 25:
                legalMoves[pos - 17] = 2

        if (pos != 7 and pos != 15 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 63 and pos != 0 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos != 8 and pos != 9 and pos != 10 and pos != 11 and pos != 12 and pos != 13 and pos != 14 and pos != 15):
            if legalMoves[pos - 15] == 0:
                legalMoves[pos - 15] = 1
            elif legalMoves[pos - 15] == 20 or legalMoves[pos - 15] == 21 or legalMoves[pos - 15] == 22 or legalMoves[pos - 15] == 23 or legalMoves[pos - 15] == 24 or legalMoves[pos - 15] == 25:
                legalMoves[pos - 15] = 2


        if (pos != 7 and pos != 15 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 63 and pos != 0 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos != 8 and pos != 9 and pos != 10 and pos != 11 and pos != 12 and pos != 13 and pos != 14 and pos != 15):
            if legalMoves[pos - 6] == 0:
                legalMoves[pos - 6] = 1
            elif legalMoves[pos - 6] == 20 or legalMoves[pos - 6] == 21 or legalMoves[pos - 6] == 22 or legalMoves[pos - 6] == 23 or legalMoves[pos - 6] == 24 or legalMoves[pos - 6] == 25:
                legalMoves[pos - 6] = 2


    if legalMoves[pos] == 21:
        if (pos != 56 and pos != 57 and pos != 58 and pos !=59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos != 48 and pos != 49 and pos != 50 and pos != 51 and pos != 52 and pos != 53 and pos != 54 and pos != 55 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 0 and pos != 8):
            if board[pos + 15] == 0:
                legalMoves[pos + 15] = 1
            elif board[pos + 15] == 10 or board[pos + 15] == 11 or board[pos + 15] == 12 or board[pos + 15] == 13 or board[pos + 15] == 14 or board[pos + 15] == 15:
                legalMoves[pos + 15] = 2

        if (pos != 56 and pos != 57 and pos != 58 and pos !=59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos != 48 and pos != 49 and pos != 50 and pos != 51 and pos != 52 and pos != 53 and pos != 54 and pos != 55 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 7 and pos != 15):
            if board[pos + 17] == 0:
                legalMoves[pos + 17] = 1
            elif board[pos + 17] == 10 or board[pos + 17] == 11 or board[pos + 17] == 12 or board[pos + 17] == 13 or board[pos + 17] == 14 or board[pos + 17] == 15:
                legalMoves[pos + 17] = 2

        if (pos != 56 and pos != 57 and pos != 58 and pos !=59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 0 and pos != 9 and pos != 17 and pos != 25 and pos != 33 and pos != 41 and pos != 49 and pos != 1):
            if board[pos + 6] == 0:
                legalMoves[pos + 6] = 1
            elif board[pos + 6] == 10 or board[pos + 6] == 11 or board[pos + 6] == 12 or board[pos + 6] == 13 or board[pos + 6] == 14 or board[pos + 6] == 15:
                legalMoves[pos + 6] = 2

        if (pos != 56 and pos != 57 and pos != 58 and pos !=59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos != 14 and pos != 22 and pos != 30 and pos != 38 and pos != 46 and pos != 54 and pos != 6 and pos != 15 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 7):
            if board[pos + 10] == 0:
                legalMoves[pos + 10] = 1
            elif board[pos + 10] == 10 or board[pos + 10] == 11 or board[pos + 10] == 12 or board[pos + 10] == 13 or board[pos + 10] == 14 or board[pos + 10] == 15:
                legalMoves[pos + 10] = 2

        if (pos != 0 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 56 and pos != 1 and pos != 9 and pos != 17 and pos != 25 and pos != 33 and pos != 41 and pos != 49 and pos != 57 and pos != 0 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7):
            if board[pos - 10] == 0:
                legalMoves[pos - 10] = 1
            elif board[pos - 10] == 10 or board[pos - 10] == 11 or board[pos - 10] == 12 or board[pos - 10] == 13 or board[pos - 10] == 14 or board[pos - 10] == 15:
                legalMoves[pos - 10] = 2

        if (pos != 0 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 56 and pos != 0 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos != 8 and pos != 9 and pos != 10 and pos != 11 and pos != 12 and pos != 13 and pos != 14 and pos != 15):
            if board[pos - 17] == 0:
                legalMoves[pos - 17] = 1
            elif board[pos - 17] == 10 or board[pos - 17] == 11 or board[pos - 17] == 12 or board[pos - 17] == 13 or board[pos - 17] == 14 or board[pos - 17] == 15:
                legalMoves[pos - 17] = 2

        if (pos != 7 and pos != 15 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 63 and pos != 0 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos != 8 and pos != 9 and pos != 10 and pos != 11 and pos != 12 and pos != 13 and pos != 14 and pos != 15):
            if board[pos - 15] == 0:
                legalMoves[pos - 17] = 1
            elif board[pos - 15] == 10 or board[pos - 15] == 11 or board[pos - 15] == 12 or board[pos - 15] == 13 or board[pos - 15] == 14 or board[pos - 15] == 15:
                legalMoves[pos - 17] = 2

        if (pos != 7 and pos != 15 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 63 and pos != 0 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos != 8 and pos != 9 and pos != 10 and pos != 11 and pos != 12 and pos != 13 and pos != 14 and pos != 15):
            if board[pos - 6] == 0:
                legalMoves[pos - 6] = 1
            elif board[pos - 6] == 10 or board[pos - 6] == 11 or board[pos - 6] == 12 or board[pos - 6] == 13 or board[pos - 6] == 14 or board[pos - 6] == 15:
                legalMoves[pos - 6] = 2

    return legalMoves

def legalBishopMoves(board, pos):
    legalMoves=board
    if board[pos]==22:
        if pos != 0 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 56 and pos != 57 and pos != 58 and pos != 59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos > 0 and pos < 63:
            if board[pos + 7] == 0:
                legalMoves[pos + 7] = 1   
            elif board[pos + 7] == 10 or board[pos + 7] == 11 or board[pos + 7] == 12 or board[pos + 7] == 13 or board[pos + 7] == 14 or board[pos + 7] == 15:
                legalMoves[pos + 7] = 2

        if pos != 7 and pos != 15 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 63 and pos != 57 and pos != 58 and pos != 59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos > 0 and pos < 63: #
            if board[pos + 9] == 0:
                legalMoves[pos + 9] = 1
            elif board[pos + 9] == 10 or board[pos + 9] == 11 or board[pos + 9] == 12 or board[pos + 9] == 13 or board[pos + 9] == 14 or board[pos + 9] == 15:
                legalMoves[pos + 9] = 2
            if pos != 0 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 56 and pos != 0 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos > 0 and pos < 63: 
                if board[pos - 9] == 0:
                    legalMoves[pos - 9] = 1
                elif board[pos - 9] == 10 or board[pos - 9] == 11 or board[pos - 9] == 12 or board[pos - 9] == 13 or board[pos - 9] == 14 or board[pos - 9] == 15:
                    legalMoves[pos - 9] = 2

            if pos != 7 and pos != 15 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 63 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos > 0 and pos < 63: 
                if board[pos - 7] == 0:
                    legalMoves[pos - 7] = 1
                elif board[pos - 7] == 10 or board[pos - 7] == 11 or board[pos - 7] == 12 or board[pos - 7] == 13 or board[pos - 7] == 14 or board[pos - 7] == 15: 
                    legalMoves[pos - 7] = 2 
    if board[pos]==12:
        if pos != 0 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 56 and pos != 57 and pos != 58 and pos != 59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos > 0 and pos < 63:
            if board[pos + 7] == 0:
                legalMoves[pos + 7] = 1   
            elif board[pos + 7] == 20 or board[pos + 7] == 21 or board[pos + 7] == 22 or board[pos + 7] == 23 or board[pos + 7] == 24 or board[pos + 7] == 25:
                legalMoves[pos + 7] = 2

        if pos != 7 and pos != 25 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 63 and pos != 57 and pos != 58 and pos != 59 and pos != 60 and pos != 61 and pos != 62 and pos != 63 and pos > 0 and pos < 63: 
            if board[pos + 9] == 0:
                legalMoves[pos + 9] = 1
            elif board[pos + 9] == 20 or board[pos + 9] == 21 or board[pos + 9] == 22 or board[pos + 9] == 23 or board[pos + 9] == 24 or board[pos + 9] == 25:
                legalMoves[pos + 9] = 2
            if pos != 0 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 56 and pos != 0 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos > 0 and pos < 63: 
                if board[pos - 9] == 0:
                    legalMoves[pos - 9] = 1
                elif board[pos - 9] == 20 or board[pos - 9] == 21 or board[pos - 9] == 22 or board[pos - 9] == 23 or board[pos - 9] == 24 or board[pos - 9] == 25:
                    legalMoves[pos - 9] = 2

            if pos != 7 and pos != 25 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 63 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos > 0 and pos < 63: 
                if board[pos - 7] == 0:
                    legalMoves[pos - 7] = 1
                elif board[pos - 7] == 20 or board[pos - 7] == 21 or board[pos - 7] == 22 or board[pos - 7] == 23 or board[pos - 7] == 24 or board[pos - 7] == 25: 
                    legalMoves[pos - 7] = 2
    return legalMoves

def legalRookMoves (board, pos):
    legalMoves = board
    if board[pos]==23:
        if pos != 56 and pos != 57 and pos != 58 and pos != 59 and pos !=  60 and pos != 61 and pos != 62 and pos != 63 and pos > 0 and pos < 63:
            if board[pos + 8] == 0:
	            legalMoves[pos + 8] = 1
            elif board[pos + 8] == 10 or board[pos + 8] == 11 or board[pos + 8] == 12 or board[pos + 8] == 13 or board[pos + 8] == 14 or board[pos + 8] == 15:
	            legalMoves[pos + 8] = 2
        if pos != 0 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 56 and pos > 0 and pos < 63: 
            if board[pos - 1] == 0:
	            legalMoves[pos - 1] = 1
            elif board[pos - 1] == 10 or board[pos - 1] == 11 or board[pos - 1] == 12 or board[pos - 1] == 13 or board[pos - 1] == 14 or board[pos - 1] == 15:
	            legalMoves[pos - 1] = 2
        if pos != 0 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos > 0 and pos < 63:
            if board[pos - 8] == 0:
	            legalMoves[pos - 8] = 1
            elif board[pos - 8] == 10 or board[pos - 8] == 11 or board[pos - 8] == 12 or board[pos - 8] == 13 or board[pos - 8] == 14 or board[pos - 8] == 15:
	            legalMoves[pos - 8] = 1
        if pos != 7 and pos != 15 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 63 and pos > 0 and pos < 63:
            if board[pos + 1] == 0:
	            legalMoves[pos + 1] = 1
            elif board[pos + 1] == 10 or board[pos + 1] == 11 or board[pos + 1] == 12 or board[pos + 1] == 13 or board[pos + 1] == 14 or board[pos + 1] == 15:
	            legalMoves[pos + 1] = 1
    if board[pos]==13:
        if pos != 56 and pos != 57 and pos != 58 and pos != 59 and pos !=  60 and pos != 61 and pos != 62 and pos != 63 and pos > 0 and pos < 63:
            if board[pos + 8] == 0:
	            legalMoves[pos + 8] = 1
            elif board[pos + 8] == 20 or board[pos + 8] == 21 or board[pos + 8] == 22 or board[pos + 8] == 23 or board[pos + 8] == 24 or board[pos + 8] == 25:
	            legalMoves[pos + 8] = 2
        if pos != 0 and pos != 8 and pos != 16 and pos != 24 and pos != 32 and pos != 40 and pos != 48 and pos != 56 and pos > 0 and pos < 63: 
            if board[pos - 1] == 0:
	            legalMoves[pos - 1] = 1
            elif board[pos - 1] == 20 or board[pos - 1] == 21 or board[pos - 1] == 22 or board[pos - 1] == 23 or board[pos - 1] == 24 or board[pos - 1] == 25:
	            legalMoves[pos - 1] = 2
        if pos != 0 and pos != 1 and pos != 2 and pos != 3 and pos != 4 and pos != 5 and pos != 6 and pos != 7 and pos > 0 and pos < 63:
            if board[pos - 8] == 0:
	            legalMoves[pos - 8] = 1
            elif board[pos - 8] == 20 or board[pos - 8] == 21 or board[pos - 8] == 22 or board[pos - 8] == 23 or board[pos - 8] == 24 or board[pos - 8] == 25:
	            legalMoves[pos - 8] = 1
        if pos != 7 and pos != 15 and pos != 23 and pos != 31 and pos != 39 and pos != 47 and pos != 55 and pos != 63 and pos > 0 and pos < 63:
            if board[pos + 1] == 0:
	            legalMoves[pos + 1] = 1
            elif board[pos + 1] == 20 or board[pos + 1] == 21 or board[pos + 1] == 22 or board[pos + 1] == 23 or board[pos + 1] == 24 or board[pos + 1] == 25:
	            legalMoves[pos + 1] = 1

    return legalMoves

def legalQueenMoves(pos):
    return legalRookMoves(pos) + legalBishopMoves(pos)

def isPositionUnderThreat(board,position,player):
    for i in range (0,64):
        if player==10:
            if board[i]>=20:
                if board[i]==20:
                    x=legalPawnMoves(board,board[i])
                    for i in x:
                        if position==x[i]:
                            return True
                        else:
                            return False
                if board[i]==21:
                    x=legalKingMoves(board,board[i])
                    for i in x:
                        if position==x[i]:
                            return True
                        else:
                            return False
                if board[i]==22:
                    x=legalBishopMoves(board,board[i])
                    for i in x:
                        if position==x[i]:
                            return True
                        else:
                            return False
            if board[i]==23:
                x=legalRookMoves(board,board[i])
                for i in x:
                    if position==x[i]:
                        return True
                    else:
                        return False
            if board[i]==24:
                x=legalQueenMoves(board, board[i])
                for i in x:
                    if position==x[i]:
                        return True
                    else:
                        return False
            if board[i]==25:
                x=legalKingMoves(board, board[i])
                for i in x:
                    if position==x[i]:
                        return True
                    else:
                        return False
    if player==20:
        if board[i]<20 and board[i]!=0:
            if board[i]==10:
                x=legalPawnMoves(board,board[i])
                for i in x:
                    if position==x[i]:
                        return True
                    else:
                        return False
            if board[i]==11:
                x=legalKingMoves(board,board[i])
                for i in x:
                     if position==x[i]:
                        return True
                     else:
                        return False
            if board[i]==12:
                x=legalBishopMoves(board,board[i])
                for i in x:
                    if position==x[i]:
                        return True
                    else:
                        return False
            if board[i]==13:
                x=legalRookMoves(board,board[i])
                for i in x:
                    if position==x[i]:
                        return True
                    else:
                        return False
            if board[i]==14:
                x=legalQueenMoves(board, board[i])
                for i in x:
                    if position==x[i]:
                        return True
                    else:
                        return False
            if board[i]==15:
                x=legalKingMoves(board, board[i])
                for i in x:
                    if position==x[i]:
                        return True
                    else:
                        return False


def genRandomMove(board,player):
    whichpiece=random.randint(0,5)
    piece=whichpiece + player
    x=GetPieceLegalMoves(board,piece)
    move=random.randint(0,len(x))
    while isPositionUnderThreat(board,x[move], player)==True:
        move=random.randint(0,len(x))
    return x[move]

def piecescore(piece):
    if piece == 10 or piece == 20:
        return 0
    if piece == 11 or piece == 21:
        return 30
    elif piece == 12 or piece == 22:
        return 30
    elif piece == 13 or piece == 23:
        return 50
    elif piece == 14 or piece == 24:
        return 90
    elif piece == 15 or piece == 25:
        return 900
    else:
        return -1

def evaluateboardscore(board):
    sum = 0
    for i in range (0,64):
        if board[i] == 0:
            add=0
            sum=sum+add
        if board[i]==10:
            add=10
            sum=sum+add
        elif board[i]==11:
            add=30
            sum=sum+add
        elif board[i]==12:
            add=30
            sum=sum+add
        elif board[i]==13:
            add=50
            sum=sum+add
        elif board [i]==14:
            add=90
            sum=sum+add
        elif board[i]==15:
            add=900
            sum=sum+add
        elif board[i]==20:
            add=-10
            sum=sum+add
        elif board[i]==21:
            add=-30
            sum=sum+add
        elif board[i]==22:
            add=-30
            sum=sum+add
        elif board[i]==23:
            add=-50
            sum=sum+add
        elif board [i]==24:
            add=-90
            sum=sum+add
        elif board[i]==25:
            add=-900
            sum=sum+add
    return sum

class tree:
    def __init__(self,x):
        self.store = [x,[]]

    def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True

    def GetSucc(self):
        return self.store[1]

    def Print_DepthFirst(self):
        self.Print_DepthFirstHelper("   ")
        return True

    def Print_DepthFirstHelper(self, prefix):
        print(prefix+str(self.store[0]))
        for i in self.store[1]:
            i.Print_DepthFirstHelper(prefix+"   ")
        return True

    def Get_LevelOrder(self):
        lista=[]
        x=Queue()
        x.enqueue(self.store)
        while True:
                y=x.dequeue()
                if y[0]!=True:
                    break
                else:
                    lista=lista+[y[1]]
                    for element in y[1][1]:
                        x.enqueue(element.store)
        return lista

