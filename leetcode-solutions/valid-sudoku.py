class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        trans = list(zip(*board))
        arein = defaultdict(list)
        # print(arein)
        
        _1st = '_1st'
        _2nd = '_2nd'
        _3rd = '_3rd'
        _4th = '_4th'
        _5th = '_5th'
        _6th = '_6th'
        _7th = '_7th'
        _8th = '_8th'
        _9th = '_9th'


        for row in range(9):
            for col in range(9):
               
                if board[row][col] != '.' and (board[row][col] in board[row][col + 1:] or board[row][col] in board[row][:col]):
                    return False
                

               
                if trans[row][col] != '.' and (trans[row][col] in trans[row][col + 1:] or trans[row][col] in trans[row][:col]):
                    return False

                if board[row][col] != '.':
                    if 0 <= row <= 2:
                        
                        if 0 <= col <= 2:
                            if board[row][col] in arein[_1st]:
                                return False
                            arein[_1st].append(board[row][col])
                        
                        elif 3 <= col <= 5:
                            if board[row][col] in arein[_2nd]:
                                return False
                            arein[_2nd].append(board[row][col])
                        
                        else:
                            if board[row][col] in arein[_3rd]:
                                return False
                            arein[_3rd].append(board[row][col])
                    


                    elif 3 <= row <= 5:
                        
                        if 0 <= col <= 2:
                            if board[row][col] in arein[_4th]:
                                return False
                            arein[_4th].append(board[row][col])
                        
                        elif 3 <= col <= 5:
                            if board[row][col] in arein[_5th]:
                                return False
                            arein[_5th].append(board[row][col])
                        
                        else:
                            if board[row][col] in arein[_6th]:
                                return False
                            arein[_6th].append(board[row][col])
                    


                    else:
                        
                        if 0 <= col <= 2:
                            if board[row][col] in arein[_7th]:
                                return False
                            arein[_7th].append(board[row][col])
                        
                        elif 3 <= col <= 5:
                            if board[row][col] in arein[_8th]:
                                return False
                            arein[_8th].append(board[row][col])
                        
                        else:
                            if board[row][col] in arein[_9th]:
                                return False
                            arein[_9th].append(board[row][col])
                    


                


        return True
        