# ICourierUserService.py
from abc import ABC, abstractmethod

class ICourierUserService(ABC):

    @abstractmethod
    def place_order(self, courierObj):
        """
        Place a new courier order.

        :param courierObj: Courier object created using values entered by users
        :return: The unique tracking number for the courier order
        """
        pass

    @abstractmethod
    def get_order_status(self, trackingNumber):
        """
        Get the status of a courier order.

        :param trackingNumber: The tracking number of the courier order
        :return: The status of the courier order (e.g., yetToTransit, In Transit, Delivered)
        """
        pass

    @abstractmethod
    def cancel_order(self, trackingNumber):
        """
        Cancel a courier order.

        :param trackingNumber: The tracking number of the courier order to be canceled
        :return: True if the order was successfully canceled, false otherwise
        """
        pass

    @abstractmethod
    def get_assigned_order(self, courierStaffId):
        """
        Get a list of orders assigned to a specific courier staff member.

        :param courierStaffId: The ID of the courier staff member
        :return: A list of courier orders assigned to the staff member
        """
        pass
