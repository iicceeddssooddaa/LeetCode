class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt, max_alt = 0, 0
        for disc in gain:
            alt += disc
            max_alt = max(alt, max_alt)
        return max_alt
      # 或许遇到下降的可以不跑max部分
-----
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt, max_alt = 0, 0
        for disc in gain:
            alt += disc
            if disc >= 0:
                max_alt = max(alt, max_alt)
        return max_alt
    # 瞬间提速，节省空间
