class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        """
        :type currentState: str
        :rtype: List[str]
        """
        if len(currentState) < 2:
            return []
        sign_list = []
        sign_list[:] = currentState
        result_list = []
        i = 0
        while i < len(currentState) - 1:
            if currentState[i:i + 2] == "++":
                sign_list[i:i + 2] = ["-", "-"]
                result_list.append("".join(sign_list))
                sign_list[i:i + 2] = ["+", "+"]
            i += 1
        return result_list
