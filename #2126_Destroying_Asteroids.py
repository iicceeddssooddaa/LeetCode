class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        n = len(asteroids)
        for i in range(n):
            if mass >= asteroids[i]: mass += asteroids[i]
            else: return False
        return True
