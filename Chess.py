from LegalMoves import *
from Board import *
from Tree import *

def GetPlayerPositions(board1,player):
        accum = []
        if (player == 10):
            for i in range(0,64):
                if ((board1[i]>=10) and (board1[i]<=15)):
                    accum += [i]
        elif (player == 20):
            for i in range(0,64):
                if ((board1[i]>=20) and (board1[i]<=25)):
                    accum += [i]
        else:
            return []
        return accum

def GetPieceLegalMoves(board2,position):
    index = board2[position]
    if (index == 0):
            return []
    elif (index == 10) or (index == 20):
        return GetPawnLegalMoves(board2,position,index)
    elif (index == 11) or (index == 21):
        return GetKnightLegalMoves(board2,position,index)
    elif (index == 12) or (index == 22):
        return GetBishopLegalMoves(board2,position,index)
    elif (index == 13) or (index == 23):
        return GetRookLegalMoves(board2,position,index)
    elif (index == 14) or (index == 24):
        return GetQueenLegalMoves(board2,position,index)
    elif (index == 15) or (index == 25):
        return GetKingLegalMoves(board2,position,index)
    else:
        return []

def IsPositionUnderThreat(board9,position,player):
    if (player == 10):
        enemy_pieces = GetPlayerPositions(board9,20)
        for i in enemy_pieces:
            enemy_LM = GetPieceLegalMoves(board9,i)
            for q in enemy_LM:
                if (q == position):
                    return True
        return False
    elif (player == 20):
        enemy_pieces = GetPlayerPositions(board9, 10)
        for i in enemy_pieces:
            enemy_LM = GetPieceLegalMoves(board9, i)
            for q in enemy_LM:
                if (q == position):
                    return True
        return False

def Num_Threats(board10,position,player):
    accum = 0
    if (player == 10):
        enemy_pieces = GetPlayerPositions(board10,20)
        for i in enemy_pieces:
            enemy_LM = GetPieceLegalMoves(board10,i)
            for q in enemy_LM:
                if (q == position):
                    accum += 1
        return accum
    elif (player == 20):
        enemy_pieces = GetPlayerPositions(board10, 10)
        for i in enemy_pieces:
            enemy_LM = GetPieceLegalMoves(board10, i)
            for q in enemy_LM:
                if (q == position):
                    accum += 1
        return accum

def evalBoard(board11,player):
    #helper functions: evalPieces(board,player),evalMobility(board,player),evalThreats,evalCentreControl
    Score_Pieces = 0.6 * evalPieces(board11,player)
    Score_Mobility = 0.15 * evalMobility(board11,player)
    Score_Threats = 0.2 * evalThreats(board11,player)
    Score_CentreControl = 0.05 * evalCentreControl(board11,player)
    sum_Score = float(Score_Pieces + Score_Mobility + Score_Threats + Score_CentreControl)
    return sum_Score

def evalPieces(board12,player):
    Pawn = 1
    Knight = 3.25
    Bishop = 3.25
    Rook = 5
    Queen = 9.75
    King = 100
    Piece = []
    val = 0
    Piece_pos = GetPlayerPositions(board12,player)
    range = len(Piece_pos)
    #End game considerations
    if (range <= 5):
        Bishop = 4.25
        Rook = 6
    for i in Piece_pos:
        Piece += [board12[i]]

    for i in Piece:
        if (i == 10) or (i == 20):
            val += Pawn
        elif (i == 11) or (i == 21):
            val += Knight
        elif (i == 12) or (i == 22):
            val += Bishop
        elif (i == 13) or (i ==23):
            val += Rook
        elif (i == 14) or (i == 24):
            val += Queen
        elif (i == 15) or (i == 25):
            val += King
    return val

def evalMobility(board13,player):
    Piece_pos = GetPlayerPositions(board13, player)
    if (player == 10):
        enemy = 20
    else:
        enemy = 10
    enemy_pos = GetPlayerPositions(board13,enemy)
    num_LegalMoves = 0
    enemy_LM = 0
    for i in Piece_pos:
        LM = GetPieceLegalMoves(board13,i)
        num_LegalMoves += len(LM)
    for q in enemy_pos:
        LM = GetPieceLegalMoves(board13,q)
        enemy_LM += len(LM)

    if ((num_LegalMoves - enemy_LM) < -20):
        score = -5
    elif ((num_LegalMoves - enemy_LM) >= -20) and ((num_LegalMoves - enemy_LM) < -15):
        score = -4
    elif ((num_LegalMoves - enemy_LM) >= -15) and ((num_LegalMoves - enemy_LM) < -10):
        score = -3
    elif ((num_LegalMoves - enemy_LM) >= -10) and ((num_LegalMoves - enemy_LM) < -5):
        score = -2
    elif ((num_LegalMoves - enemy_LM) >= -5) and ((num_LegalMoves - enemy_LM) < 0):
        score = -1
    elif ((num_LegalMoves - enemy_LM) == 0):
        score = 0
    elif ((num_LegalMoves - enemy_LM) > 0) and ((num_LegalMoves - enemy_LM) < 5):
        score = 1
    elif ((num_LegalMoves - enemy_LM) >= 5) and ((num_LegalMoves - enemy_LM) < 10):
        score = 2
    elif ((num_LegalMoves - enemy_LM) >= 10) and ((num_LegalMoves - enemy_LM) < 15):
        score = 3
    elif ((num_LegalMoves - enemy_LM) >= 15) and ((num_LegalMoves - enemy_LM) < 20):
        score = 4
    elif ((num_LegalMoves - enemy_LM) >= 20):
        score = 5
    return score

