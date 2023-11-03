import math
class School:
    def __init__(self,name,classes,teachers):
        self.name = name
        self.classes = classes
        self.teachers = teachers
    def add_teacher(self,teacher):
        self.teachers.append(teacher)
    def add_school_classes(self,classes):
        self.school_classes.append(classes)
class Student:
    def __init__(self,name,age,grade,student_id):
        self.name = name
        self,age = age
        self.grade = grade
        self.student_id = student_id
        self.course = []
    def enroll_in_course(self,course):
        self.course.append(course)
    def submit_assignment_in_course(self,course,assignment):
    def take_exam_in_course(self,course,exam):
    def view_grade(self):
class Teacher:
    def __init__(self,name,assitance,subject):
        self.name = name
        self.assitance = assitance
        self.subject = subject
    def attend(self, date):
        self.attendance[date] = True
    def def teach_class(self, school_class):
        pass
       

