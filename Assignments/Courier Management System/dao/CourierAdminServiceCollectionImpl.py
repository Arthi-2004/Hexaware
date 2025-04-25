from dao.CourierUserServiceCollectionImpl import CourierUserServiceCollectionImpl
from dao.ICourierAdminService import ICourierAdminService

class CourierAdminServiceCollectionImpl(CourierUserServiceCollectionImpl, ICourierAdminService):
    def viewAllCouriers(self):
        return self.companyObj.getAllCouriers()

    def viewAllEmployees(self):
        return self.companyObj.getAllEmployees()
