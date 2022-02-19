"""
You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. 
In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

Return the total number of good triplets.


Example 1
Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
Output: 1
Explanation: 
There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.

Example 2
Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
Output: 4
Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).
"""
-------------
class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        pos1, pos2, n, record = {}, {}, len(nums1), []
        for i in range(n): record.append([0,0])
        for i in range(n):
            pos1[nums1[i]] = i
            pos2[nums2[i]] = i
        for i in range(n - 1):
            for j in range(i + 1, n):
                if pos1[i] < pos1[j] and pos2[i] < pos2[j]: 
                    record[i][0] += 1
                    record[j][1] += 1
                elif pos1[i] > pos1[j] and pos2[i] > pos2[j]: 
                    record[i][1] += 1
                    record[j][0] += 1
        count = sum(record[i][0] * record[i][1] for i in range(n))
        return count
# 超时
----------
  class Solution(object):
    def goodTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        pos1, pos2, n, record, count = {}, {}, len(nums1), {}, 0
        for i in range(n):
            pos1[nums1[i]] = i
            pos2[nums2[i]] = i
        for i in range(n - 1):
            for j in range(i + 1, n):
                if pos1[i] < pos1[j] and pos2[i] < pos2[j]: 
                    if i not in record: record[i] = [1,0]
                    else: 
                        if j not in record: record[j] = [0,1]
                        else: 
                            record[i][0] += 1
                            record[j][1] += 1
                elif pos1[i] > pos1[j] and pos2[i] > pos2[j]:
                    if i not in record: record[i] = [0,1]
                    else:
                        if j not in record: record[j] = [1,0]
                        else:
                            record[i][1] += 1
                            record[j][0] += 1
        print record
        for key, value in record.items():
            count += value[0] * value[1]
        return count
#       有错
