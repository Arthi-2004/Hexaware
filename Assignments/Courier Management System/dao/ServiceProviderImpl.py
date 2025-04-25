from exception.TrackingNumberNotFoundException import TrackingNumberNotFoundException
from exception.InvalidEmployeeIdException import InvalidEmployeeIdException

class ServiceProviderImpl:

    def getOrderStatus(self, trackingNumber, courierList):
        if trackingNumber not in [c.get_trackingNumber() for c in courierList]:
            raise TrackingNumberNotFoundException(f"Tracking number {trackingNumber} is invalid.")
        return "In Transit"

    def validateEmployee(self, empId, employeeList):
        if empId not in [e.get_empId() for e in employeeList]:
            raise InvalidEmployeeIdException(f"Employee ID {empId} does not exist.")
        return True

