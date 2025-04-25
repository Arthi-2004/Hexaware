from util.db_conn_util import DBConnUtil
from entity.enrollment import Enrollment
from entity.payment import Payment

class SISManager:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def add_enrollment(self, student, course, enrollment_date):
        self.cursor.execute(
            "SELECT COUNT(*) FROM enrollments WHERE student_id = ? AND course_id = ?",
            (student.student_id, course.course_id)
        )
        if self.cursor.fetchone()[0] > 0:
            print("⚠️ Student already enrolled in this course.")
            return

        self.cursor.execute(
            "INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)",
            (student.student_id, course.course_id, enrollment_date)
        )
        self.conn.commit()
        print(f"✅ Enrolled {student.first_name} in {course.course_name}")

    def assign_course_to_teacher(self, course, teacher):
        self.cursor.execute(
            "UPDATE courses SET teacher_id = ? WHERE course_id = ?",
            (teacher.teacher_id, course.course_id)
        )
        self.conn.commit()
        print(f"✅ Assigned {teacher.first_name} to teach {course.course_name}")

    def add_payment(self, student, amount, payment_date):
        self.cursor.execute(
            "INSERT INTO payments (student_id, amount, payment_date) VALUES (?, ?, ?)",
            (student.student_id, amount, payment_date)
        )
        self.conn.commit()
        print(f"💰 Recorded payment of ₹{amount} for {student.first_name}")

    def get_enrollments_for_student(self, student):
        self.cursor.execute(
            "SELECT e.enrollment_id, c.course_name, e.enrollment_date "
            "FROM enrollments e JOIN courses c ON e.course_id = c.course_id "
            "WHERE e.student_id = ?",
            (student.student_id,)
        )
        return self.cursor
