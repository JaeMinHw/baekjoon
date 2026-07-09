def solution(board):
    answer = 0
    cp_board = board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1 :
                if j-1>=0 :
                    cp_board[i][j-1] = 1
                if j-1>=0 and i-1 >= 0:
                    cp_board[i-1][j-1] = 1
                if i+1 <= len(board) and j-1 >=0 :
                    cp_board[i+1][j-1] = 1
                if i-1 >= 0:
                    cp_board[i-1][j] = 1
                if i+1 <= len(board):
                    cp_board[i+1][j] = 1
                if j+1 <= len(board):
                    cp_board[i][j+1] = 1
                if i+1 <= len(board) and j+1 <= len(board) :
                    cp_board[i+1][j+1] = 1
                if i-1 >= 0 and j+1 <= len(board):
                    cp_board[i-1][j+1] = 1
                
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0 :
                answer += 1
                
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))