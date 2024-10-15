class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} old"
    
    def __str__(self) -> str:
        return f'<name>:{self.name}, <age>:{self.age}'

class Student(Person):
    """A class to model a student in a classroom"""
    def __init__(self, name,age, grade):
        super().__init__(name, age)
        """Initialize the attributes of the student"""
        self.grade = grade #Private attributes (encapsulated)

    def enroll(self):
        """Display student information"""
        return f"{self.name} is enrolled"
     
    def view_grade(self):
        """Display student information"""
        return f"{self.name}'s grade is {self.grade}"

class Course(Student):
    def __init__(self, name, age, grade, course):
        super().__init__(name, age, grade)
        self.course = course
    
    def assigncourse_grade(self, student, **course_info):
        student.grade = self.grade
        course_info['course'] = self.course
        course_info['grade'] = student.grade
        course_info['name'] = self.name
        return course_info


person1 = Person("James", 32)
print(person1)

student1 = Student("John Doe", 20)
print(student1)

course1 = Course('James', 20, 'B', 'Math')
print(course1)

testing = course1.assigncourse_grade(student1)
print(testing)
# course1 = Course('James',  'math')
# print(course1)