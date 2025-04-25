import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.db_handler import DBHandler
from entity.student import Student
from entity.enrollment import Enrollment
from entity.course import Course
from entity.teacher import Teacher
from entity.payment import Payment
from dao.sis_manager import SISManager

db = DBHandler()

# Add Alice
alice = Student(None, "Alice", "Cooper", "1996-12-01", "alice.cooper@example.com", "3216549870")
alice_id = db.insert_student(alice)
alice.student_id = alice_id
print(f"Student added: {alice.first_name} {alice.last_name} to students table.\n")

# Add John (teacher)
teacher_john = Teacher(None, "John", "Miller", "john.miller@example.com")
john_id = db.insert_teacher(teacher_john)
teacher_john.teacher_id = john_id
print(f"Teacher added: {teacher_john.first_name} {teacher_john.last_name} as teacher.\n")

# Add Courses
course1 = Course(None, "Introduction to Programming", 4, john_id)
course2 = Course(None, "Mathematics 101", 3, john_id)
course1.course_id = db.insert_course(course1)
course2.course_id = db.insert_course(course2)
print(f"Courses added: {course1.course_name} (Credits: {course1.credits}), {course2.course_name} (Credits: {course2.credits}).\n")

# Enroll Alice
enroll1 = Enrollment(None, alice, course1, "2025-04-18")
enroll2 = Enrollment(None, alice, course2, "2025-04-18")
db.insert_enrollment(enroll1)
db.insert_enrollment(enroll2)
print(f"{alice.first_name} enrolled in courses: {course1.course_name}, {course2.course_name}.\n")

# Assign Sarah Smith
sarah = Teacher(None, "Sarah", "Smith", "sarah.smith@example.com")
sarah_id = db.insert_teacher(sarah)
sarah.teacher_id = sarah_id

new_course = Course(None, "Advanced Database Management", 4, sarah_id)
new_course.course_id = db.insert_course(new_course)
db.update_course_teacher(new_course.course_id, sarah_id)

print("\n==============================")
print("Task 9 – Teacher Assignment:")
print(f"Teacher: {sarah.first_name} {sarah.last_name} | Email: {sarah.email}")
print(f"Course ID: {new_course.course_id} | Name: {new_course.course_name} | Credits: {new_course.credits} | Instructor: {sarah.first_name} {sarah.last_name}")
print("==============================\n")

# Jane Johnson makes payment
jane = Student(None, "Jane", "Johnson", "2000-02-15", "jane.johnson@example.com", "9876543210")
jane_id = db.insert_student(jane)
jane.student_id = jane_id

payment = Payment(None, jane, 500.00, "2023-04-10")
db.insert_payment(payment)

print("\n==============================")
print("Task 10 – Payment Record:")
print(f"Student: {jane.first_name} {jane.last_name} | Payment: ₹{payment.amount} | Date: {payment.payment_date}")
print("==============================\n")

# Enrollment report
print("\n==============================")
print("Task 11 – Enrollment Report Generation:")
sis = SISManager()

cs_course = Course(None, "Computer Science 101", 4, None)
cs_course.course_id = db.insert_course(cs_course)

student1 = Student(None, "Aditi", "Rao", "2002-04-10", "aditi.rao@example.com", "9090909090")
student2 = Student(None, "Rahul", "Verma", "2001-03-15", "rahul.verma@example.com", "8080808080")

student1.student_id = db.insert_student(student1)
student2.student_id = db.insert_student(student2)

enrollment1 = Enrollment(None, student1, cs_course, "2025-04-21")
enrollment2 = Enrollment(None, student2, cs_course, "2025-04-21")vs
db.insert_enrollment(enrollment1)
db.insert_enrollment(enrollment2)

print(f"Enrollment Report for {cs_course.course_name}:")
for e in [enrollment1, enrollment2]:
    print(f"Student ID: {e.student.student_id} | Name: {e.student.first_name} {e.student.last_name} | Enrolled on: {e.enrollment_date}")
print("==============================\n")

db.close_connection()
