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
----------------------
# 想复杂了。用check swap改。多一步判断如果不对换是否有重复字母即可（重复说明可在内部交换）
class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # 预判断长度。对不同位记录分别记录两个字符。检查字典长度为0或2，为2追加判断字符对调。
        n, _dict, counter = len(s), {}, collections.Counter(s)
        if len(goal) != n: return False
        for i in range(n): 
            if s[i] != goal[i]: _dict[i] = [s[i], goal[i]]
        if len(_dict) == 0 and len(counter) < n: return True
        elif len(_dict) !=2: return False
        else:
            cache = []
            for key, value in _dict.items(): cache.append(value)
            return cache[0][0] == cache[1][1] and cache[0][1] == cache[1][0]
