# entity/CourierCompanyCollection.py

from entity.Courier import Courier

class CourierCompanyCollection:
    def __init__(self):
        self._courier_list = []

    def add_courier(self, courier: Courier):
        self._courier_list.append(courier)

    def get_all_couriers(self):
        return self._courier_list

    def get_courier_by_tracking(self, tracking_number: int):
        for courier in self._courier_list:
            if courier.get_tracking_number() == tracking_number:
                return courier
        return None

    def remove_courier(self, tracking_number: int):
        for courier in self._courier_list:
            if courier.get_tracking_number() == tracking_number:
                self._courier_list.remove(courier)
                return True
        return False

    def get_couriers_by_user(self, user_id: int):
        return [c for c in self._courier_list if c.get_userID() == user_id]
