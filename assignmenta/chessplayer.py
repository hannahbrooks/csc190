from chessplayer_main import *
import sys

def main():
    whitePlayerScore = 0
    blackPlayerScore = 0

    print("Welcome! You are playing chess, you control the white pieces")
    board = genBoard()
    print (printBoard(board))
    print("remember indexes are as follows")
    print (printNumbers())
    player = "white"
    
    for i in range(0,2):
        if player == "white":
            startpos=int(input("where would you like to move from?"))-1
            if player == "white" and board[startpos] >= 20:
                continue 
            elif startpos > 64:
                print("invalid move!\n")
                continue

            legalMoves = board
            print(legalMoves[startpos])

            print(board[startpos])

            endpos=int(input("where would you like to move to?"))-1

            legalmoves = []
            legalMoves+=GetPieceLegalMoves(board, startpos)

            if legalMoves[endpos] == 0:
                continue
            else:
                if player == "white":
                    if legalMoves[endpos] == 1 or legalMoves[endpos] == 2:
                        if legalMoves[endpos] == 2:
                            whitePlayerScore+=piecescore(board[endpos])                
                        board[endpos] = board[startpos]
                        board[startpos] = 0
                    else:
                        print("invalid move!\n")
                        continue
            
        if player == "black":
            EvalTree(board)            
        if player == "white":
            player = "white"
        else:
            player = "white"

        print (printBoard(board))
        print("remember indexes are as follows")
        print (printNumbers())
        player = "white"

main()

