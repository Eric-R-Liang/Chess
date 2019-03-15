def GetPawnLegalMoves(board3,position,index):
    LM = []
    if (position >= 8) and (position <= 55):
        if (index == 10):
            if (board3[position+8] == 0):
                LM += [position+8]
            if (position%8 == 7) and (board3[position+7] >= 20):
                LM += [position+7]
            if (position%8 == 0) and (board3[position+9] >= 20):
                LM += [position+9]
            if (position%8 >= 1) and (position%8 <= 6):
                if (board3[position+7] >= 20):
                    LM += [position+7]
                if (board3[position+9] >= 20):
                    LM += [position+9]
        elif (index == 20):
            if (board3[position-8] == 0):
                LM += [position-8]
            if (position%8 == 7) and (board3[position-9] >= 10):
                LM += [position-9]
            if (position%8 == 0) and (board3[position-7] >= 10):
                LM += [position-7]
            if (position%8 >= 1) and (position%8 <= 6):
                if (board3[position-7] >= 10):
                    LM += [position-7]
                if (board3[position-9] >= 10):
                    LM += [position-9]
    return LM

def GetKnightLegalMoves(board4,position,index):
    LM = []
    x_comp = position//8
    y_comp = position%8
    trans = [[-2,-1],[-2,1],[2,-1],[2,1],[-1,-2],[-1,2],[1,-2],[1,2]]
    for i in trans:
        x_Candidate = x_comp + i[0]
        y_Candidate = y_comp + i[1]
        enemy_pos = x_Candidate * 8 + y_Candidate
        if (x_Candidate >= 0) and (x_Candidate <= 7) and (y_Candidate >= 0) and (y_Candidate <= 7):
            if (board4[enemy_pos] == 0):
                LM += [enemy_pos]
            if (index == 10):
                if (board4[enemy_pos] >= 20) and (board4[enemy_pos] <= 25):
                    LM += [enemy_pos]
            elif (index == 20):
                if (board4[enemy_pos] >= 10) and (board4[enemy_pos] <= 15):
                    LM += [enemy_pos]
    return LM

def GetBishopLegalMoves(board5,position,index):
    LM = []
    x_comp = position // 8
    y_comp = position % 8
    factor = 1
    trans = [[1,-1],[1,1],[-1,1],[-1,-1]]
    for i in trans:
        while True:
            x_Candidate = x_comp + factor * i[0]
            y_Candidate = y_comp + factor * i[1]
            enemy_pos = x_Candidate * 8 + y_Candidate
            if (x_Candidate >= 0) and (x_Candidate <= 7) and (y_Candidate >= 0) and (y_Candidate <= 7):
                if (board5[enemy_pos] == 0):
                    LM += [enemy_pos]
                if (index == 10):
                    if (board5[enemy_pos] >= 20) and (board5[enemy_pos] <= 25):
                        LM += [enemy_pos]
                elif (index == 20):
                    if (board5[enemy_pos] >= 10) and (board5[enemy_pos] <= 15):
                        LM += [enemy_pos]
            else:
                break
            if (board5[enemy_pos] != 0):
                break
            factor += 1
        factor = 1
    return LM

def GetRookLegalMoves(board6,position,index):
    LM = []
    factor = 1
    x_comp = position // 8
    y_comp = position % 8
    trans = [[1,0],[-1,0],[0,1],[0,-1]]
    for i in trans:
        while True:
            x_Candidate = x_comp + factor * i[0]
            y_Candidate = y_comp + factor * i[1]
            enemy_pos = x_Candidate * 8 + y_Candidate
            if (x_Candidate >= 0) and (x_Candidate <= 7) and (y_Candidate >= 0) and (y_Candidate <= 7):
                if (board6[enemy_pos] == 0):
                    LM += [enemy_pos]
                if (index == 10):
                    if (board6[enemy_pos] >= 20) and (board6[enemy_pos] <= 25):
                        LM += [enemy_pos]
                elif (index == 20):
                    if (board6[enemy_pos] >= 10) and (board6[enemy_pos] <= 15):
                        LM += [enemy_pos]
            else:
                break
            if (board6[enemy_pos] != 0):
                break
            factor += 1
        factor = 1
    return LM

def GetQueenLegalMoves(board7,position,index):
    return GetBishopLegalMoves(board7,position,index) + GetRookLegalMoves(board7,position,index)

def GetKingLegalMoves(board8,position,index):
    LM = []
    x_comp = position // 8
    y_comp = position % 8
    trans = [[1, -1], [1, 1], [-1, 1], [-1, -1],[1,0],[-1,0],[0,1],[0,-1]]
    for i in trans:
        x_Candidate = x_comp + i[0]
        y_Candidate = y_comp + i[1]
        enemy_pos = x_Candidate * 8 + y_Candidate
        if (x_Candidate >= 0) and (x_Candidate <= 7) and (y_Candidate >= 0) and (y_Candidate <= 7):
            if (board8[enemy_pos] == 0):
                LM += [enemy_pos]
            if (index == 10):
                if (board8[enemy_pos] >= 20) and (board8[enemy_pos] <= 25):
                    LM += [enemy_pos]
            elif (index == 20):
                if (board8[enemy_pos] >= 10) and (board8[enemy_pos] <= 15):
                    LM += [enemy_pos]
    return LM



#board = []
#for i in range (0,64):
#    board += [0]
#board[24] = 15
#print(GetKingLegalMoves(board,24,15))
