class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        """
        比较方式直接：
        造字典，持续差沿字典序搜索保持同非负或同非正即可。
        """
        #两本字典
        
        counter1 = collections.Counter(s1)
        counter2 = collections.Counter(s2)
        #查询依序
        checklist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        count = counter1[checklist[0]] - counter2[checklist[0]]
        #一次计算，两个指针
        leq = count <= 0
        geq = count >= 0
        i = 1
        while leq and i < len(checklist):
            #顺手边字典
            if checklist[i] not in counter1:
                counter1[checklist[i]] = 0
            if checklist[i] not in counter2:
                counter2[checklist[i]] = 0
            count += counter1[checklist[i]] - counter2[checklist[i]]
            leq = leq and count <= 0
            geq = geq and count >= 0
            i += 1
        #小于失败则继续，不要从头开始。内存和速度都有保持
        while geq and i < len(checklist):
            if checklist[i] not in counter1:
                counter1[checklist[i]] = 0
            if checklist[i] not in counter2:
                counter2[checklist[i]] = 0
            count += counter1[checklist[i]] - counter2[checklist[i]]
            geq = geq and count >= 0
            i += 1
        return leq or geq
        #理论上s1和s2过了一遍，字典序过两个字典，O(n)
