# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1, poly2):
        """
        :type poly1: PolyNode
        :type poly2: PolyNode
        :rtype: PolyNode
        """
        #最极端，一个为空，返回另一个
        if poly1 == None:
            return poly2
        if poly2 == None:
            return poly1
        
        #初始化，头部直接无穷次幂，最后删除
        cur1, cur2 = poly1, poly2
        head = PolyNode("inf", 1, None)
        tail = head
        #主体循环
        while cur1 and cur2:
            while cur1 and cur2 and cur1.power > cur2.power:
                tail.next = cur1
                tail = cur1
                cur1 = cur1.next
            while cur1 and cur2 and cur2.power > cur1.power:
                tail.next = cur2
                tail = cur2
                cur2 = cur2.next
            if cur1 and cur2 and (cur1.coefficient + cur2.coefficient != 0):
                node = PolyNode(cur1.coefficient + cur2.coefficient, cur1.power, None)
                tail.next = node
                tail = node
                cur1 = cur1.next
                cur2 = cur2.next
            elif cur1 and cur2 and (cur1.coefficient + cur2.coefficient == 0):
                cur1 = cur1.next
                cur2 = cur2.next
                if tail.next != None:
                    tail = tail.next #如果tail已经到底，tail.next就没东西了
        #如果剩下，直接并入
        if cur1:
            tail.next = cur1
        if cur2:
            tail.next = cur2
        #去头
        head = head.next
        return head
      
--------------
# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1, poly2):
        """
        :type poly1: PolyNode
        :type poly2: PolyNode
        :rtype: PolyNode
        """
        #最极端，一个为空，返回另一个
        if poly1 == None:
            return poly2
        if poly2 == None:
            return poly1
        
        #初始化，头部直接无穷次幂，最后删除
        cur1, cur2 = poly1, poly2
        head = PolyNode("inf", 1, None)
        tail = head
        #主体循环
        while cur1 and cur2:
            while cur1 and cur2 and cur1.power > cur2.power:
                tail.next = cur1
                tail = cur1
                cur1 = cur1.next
            while cur1 and cur2 and cur2.power > cur1.power:
                tail.next = cur2
                tail = cur2
                cur2 = cur2.next
            while cur1 and cur2 and cur1.power == cur2.power:
                node = PolyNode(cur1.coefficient + cur2.coefficient, cur1.power, None)
                tail.next = node
                tail = node
                cur1 = cur1.next
                cur2 = cur2.next
        #如果剩下，直接并入
        if cur1:
            tail.next = cur1
        if cur2:
            tail.next = cur2
        #去头
        head = head.next
        cur = head
        #中间去不掉0，最后处理
        while cur:
            tmp = cur.next
            if tmp and tmp.coefficient == 0:
                cur.next = tmp.next
                del tmp
            cur = cur.next
        if cur.coefficient == 0:
            
        return head
            
            
