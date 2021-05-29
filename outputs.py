import json
from objects import Lecture, Student, Teacher


class FileManager:

    def __init__(self):
        self.file = "./data.json"

    def load(self):
        teachers = []
        lectures = []
        students = []     
        try:
            with open(self.file) as file:
                data = json.load(file)
        except FileNotFoundError:
            return teachers, lectures, students
        for teacher in data["teachers"]:
            teachers.append(Teacher(teacher["name"])) 
        for subject in data["lectures"]:
            for teacher in teachers:
                if teacher.name == subject["teacher"]:
                    new_lecture = Lecture(subject["subject"], teacher)
                    lectures.append(new_lecture)
                    teacher.asign(new_lecture) 
        for student in data["students"]:
            new_student = Student(student["name"])
            students.append(new_student)
            for lecture in lectures:
                if lecture.subject in student["lectures"]:
                    new_student.asign(lecture)
                    lecture.enroll(new_student)
        return teachers, lectures, students

    def save(self, teachers, lectures, students):
        data = {
            "teachers": [],
            "lectures": [],
            "students": []
        }
        for teacher in teachers:
            data["teachers"].append(teacher.get_json())
        for lecture in lectures:
            data["lectures"].append(lecture.get_json())
        for student in students:
            data["students"].append(student.get_json())            
        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)        
