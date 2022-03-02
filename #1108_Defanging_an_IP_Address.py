class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        cache = address.split(".")
        string = "[.]".join(cache)
        return string
