# ICourierAdminService.py
from abc import ABC, abstractmethod

class ICourierAdminService(ABC):

    @abstractmethod
    def add_courier_staff(self, name, contactNumber):
        """
        Add a new courier staff member to the system.

        :param name: The name of the courier staff member
        :param contactNumber: The contact number of the courier staff member
        :return: The ID of the newly added courier staff member
        """
        pass
