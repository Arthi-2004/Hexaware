from entity.donation import Donation

class ItemDonation(Donation):
    def __init__(self, donor_name, amount, item_type):
        super().__init__(donor_name, amount)
        self._item_type = item_type

    def record_donation(self):
        return f"Item Donation recorded: Donor: {self._donor_name}, Item: {self._item_type}, Value: ${self._amount}"
