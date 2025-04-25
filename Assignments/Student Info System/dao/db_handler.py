from util.db_conn_util import DBConnUtil

class DBHandler:
    def __init__(self):
        self.conn = DBConnUtil.get_connection()
        self.cursor = self.conn.cursor()

    def insert_student(self, student):
        try:
            query = """
                INSERT INTO students (first_name, last_name, date_of_birth, email, phone_number)
                OUTPUT INSERTED.student_id
                VALUES (?, ?, ?, ?, ?)
            """
            self.cursor.execute(query, (
                student.first_name, student.last_name,
                student.date_of_birth, student.email, student.phone_number
            ))
            result = self.cursor.fetchone()
            if result:
                student_id = result[0]  # Fetch the inserted ID
                self.conn.commit()
                return student_id
            else:
                print("Error: No student ID returned from the insert query.")
                return None
        except Exception as e:
            print(f"Error inserting student: {e}")
            self.conn.rollback()
            return None

    def insert_teacher(self, teacher):
        try:
            query = """
                INSERT INTO teacher (first_name, last_name, email)
                OUTPUT INSERTED.teacher_id
                VALUES (?, ?, ?)
            """
            self.cursor.execute(query, (
                teacher.first_name, teacher.last_name, teacher.email
            ))
            result = self.cursor.fetchone()
            if result:
                teacher_id = result[0]  # Fetch the inserted ID
                self.conn.commit()
                return teacher_id
            else:
                print("Error: No teacher ID returned from the insert query.")
                return None
        except Exception as e:
            print(f"Error inserting teacher: {e}")
            self.conn.rollback()
            return None

    def insert_course(self, course):
        try:
            if course.teacher_id is None or self._teacher_exists(course.teacher_id):
                query = """
                    INSERT INTO courses (course_name, credits, teacher_id)
                    OUTPUT INSERTED.course_id
                    VALUES (?, ?, ?)
                """
                self.cursor.execute(query, (
                    course.course_name, course.credits, course.teacher_id
                ))
                result = self.cursor.fetchone()
                if result:
                    course_id = result[0]  # Fetch the inserted ID
                    self.conn.commit()
                    return course_id
                else:
                    print("Error: No course ID returned from the insert query.")
                    return None
            else:
                print(f"Teacher with ID {course.teacher_id} does not exist.")
                return None
        except Exception as e:
            print(f"Error inserting course: {e}")
            self.conn.rollback()
            return None

    def insert_enrollment(self, enrollment):
        try:
            if self._student_exists(enrollment.student.student_id) and self._course_exists(enrollment.course.course_id):
                query = """
                    INSERT INTO enrollments (student_id, course_id, enrollment_date)
                    OUTPUT INSERTED.enrollment_id
                    VALUES (?, ?, ?)
                """
                self.cursor.execute(query, (
                    enrollment.student.student_id,
                    enrollment.course.course_id,
                    enrollment.enrollment_date
                ))
                result = self.cursor.fetchone()
                if result:
                    enrollment_id = result[0]  # Fetch the inserted ID
                    self.conn.commit()
                    return enrollment_id
                else:
                    print("Error: No enrollment ID returned from the insert query.")
                    return None
            else:
                print("Invalid student ID or course ID for enrollment.")
                return None
        except Exception as e:
            print(f"Error inserting enrollment: {e}")
            self.conn.rollback()
            return None

    def insert_payment(self, payment):
        try:
            if self._student_exists(payment.student.student_id):
                query = """
                    INSERT INTO payments (student_id, amount, payment_date)
                    OUTPUT INSERTED.payment_id
                    VALUES (?, ?, ?)
                """
                self.cursor.execute(query, (
                    payment.student.student_id,
                    payment.amount, payment.payment_date
                ))
                result = self.cursor.fetchone()
                if result:
                    payment_id = result[0]  # Fetch the inserted ID
                    self.conn.commit()
                    return payment_id
                else:
                    print("Error: No payment ID returned from the insert query.")
                    return None
            else:
                print(f"Student with ID {payment.student.student_id} does not exist.")
                return None
        except Exception as e:
            print(f"Error inserting payment: {e}")
            self.conn.rollback()
            return None

    def update_course_teacher(self, course_id, teacher_id):
        try:
            if self._teacher_exists(teacher_id):
                query = "UPDATE courses SET teacher_id = ? WHERE course_id = ?"
                self.cursor.execute(query, (teacher_id, course_id))
                self.conn.commit()
            else:
                print(f"Teacher with ID {teacher_id} does not exist.")
        except Exception as e:
            print(f"Error updating course teacher: {e}")
            self.conn.rollback()

    # --- Helper Methods ---

    def _student_exists(self, student_id):
        query = "SELECT COUNT(*) FROM students WHERE student_id = ?"
        self.cursor.execute(query, (student_id,))
        return self.cursor.fetchone()[0] > 0

    def _course_exists(self, course_id):
        query = "SELECT COUNT(*) FROM courses WHERE course_id = ?"
        self.cursor.execute(query, (course_id,))
        return self.cursor.fetchone()[0] > 0

    def _teacher_exists(self, teacher_id):
        query = "SELECT COUNT(*) FROM teacher WHERE teacher_id = ?"
        self.cursor.execute(query, (teacher_id,))
        return self.cursor.fetchone()[0] > 0

    def close_connection(self):
        self.conn.close()
