board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
word = "SEE"
word = "ABCB"
def get_cors_around(ind, was):# координаты ячеек в которых еще не были
    directs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    return [[ind[0] + d[0], ind[1] + d[1]] for d in directs 
            if 0 <= ind[0] + d[0] < len(board) and 
            0 <= ind[1] + d[1] < len(board[0]) and 
            [ind[0] + d[0], ind[1] + d[1]] not in was]

def rec(cur_string, ind, was=[]):
    was = was + [ind]
    if not cur_string:
        return True
    if cur_string.startswith(board[ind[0]][ind[1]]):
        return any(rec(cur_string[1:], new_ind, was.copy()) 
                   for new_ind in get_cors_around(ind, was))
    return False
print(any([rec(word, [i, j]) for j in range(len(board[0])) for i in range(len(board))]))