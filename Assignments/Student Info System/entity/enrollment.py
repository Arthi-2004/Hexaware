class Enrollment:
    def __init__(self, enrollment_id, student, course, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student = student            # Reference to a Student object
        self.course = course              # Reference to a Course object
        self.enrollment_date = enrollment_date


    def get_student(self):
        return self.student_id

    def get_course(self):
        return self.course_id
