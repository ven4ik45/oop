class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за домашние задания:{self.average_rate():0.2f}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
              f'Завершенные курсы: {self.finished_courses}\n'
        return res

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (lecturer.courses_attached and self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self):
        score = [sum([sum(grade) for course, grade in self.grades.items()])][0]
        count_grades = [sum([len(v) for k, v in self.grades.items()])][0]
        average = (score/count_grades)
        return average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rate(self):
        score = [sum([sum(grade) for course, grade in self.grades.items()])][0]
        count_grades = [sum([len(v) for k, v in self.grades.items()])][0]
        average = (score/count_grades)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_rate()}\n'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in (self.courses_attached and student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n'
        return res


best_student = Student('Ученик', 'Иванов', 'm')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Иван', 'Проверяющий')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Java', 7)
cool_reviewer.rate_hw(best_student, 'Java', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 6)



cool_lecturer = Lecturer('Учитель', 'Петров')
cool_lecturer.courses_attached += ['Python']

best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 3)

best_student.rate_lecturer(cool_lecturer, 'Java', 7)
best_student.rate_lecturer(cool_lecturer, 'Java', 8)

print(cool_reviewer)
print(cool_lecturer)
print(best_student)
