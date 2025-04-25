class Payment:
    def __init__(self, payment_id, student, amount, payment_date):
        self.payment_id = payment_id
        self.student = student        # Reference to Student object
        self.amount = amount
        self.payment_date = payment_date

    def get_student(self):
        return self.student  # returns the Student object

    def get_payment_amount(self):
        return self.amount

    def get_payment_date(self):
        return self.payment_date


