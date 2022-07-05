class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        m, n, sto, result = len(mat), len(mat[0]), [], []
        for i in range(m):
            left, right = 0, n-1
            while left < right:
                if not mat[i][left]: right = 0
                elif mat[i][right]: left = right + 1
                else:
                    mid = (left + right)//2
                    if mat[i][mid] > mat[i][mid + 1]: left, right = mid+1, mid+1
                    elif mat[i][mid]: left = mid + 1
                    else: right = mid
            sto.append([left,i])
        sto.sort()
        for i in range(k):
            result.append(sto[i][1])
        return result
