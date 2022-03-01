class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        _dict, count = {"type":0, "color":1, "name":2}, 0
        key = _dict[ruleKey]
        for item in items: count += item[key] == ruleValue
        return count
