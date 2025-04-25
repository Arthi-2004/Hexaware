# Payment.py
class Payment:
    def __init__(self, paymentID=None, courierID=None, amount=None, paymentDate=None):
        self.__paymentID = paymentID
        self.__courierID = courierID
        self.__amount = amount
        self.__paymentDate = paymentDate

    # Getters
    def get_paymentID(self):
        return self.__paymentID

    def get_courierID(self):
        return self.__courierID

    def get_amount(self):
        return self.__amount

    def get_paymentDate(self):
        return self.__paymentDate

    # Setters
    def set_paymentID(self, paymentID):
        self.__paymentID = paymentID

    def set_courierID(self, courierID):
        self.__courierID = courierID

    def set_amount(self, amount):
        self.__amount = amount

    def set_paymentDate(self, paymentDate):
        self.__paymentDate = paymentDate

    # toString()
    def __str__(self):
        return f"Payment[paymentID={self.__paymentID}, courierID={self.__courierID}, amount={self.__amount}, paymentDate={self.__paymentDate}]"
