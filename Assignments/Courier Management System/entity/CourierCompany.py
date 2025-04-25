# CourierCompany.py
class CourierCompany:
    def __init__(self, companyName=None, courierDetails=None, employeeDetails=None, locationDetails=None):
        self.__companyName = companyName
        self.__courierDetails = courierDetails if courierDetails else []
        self.__employeeDetails = employeeDetails if employeeDetails else []
        self.__locationDetails = locationDetails if locationDetails else []

    # Getters
    def get_companyName(self):
        return self.__companyName

    def get_courierDetails(self):
        return self.__courierDetails

    def get_employeeDetails(self):
        return self.__employeeDetails

    def get_locationDetails(self):
        return self.__locationDetails

    # Setters
    def set_companyName(self, companyName):
        self.__companyName = companyName

    def set_courierDetails(self, courierDetails):
        self.__courierDetails = courierDetails

    def set_employeeDetails(self, employeeDetails):
        self.__employeeDetails = employeeDetails

    def set_locationDetails(self, locationDetails):
        self.__locationDetails = locationDetails

    # toString()
    def __str__(self):
        return f"CourierCompany[companyName={self.__companyName}, courierDetails={self.__courierDetails}, employeeDetails={self.__employeeDetails}, locationDetails={self.__locationDetails}]"

