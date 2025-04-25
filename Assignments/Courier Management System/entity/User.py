class User:
    def __init__(self, userID=None, userName=None, email=None, password=None, contactNumber=None, address=None):
        self.__userID = userID
        self.__userName = userName
        self.__email = email
        self.__password = password
        self.__contactNumber = contactNumber
        self.__address = address

    # Getters
    def get_userID(self):
        return self.__userID

    def get_userName(self):
        return self.__userName

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_contactNumber(self):
        return self.__contactNumber

    def get_address(self):
        return self.__address

    # Setters
    def set_userID(self, userID):
        self.__userID = userID

    def set_userName(self, userName):
        self.__userName = userName

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_contactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def set_address(self, address):
        self.__address = address

    # toString()
    def __str__(self):
        return f"User[userID={self.__userID}, userName={self.__userName}, email={self.__email}, contactNumber={self.__contactNumber}, address={self.__address}]"

