class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.sto = [small, big, medium]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if bool(self.sto[carType%3]):
            self.sto[carType%3] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
