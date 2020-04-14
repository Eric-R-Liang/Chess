from Board import *
from Chess import *
from LegalMoves import *

def main():
  n = 0
  player = 10
  enemy = 20
  board = genBoard()
  print ("raw board is: (index=0 ... index=63):")
  print (board)
  print (" \nwhich will look like the following:")
  print (printBoard(genBoard()))
  print ("")
  print (" Note 1: lower right hand square is WHITE")
  print (" Note 2: two upper rows are for BLACK PIECES")
  print (" Note 3: two lower rows are for WHITE PIECES")

  while (n <= 20):
      pos1 = int(input ("Enter a position of the piece that you want to move:"))
      pos2 = int(input ("Enter a position that you wish to move to"))
      P_move = [pos1,pos2]
      print(P_move)
      board = genNewBoard(board,P_move,player)
      print(printBoard(board))
      lol = chessPlayer(board,enemy)
      board = genNewBoard(board,[lol[1][0],lol[1][1]],player)
      print(printBoard(board))
      n += 1
      
 main()

