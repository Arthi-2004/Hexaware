from dao.CourierUserServiceImpl import CourierUserServiceImpl
from dao.ICourierAdminService import ICourierAdminService

class CourierAdminServiceImpl(CourierUserServiceImpl, ICourierAdminService):
    def viewAllCouriers(self):
        return self.companyObj.getAllCouriers()

    def viewAllEmployees(self):
        return self.companyObj.getAllEmployees()
