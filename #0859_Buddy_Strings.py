class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # 长度不同直接报错
        if len(s) != len(goal): return False
        # 出现频率不同也有问题。用位置字典一并解决
        pos_s, pos_goal = {}, {}
        for i in range(len(s)):
            if s[i] not in pos_s: 
                pos_s[s[i]] = set()
                pos_s[s[i]].add(i)
            else: pos_s[s[i]].add(i)
            if goal[i] not in pos_goal: 
                pos_goal[goal[i]] = set()
                pos_goal[goal[i]].add(i)
            else: pos_goal[goal[i]].add(i)
        
        # print pos_s, pos_goal
        # 不同字母交换，则必然遍历goal会出现两处不同
        # 同字母交换，判断是否存在一个字母出现两次即可
        diff, exist = 0, False
        for key, value in pos_s.items():
            if key not in pos_goal: return False
            # 出现的次数不同报错
            if len(pos_s[key]) != len(pos_goal[key]): return False
            # 出现多次记录
            if not exist and len(pos_s[key]) > 1: exist = True
            # 判断位置差异数量
            cache = pos_s[key] ^ pos_goal[key]
            if len(cache) > 2: return False
            if len(cache) == 2: diff += 1
        return (diff == 2) or (diff == 0 and exist) 
