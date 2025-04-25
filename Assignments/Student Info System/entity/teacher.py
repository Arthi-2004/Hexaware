class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses = []

    def update_info(self, name, email, expertise=None):
        self.first_name, self.last_name = name.split(" ")
        self.email = email

    def display_info(self):
        print(f"Teacher: {self.first_name} {self.last_name} | Email: {self.email}")

    def get_assigned_courses(self):
        return self.assigned_courses
