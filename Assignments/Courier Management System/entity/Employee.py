# 3. Employee Class
class Employee:
    def __init__(self, employeeID=None, employeeName=None, email=None, contactNumber=None, role=None, salary=None):
        self.__employeeID = employeeID
        self.__employeeName = employeeName
        self.__email = email
        self.__contactNumber = contactNumber
        self.__role = role
        self.__salary = salary

    # Getters
    def get_employeeID(self):
        return self.__employeeID

    def get_employeeName(self):
        return self.__employeeName

    def get_email(self):
        return self.__email

    def get_contactNumber(self):
        return self.__contactNumber

    def get_role(self):
        return self.__role

    def get_salary(self):
        return self.__salary

    # Setters
    def set_employeeID(self, employeeID):
        self.__employeeID = employeeID

    def set_employeeName(self, employeeName):
        self.__employeeName = employeeName

    def set_email(self, email):
        self.__email = email

    def set_contactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def set_role(self, role):
        self.__role = role

    def set_salary(self, salary):
        self.__salary = salary

    # toString()
    def __str__(self):
        return f"Employee[employeeID={self.__employeeID}, employeeName={self.__employeeName}, email={self.__email}, contactNumber={self.__contactNumber}, role={self.__role}, salary={self.__salary}]"

