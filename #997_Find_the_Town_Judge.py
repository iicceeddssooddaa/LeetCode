class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1
        # 和城市终点类似，找到唯一（或无）的数字始终存在于后位。首次遇到生成个变量，逐次增加信任者数量
        judge_pot, trusted = {}, {}
        for relation in trust:
            judge_pot[relation[0]] = 1
            if relation[1] not in judge_pot: 
                judge_pot[relation[1]] = -1
                trusted[relation[1]] = 1
            elif judge_pot[relation[1]] == -1: 
                trusted[relation[1]] += 1
        for key, value in judge_pot.items():
            if value == -1 and trusted[key] == n - 1: return key
        return -1
      # 貌似可以把字典和计数合并，暂时脑子不够用了。
-----------
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n == 1:
            return 1
        # 和城市终点类似，找到唯一（或无）的数字始终存在于后位。首次遇到生成个变量，逐次增加信任者数量
        # judge_pot: judge potential
        judge_pot = {}
        for relation in trust:
            judge_pot[relation[0]] = -1
            if relation[1] not in judge_pot: judge_pot[relation[1]] = 1
            elif judge_pot[relation[1]] > 0: judge_pot[relation[1]] += 1 
        for key, value in judge_pot.items():
            if value == n - 1: return key
        return -1
