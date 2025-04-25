from dao.ICourierUserService import ICourierUserService
from entity.CourierCompany import CourierCompany

class CourierUserServiceImpl(ICourierUserService):
    def __init__(self):
        self.companyObj = CourierCompany()

    def placeOrder(self, senderName, senderAddress, receiverName, receiverAddress, weight, employeeId):
        return self.companyObj.addCourier(senderName, senderAddress, receiverName, receiverAddress, weight, employeeId)

    def getOrderStatus(self, trackingNumber):
        return self.companyObj.getCourierStatus(trackingNumber)

    def cancelOrder(self, trackingNumber):
        return self.companyObj.removeCourier(trackingNumber)

    def getAssignedOrder(self, empId):
        return self.companyObj.getCourierByEmployeeId(empId)
