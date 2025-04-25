class DuplicateEnrollmentException(Exception):
    def __init__(self, message="Student already enrolled in this course."):
        super().__init__(message)

class CourseNotFoundException(Exception):
    def __init__(self, message="Course not found."):
        super().__init__(message)

class StudentNotFoundException(Exception):
    def __init__(self, message="Student not found."):
        super().__init__(message)

class TeacherNotFoundException(Exception):
    def __init__(self, message="Teacher not found."):
        super().__init__(message)

class PaymentValidationException(Exception):
    def __init__(self, message="Invalid payment amount or date."):
        super().__init__(message)

class InvalidStudentDataException(Exception):
    def __init__(self, message="Invalid student data provided."):
        super().__init__(message)

class InvalidCourseDataException(Exception):
    def __init__(self, message="Invalid course data provided."):
        super().__init__(message)

class InvalidEnrollmentDataException(Exception):
    def __init__(self, message="Invalid enrollment data."):
        super().__init__(message)

class InvalidTeacherDataException(Exception):
    def __init__(self, message="Invalid teacher data."):
        super().__init__(message)

class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds for enrollment."):
        super().__init__(message)
