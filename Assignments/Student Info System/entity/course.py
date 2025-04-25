class Course:
    def __init__(self, course_id, course_name, credits, teacher_id=None, course_code=None, instructor_name=None):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.teacher_id = teacher_id
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.enrollments = []

    def assign_teacher(self, teacher):
        self.teacher_id = teacher.teacher_id
        self.instructor_name = f"{teacher.first_name} {teacher.last_name}"
        teacher.assigned_courses.append(self)

    def update_course_info(self, course_code, course_name, instructor_name):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name

    def display_course_info(self):
        print(f"Course ID: {self.course_id} | Name: {self.course_name} | Credits: {self.credits} | Instructor: {self.instructor_name}")

    def get_enrollments(self):
        return self.enrollments

    def get_teacher(self):
        return self.teacher_id
