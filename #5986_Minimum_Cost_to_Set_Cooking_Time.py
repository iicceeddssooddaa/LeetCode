class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        if targetSeconds < 60:
            sto = []
            while targetSeconds > 0:
                sto.insert(0,targetSeconds%10)
                targetSeconds //= 10
            cost = 0
            t = len(sto)
            sto.insert(0,startAt)
            for i in range(t):
                if sto[i] != sto[i + 1]: cost += moveCost
                cost += pushCost
            return cost
        
        #two possible combinations
        minute1, second1 = targetSeconds // 60, targetSeconds %60
        minute2, second2 = minute1 - 1, second1 + 60
        allow = (second2 <= 99)
        
        cost1 = 0
        sto11 = []
        while minute1 > 0:
            sto11.insert(0,minute1%10)
            minute1 //= 10

        t11 = len(sto11)
        sto11.insert(0,startAt)
        sto12 = []
        while second1 > 0:
            sto12.insert(0,second1%10)
            second1 //= 10
        while len(sto11) > 0 and len(sto12) < 2:
            sto12.insert(0,0)
        t12 = len(sto12)
        sto12.insert(0,sto11[-1])
        
        for i in range(t11):
            if sto11[i] != sto11[i + 1]: cost1 += moveCost
            cost1 += pushCost
        for i in range(t12):
            if sto12[i] != sto12[i + 1]: cost1 += moveCost
            cost1 += pushCost
        
        if not allow: 
            return cost1
        
        cost2 = 0
        sto21 = []
        while minute2 > 0:
            sto21.insert(0,minute2%10)
            minute2 //= 10

        t21 = len(sto21)
        sto21.insert(0,startAt)
        sto22 = []
        while second2 > 0:
            sto22.insert(0,second2%10)
            second2 //= 10
        while len(sto21) > 0 and len(sto22) < 2:
            sto22.insert(0,0)
        t22 = len(sto22)
        sto22.insert(0,sto21[-1])
        
        for i in range(t21):
            if sto21[i] != sto21[i + 1]: cost2 += moveCost
            cost2 += pushCost
        for i in range(t12):
            if sto22[i] != sto22[i + 1]: cost2 += moveCost
            cost2 += pushCost
        
        return min(cost1, cost2)
        
