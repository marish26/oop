class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grad(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses and course in lector.courses:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lector(Mentor):
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses = {}
class Rewiures(Mentor):
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.coursed = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.coursed and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']

cool_mentor = Rewiures('Some', 'Buddy')
cool_mentor.coursed += ['Python']
cool_mentor.coursed += ['Java']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Java', 8)
cool_mentor.rate_hw(best_student, 'Python', 9)

best_lector = Lector('Mar','Jev')
best_lector.courses = {'Python' : 10}
best_lector.courses = {'Java' : 11}



print(best_student.grades)
print(best_lector.courses)

