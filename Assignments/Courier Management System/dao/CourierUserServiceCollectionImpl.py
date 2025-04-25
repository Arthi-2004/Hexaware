# dao/CourierUserServiceCollectionImpl.py

from entity.CourierCompanyCollection import CourierCompanyCollection
from entity.Courier import Courier
from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException

class CourierUserServiceCollectionImpl:
    def __init__(self):
        self.companyObj = CourierCompanyCollection()

    def placeOrder(self, senderName, senderAddress, receiverName, receiverAddress, weight, userId):
        courier = Courier(senderName, senderAddress, receiverName, receiverAddress, weight, "yetToTransit", userId)
        self.companyObj.add_courier(courier)
        return courier.get_tracking_number()

    def getOrderStatus(self, trackingNumber):
        courier = self.companyObj.get_courier_by_tracking(trackingNumber)
        if courier is None:
            raise TrackingNumberNotFoundException(f"No courier found with tracking number {trackingNumber}")
        return courier.get_status()

    def cancelOrder(self, trackingNumber):
        return self.companyObj.remove_courier(trackingNumber)

    def getAssignedOrder(self, courierStaffId):
        return self.companyObj.get_couriers_by_user(courierStaffId)  # Assuming userID represents staff too
