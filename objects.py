class Lecture:

    def __init__(self, subject, teacher):
        self.subject = subject
        self.teacher = teacher
        self.name = f"{self.subject} taught by {self.teacher.name}"
        self.students = []

    def enroll(self, student):
        self.students.append(student)

    def dismiss(self, student):
        self.students.remove(student)

    def number_of_students(self):
        return len(self.students)
    
    def get_json(self):
        data = {
            "subject": self.subject,
            "teacher": self.teacher.name,
            "students": [student.name for student in self.students]
        }
        return data


class Person:

    def __init__(self, name):
        self.name = name
        self.lectures = []

    def asign(self, lecture):
        self.lectures.append(lecture)

    def resign(self, lecture):
        self.lectures.remove(lecture)

    def get_json(self):
        data = {
            "name": self.name,
            "lectures": [lecture.subject for lecture in self.lectures]
        }
        return data


class Student(Person):

    def __init__(self, name):
        super().__init__(name)
    

class Teacher(Person):

    def __init__(self, name):
        super().__init__(name)