def evalThreats(board14,player):
    Piece_pos = GetPlayerPositions(board14, player)
    accum1 = 0
    accum2 = 0
    if (player == 10):
        enemy = 20
    else:
        enemy = 10
    enemy_pos = GetPlayerPositions(board14, enemy)
    for i in Piece_pos:
        accum1 += Num_Threats(board14,i,player)
    for q in enemy_pos:
        accum2 += Num_Threats(board14,q,enemy)
    if ((accum1 - accum2) < -5):
        score = -5
    elif ((accum1 - accum2) >= -5) and ((accum1 - accum2) < -3):
        score = -3
    elif ((accum1 - accum2) >= -3) and ((accum1 - accum2) < 0):
        score = -1
    elif ((accum1 - accum2) == 0):
        score = 0
    elif ((accum1 - accum2) > 0) and ((accum1 - accum2) < 3):
        score = 1
    elif ((accum1 - accum2) >= 3) and ((accum1 - accum2) < 5):
        score = 3
    elif ((accum1 - accum2) > 5):
        score = 5
    return score

def evalCentreControl(board15,player):
    Piece_pos = GetPlayerPositions(board15, player)
    accum = 0
    for i in Piece_pos:
        if (i >= 24) and (i <= 39):
            accum += 1
    if (accum == 0):
        score = 0
    elif (accum > 0) and (accum < 3):
        score = 0.5
    elif (accum >= 3) and (accum < 5):
        score = 1
    elif (accum >= 5) and (accum < 8):
        score = 1.5
    elif (accum == 8):
        score = 2
    elif (accum > 8):
        score = 3
    return score


def CandidateMoves(board16,player):
    Moves = []
    Candidate_moves = []
    Piece_pos = GetPlayerPositions(board16, player)
    for i in Piece_pos:
        LM = GetPieceLegalMoves(board16,i)
        for q in LM:
            if not (IsPositionUnderThreat(board16,q,player)):
                Moves += [q]
        Candidate_moves += [[i,Moves]]
        Moves = []
    return Candidate_moves

#piece_move is a 2-element list, first element is the position on the board of a piece being moved
#second element is te position on the board that the piece is being moved to
def get_Score(board17,piece_move,player):
    return evalBoard(genNewBoard(board17,piece_move,player),player)


def genNewBoard(board18,piece_move,player):
    tempBoard = []
    for i in board18:
        tempBoard += [i]
    old_piece = tempBoard[piece_move[0]]
    tempBoard[piece_move[0]] = 0
    tempBoard[piece_move[1]] = old_piece
    return tempBoard

def genTree(tempboard):
    return Tree(tempboard)

def AddToTree(board19,Candidate,player):
    temp = []
    if (player == 10):
        enemy = 20
    else:
        enemy = 10
    for i in board19:
        temp += [i]
    evalTree = Tree(temp)
    for i in Candidate:
        for q in i[1]:
            tempboard = genNewBoard(temp,[i[0],q],player)
            tempTree = genTree(tempboard)
            tempCandidate = CandidateMoves(tempboard,enemy)
            for a in tempCandidate:
                for b in a[1]:
                    temp2 = genNewBoard(tempboard,[a[0],b],enemy)
                    temp2Tree = genTree(temp2)
                    Candidate2 = CandidateMoves(temp2,player)
                    for c in Candidate2:
                        for d in c[1]:
                            temp3 = genNewBoard(temp2,[c[0],d],player)
                            temp3Tree = genTree(temp3)
                            temp2Tree.AddSuccessor(temp3Tree)
                    tempTree.AddSuccessor(temp2Tree)
            evalTree.AddSuccessor(tempTree)
    return evalTree

def getGameTree(board, player, depth):
    if depth == 0:
        return Tree((None, evalBoard(board, player)))

    if player == 10:
        opp = 20
    else:
        opp = 10
    nodeTree = Tree((None, None)) # move, score of board
    CM = CandidateMoves(board, player)
    for i in CM:
        for q in i[1]:
            move = [i[1], q]
            tempBoard = genNewBoard(board, move, player)
            nodeTree.AddSuccessor(getGameTree(tempBoard, player, depth-1))

def getBestMove(board20,player):
    CM = CandidateMoves(board20,player)
    accum = []
    max = 0
    for i in CM:
        for q in i[1]:
            temp = genNewBoard(board20,[i[0],q],player)
            score = float(evalBoard(temp,player))
            if (max < score):
                max = score
                accum = [i[0],q]
    return accum



def minimax(node,depth,maximizingPlayer,player):
    if (player == 10):
        enemy = 20
    else:
        enemy = 10

    if (depth == 0):
        return evalBoard(node.GetNode(),player)

    if (maximizingPlayer == True):
        bestVal = -1000
        for i in range (0,len(node.store[1])):
            value = minimax(node.store[1][i],depth - 1,False,enemy)
            bestVal = max(bestVal,value)


    elif (maximizingPlayer == False):
        bestVal = 1000
        for q in range (0,len(node.store[1])):
            value = minimax(node.store[1][q],depth - 1,True,enemy)
            bestVal = min(bestVal,value)

    return float(bestVal)

def max(num1,num2):
    if (num1 >= num2):
        return num1
    return num2

def min(num1,num2):
    if (num1 < num2):
        return num1
    return num2

def chessPlayer(board21,player):
    status = False
    tempTr = AddToTree(board21,CandidateMoves(board21,10),10)
    #best_score = minimax(tempTr,3,True,player)
    move = getBestMove(board21,player)
    Candidate_accum = []
    Candidates = CandidateMoves(board21,player)
    for i in Candidates:
        for q in i[1]:
            tempboard = genNewBoard(board21,[i[0],q],player)
            score = float(evalBoard(tempboard,player))
            Candidate_accum += [[[i[0],q],score]]
    if not (len(move) == 0):
        status = True

    return [status,move,Candidate_accum, tempTr.Get_LevelOrder()]


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

