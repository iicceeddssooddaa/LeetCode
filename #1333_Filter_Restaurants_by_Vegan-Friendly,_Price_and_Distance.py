class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        sto = []
        for restaurant in restaurants:
            if (not veganFriendly or restaurant[2]) and restaurant[3] <= maxPrice and restaurant[4] <= maxDistance: sto.append(restaurant)
        sto.sort(key = lambda x: (x[1], x[0]), reverse = True)
        result = [restaurant[0] for restaurant in sto]
        return result
