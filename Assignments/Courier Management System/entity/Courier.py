# Courier.py
class Courier:
    tracking_number_counter = 1000  # Static variable to generate unique tracking numbers

    def __init__(self, senderName=None, senderAddress=None, receiverName=None,
                 receiverAddress=None, weight=None, status=None, userId=None, deliveryDate=None):
        self.__courierID = None
        self.__senderName = senderName
        self.__senderAddress = senderAddress
        self.__receiverName = receiverName
        self.__receiverAddress = receiverAddress
        self.__weight = weight
        self.__status = status
        self.__trackingNumber = Courier.tracking_number_counter
        self.__deliveryDate = deliveryDate
        self.__userId = userId
        Courier.tracking_number_counter += 1  # Increment for next courier

    # Getters
    def get_courierID(self):
        return self.__courierID

    def get_senderName(self):
        return self.__senderName

    def get_senderAddress(self):
        return self.__senderAddress

    def get_receiverName(self):
        return self.__receiverName

    def get_receiverAddress(self):
        return self.__receiverAddress

    def get_weight(self):
        return self.__weight

    def get_status(self):
        return self.__status

    def get_trackingNumber(self):
        return self.__trackingNumber

    def get_deliveryDate(self):
        return self.__deliveryDate

    def get_userId(self):
        return self.__userId

    # Setters
    def set_courierID(self, courierID):
        self.__courierID = courierID

    def set_senderName(self, senderName):
        self.__senderName = senderName

    def set_senderAddress(self, senderAddress):
        self.__senderAddress = senderAddress

    def set_receiverName(self, receiverName):
        self.__receiverName = receiverName

    def set_receiverAddress(self, receiverAddress):
        self.__receiverAddress = receiverAddress

    def set_weight(self, weight):
        self.__weight = weight

    def set_status(self, status):
        self.__status = status

    def set_trackingNumber(self, trackingNumber):
        self.__trackingNumber = trackingNumber

    def set_deliveryDate(self, deliveryDate):
        self.__deliveryDate = deliveryDate

    def set_userId(self, userId):
        self.__userId = userId

    # toString()
    def __str__(self):
        return (f"Courier[courierID={self.__courierID}, senderName={self.__senderName}, "
                f"receiverName={self.__receiverName}, weight={self.__weight}, status={self.__status}, "
                f"trackingNumber={self.__trackingNumber}, deliveryDate={self.__deliveryDate}, userID={self.__userId}]")
