class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack, i = [], 0
        while i < len(asteroids):
            if asteroids[i] > 0: 
                stack.append(asteroids[i])
                i += 1
            non_stop = True
            while i < len(asteroids) and asteroids[i] < 0 and non_stop:
                if len(stack) == 0: 
                    stack.append(asteroids[i])
                    i += 1
                    non_stop = False
                elif stack[-1] + asteroids[i] == 0: 
                    i += 1
                    stack.pop()
                    non_stop = False
                elif stack[-1] + asteroids[i] > 0: 
                    i += 1
                    non_stop = False
                elif stack[-1] > 0 and stack[-1] + asteroids[i] < 0:
                    stack.pop()
                elif stack[-1] < 0: 
                    stack.append(asteroids[i])
                    i += 1
                    non_stop = False
        return stack
