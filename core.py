from objects import Lecture, Student, Teacher
from outputs import FileManager
from ui import Window


class Database:

    def __init__(self):
        self.window = Window()
        self.file_manager = FileManager()
        self.teachers, self.lectures, self.students = self.file_manager.load()
    
    def main_menu(self):
        heading = "== MAIN MENU =="
        menuitems = {
            1: {"name": "Teachers", "func": self.teachers_menu},
            2: {"name": "Lectures", "func": self.lectures_menu}, 
            3: {"name": "Students", "func": self.students_menu}, 
            4: {"name": "Save and exit", "func": self.save_and_exit}
        }
        choice = self.window.get_user_choice(menuitems, heading)
        return menuitems[choice]["func"]()

    def teachers_menu(self):
        menuitems = {
            1: {"name": "Add teacher", "func": self.add_teacher},
            2: {"name": "Delete teacher", "func": self.delete_teacher}, 
            3: {"name": "Show list of teachers", "func": self.list_teachers}, 
            4: {"name": "Return to main menu", "func": self.main_menu}
        }        
        choice = self.window.get_user_choice(menuitems)
        return menuitems[choice]["func"]()

    def lectures_menu(self):
        menuitems = {
            1: {"name": "Add lecture", "func": self.add_lecture},
            2: {"name": "Delete lecture", "func": self.delete_lecture},
            3: {"name": "Show list of lectures", "func": self.list_lectures},
            4: {"name": "Return to main menu", "func": self.main_menu}
        }
        choice = self.window.get_user_choice(menuitems)
        return menuitems[choice]["func"]()

    def students_menu(self):
        menuitems = {
            1: {"name": "Add student", "func": self.add_student},
            2: {"name": "Delete student", "func": self.delete_student},
            3: {"name": "Show list of students", "func": self.list_students},
            4: {"name": "Enroll student to lectures", "func": self.enroll_student},
            5: {"name": "Resign student from lectures", "func": self.resign_student},
            6: {"name": "Return to main menu", "func": self.main_menu}
        }
        choice = self.window.get_user_choice(menuitems)
        return menuitems[choice]["func"]()

    def save_and_exit(self):
        prompt = input("Do you want to save your progress? (Y/n) ").lower()
        if prompt != "n":
            self.file_manager.save(self.teachers, self.lectures, self.students)
            print("\nData was saved.", end=" ")
        return False

    def add_teacher(self):
        print()
        name = ""
        while name == "":
            name = input("What is the teacher's name? ")
        for teacher in self.teachers:
            if name == teacher.name:
                print(f"Error, {name} was already added.")
                return True
        self.teachers.append(Teacher(name))
        print(f"{name} successfuly added.")
        return True

    def delete_teacher(self):
        print()
        if len(self.teachers) == 0:
            print("\nThere are no teachers to delete.")
            return True
        menuitems = self.window.get_menu_items(self.teachers)
        heading = "Who do you want to delete from database?"
        id = self.window.get_user_choice(menuitems, heading) -1       
        teacher = self.teachers[id]
        prompt = input(f"Are you sure you want to delete {teacher.name}? (Y/n) ").lower()
        if prompt == "y":
            if len(teacher.lectures) > 0:
                print(f"You can't delete {teacher.name}, who is teaching {len(teacher.lectures)} lecture/s.")
            else:
                print(f"{teacher.name} succesfuly deleted.")
                self.teachers.remove(teacher)               
        return True

    def list_teachers(self):
        print("\n== LIST OF TEACHERS ==")
        for teacher in self.teachers:
            print(f"\n{teacher.name} is teaching:")
            for lecture in teacher.lectures:
                print(f"  {lecture.subject} ({lecture.number_of_students()} student/s)")
        return True

    def add_lecture(self):
        print()
        if self.teachers == []:
            print("There are no teachers in this school. You should hire some.")
            return True
        name = ""
        while name == "":
            name = input("What is the subject of this lecture? ")
        for lecture in self.lectures:
            if name == lecture.subject:
                print(f"Error, {name} was already added.")
                return True
        menuitems = self.window.get_menu_items(self.teachers)
        heading = "Who is going to teach this lecture?"
        id = self.window.get_user_choice(menuitems, heading) - 1
        teacher = self.teachers[id]
        lecture = Lecture(name, teacher)
        teacher.asign(lecture)
        self.lectures.append(lecture)
        print(f"{name} taught by {teacher.name} succesfuly added.")
        return True

    def delete_lecture(self):
        print()
        if len(self.lectures) == 0:
            print("\nThere are no lectures to delete.")
            return True
        menuitems = self.window.get_menu_items(self.lectures)
        heading = "What do you want to delete from database?"
        id = self.window.get_user_choice(menuitems, heading) - 1
        lecture = self.lectures[id]
        prompt = input(f"Are you sure you want to delete {lecture.subject}? (Y/n) ").lower()
        if prompt == "y":
            print(f"{lecture.subject} succesfuly deleted.")
            for student in self.students:
                if lecture in student.lectures:
                    student.resign(lecture)
            for teacher in self.teachers:
                if lecture in teacher.lectures:
                    teacher.resign(lecture)
            self.lectures.remove(lecture)
        return True

    def list_lectures(self):
        print("\n== LIST OF LECTURES ==")
        for lecture in self.lectures:
            print(f"\n{lecture.subject} taught by {lecture.teacher.name} is attended by:")
            for student in lecture.students:
                print(f"  {student.name}")
        return True

    def add_student(self):
        print()
        name = ""
        while name == "":
            name = input("What is the student's name? ")
        for student in self.students:
            if name == student.name:
                print(f"Error, {name} was already added.")
                return True
        self.students.append(Student(name))
        print(f"{name} successfuly added. Don't forget to sign up for lectures.")
        return True

    def delete_student(self):
        print()
        if len(self.students) == 0:
            print("\nThere are no students to delete.")
            return True       
        menuitems = self.window.get_menu_items(self.students)
        heading = "Who do you want to delete from database?"
        id = self.window.get_user_choice(menuitems, heading) - 1
        student = self.students[id]
        prompt = input(f"Are you sure you want to delete {student.name}? (Y/n) ").lower()
        if prompt == "y":
            print(f"{student.name} succesfuly deleted.")
            for lecture in self.lectures:
                if student in lecture.students:
                    lecture.dismiss(student)
            self.students.remove(student)
        return True

    def list_students(self):
        print("\n== LIST OF STUDENTS ==")
        for student in self.students:
            print(f"\n{student.name} is attending:")
            for lecture in student.lectures:
                print(f"  {lecture.subject} taught by {lecture.teacher.name}")
        return True

    def enroll_student(self):
        if len(self.lectures) == 0:
            print("There are no lectures to enroll to.")
            return True
        if len(self.students) == 0:
            print("There are no students to enroll.")
            return True
        menuitems = self.window.get_menu_items(self.students)
        heading = "Who do you want to enroll?"
        student_id = self.window.get_user_choice(menuitems, heading) - 1
        student = self.students[student_id]
        menuitems = self.window.get_menu_items(self.lectures)
        heading = "Which lectures does the student enroll to?"        
        ids = self.window.get_choices_list(menuitems, heading)
        lectures = [self.lectures[id-1] for id in ids]        
        for lecture in lectures:
            if lecture not in student.lectures:
                student.asign(lecture)
                lecture.enroll(student)        
        print(f"{student.name} is now enrolled to these lectures:")
        for lecture in student.lectures:
            print(f"  {lecture.subject} taught by {lecture.teacher.name}")        
        return True

    def resign_student(self):
        if len(self.students) == 0:
            print("There are no students to resign.")
            return True
        menuitems = self.window.get_menu_items(self.students)
        heading = "Who do you want to resign?"
        student_id = self.window.get_user_choice(menuitems, heading) - 1
        student = self.students[student_id]
        if len(student.lectures) == 0:
            print("There are no lectures to resign from.")
            return True       
        menuitems = self.window.get_menu_items(student.lectures)
        heading = "Which lectures does the student resign from?"
        ids = self.window.get_choices_list(menuitems, heading)
        lectures = [student.lectures[id-1] for id in ids]        
        for lecture in lectures:
            if lecture in student.lectures:
                student.resign(lecture)
                lecture.dismiss(student)        
        print(f"{student.name} has resigned from these lectures:")
        for lecture in lectures:
            print(f"  {lecture.subject} taught by {lecture.teacher.name}")        
        return True
