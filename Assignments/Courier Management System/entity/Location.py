# 4. Location Class
class Location:
    def __init__(self, locationID=None, locationName=None, address=None):
        self.__locationID = locationID
        self.__locationName = locationName
        self.__address = address

    # Getters
    def get_locationID(self):
        return self.__locationID

    def get_locationName(self):
        return self.__locationName

    def get_address(self):
        return self.__address

    # Setters
    def set_locationID(self, locationID):
        self.__locationID = locationID

    def set_locationName(self, locationName):
        self.__locationName = locationName

    def set_address(self, address):
        self.__address = address

    # toString()
    def __str__(self):
        return f"Location[locationID={self.__locationID}, locationName={self.__locationName}, address={self.__address}]"


