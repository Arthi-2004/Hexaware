class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address, created_at=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.created_at = created_at  # Include created_at to avoid the error

    def get_customer_id(self):
        return self.customer_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def get_created_at(self):
        return self.created_at  # Optional method to access created_at field
