from datetime import datetime
from entity.payment import Payment
from entity.enrollment import Enrollment

class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.enrollments = []
        self.payments = []

    def enroll_in_course(self, course):
        enrollment = Enrollment(len(self.enrollments)+1, self.student_id, course.course_id, str(datetime.today().date()))
        self.enrollments.append(enrollment)
        course.enrollments.append(enrollment)

    def update_info(self, first_name, last_name, date_of_birth, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number

    def make_payment(self, amount, payment_date):
        payment = Payment(len(self.payments)+1, self.student_id, amount, payment_date)
        self.payments.append(payment)

    def display_info(self):
        print(f"Student ID: {self.student_id}\nName: {self.first_name} {self.last_name}")
        print(f"DOB: {self.date_of_birth} | Email: {self.email} | Phone: {self.phone_number}")

    def get_enrolled_courses(self):
        return self.enrollments

    def get_payment_history(self):
        return self.payments
