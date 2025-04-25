-- Create Database
create database SISDB1;
-- Use Database
use SISDB1

-- Recreate the tables


-- Create students table
CREATE TABLE students (
    student_id INT IDENTITY(1,1) PRIMARY KEY, -- Auto-increment for student_id
    first_name VARCHAR(20),
    last_name VARCHAR(30),
    date_of_birth DATE,
    email VARCHAR(30),
    phone_number BIGINT
);

-- Create teacher table
CREATE TABLE teacher (
    teacher_id INT IDENTITY(1,1) PRIMARY KEY, -- Auto-increment for teacher_id
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(50)
);

-- Create courses table with foreign key reference to teacher
CREATE TABLE courses (
    course_id INT IDENTITY(1,1) PRIMARY KEY, -- Auto-increment for course_id
    course_name VARCHAR(30),
    credits INT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
);

-- Create enrollments table with foreign keys referencing students and courses
CREATE TABLE enrollments (
    enrollment_id INT IDENTITY(1,1) PRIMARY KEY, -- Auto-increment for enrollment_id
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Create payments table with foreign key reference to students
CREATE TABLE payments (
    payment_id INT IDENTITY(1,1) PRIMARY KEY, -- Auto-increment for payment_id
    student_id INT,
    amount MONEY,
    payment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
 -- Check Students
SELECT * FROM students;

-- Check Teachers
SELECT * FROM teacher;

-- Check Courses
SELECT * FROM courses;

-- Check Enrollments
SELECT * FROM enrollments;

-- Check Payments
SELECT * FROM payments;

DELETE FROM enrollments WHERE course_id IN (301, 302);


DELETE FROM courses WHERE course_id IN (301, 302);

DELETE FROM payments;
DELETE FROM enrollments;
DELETE FROM courses;
DELETE FROM students;
DELETE FROM teacher;

