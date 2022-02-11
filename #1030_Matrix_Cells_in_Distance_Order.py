class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        # 初始化，找寻最大距离（终止范围）
        dist00, dist01, dist10, dist11 = rCenter + cCenter, rCenter + cols - 1 - cCenter, rows - 1 - rCenter + cCenter, rows - rCenter - 2 + cols - cCenter
        max_dist = max(dist00, dist01, dist10, dist11)
        dist, pt_list = 1, [[rCenter,cCenter]]
        # 循环，针对每个特定距离把周边搜索一遍
        while dist <= max_dist:
            # 左端点
            i= rCenter - dist
            if 0 <= i < rows: pt_list.append([i,cCenter])
            i += 1
            # 上下同时进行
            while i <= rCenter:
                j1, j2 = rCenter - i + cCenter - dist, dist + i - rCenter + cCenter
                if 0 <= i < rows and 0 <= j1 < cols: pt_list.append([i,j1])
                if 0 <= i < rows and 0 <= j2 < cols: pt_list.append([i,j2])
                i += 1
            while i < rCenter + dist:
                j1, j2 = i - rCenter + cCenter - dist, dist + rCenter - i + cCenter
                if 0 <= i < rows and 0 <= j1 < cols: pt_list.append([i,j1])
                if 0 <= i < rows and 0 <= j2 < cols: pt_list.append([i,j2])
                i += 1
            # 右端点（需要规避识别为左端点）
            if 0 <= i < rows and i!=rCenter - dist: pt_list.append([i,cCenter])
            dist += 1
        return pt_list
