class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        sto, n = [float('-inf')]*9, len(moves)
        for i in range(n):
            cache = moves[i][0] * 3 + moves[i][1]
            sto[cache] = i%2
        checklist = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for check in checklist:
            i,j,k = check[0], check[1], check[2]
            if sto[i] + sto[j] + sto[k] >= 0:
                if sto[i] == sto[j] and sto[j] == sto[k] : return 'B' if sto[i] else 'A'
        return 'Draw' if n == 9 else 'Pending'
