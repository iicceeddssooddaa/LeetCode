class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            cache = [1] * 9
            for j in range(9):
                if board[i][j] != ".": 
                    cache[int(board[i][j]) - 1] -= 1
                    if cache[int(board[i][j]) - 1] < 0: return False
        for i in range(9):
            cache = [1] * 9
            for j in range(9):
                if board[j][i] != ".": 
                    cache[int(board[j][i]) - 1] -= 1
                    if cache[int(board[j][i]) - 1] < 0: return False
        check_set = [[0,1,2],[3,4,5],[6,7,8]]
        for index1 in check_set:
            for index2 in check_set:
                print index1, index2
                cache = cache = [1] * 9
                for i in index1:
                    for j in index2:
                        if board[i][j] != ".":
                            cache[int(board[i][j]) - 1] -= 1
                            if cache[int(board[i][j]) - 1] < 0: return False
        return True
