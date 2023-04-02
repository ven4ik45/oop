student_list = []
lecturer_list = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        student_list.append(self)

    def __str__(self):
        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за домашние задания:{self.average_rate():0.2f}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
              f'Завершенные курсы: {self.finished_courses}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Chracter')
            return
        return self.average_rate() < other.average_rate()

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (lecturer.courses_attached and self.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self):
        score = [sum(grade) for course, grade in self.grades.items()][0]
        count_grades = [len(v) for k, v in self.grades.items()][0]
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
        lecturer_list.append(self)

    def average_rate(self):
        score = [sum(grade) for course, grade in self.grades.items()][0]
        count_grades = [len(v) for k, v in self.grades.items()][0]
        average = (score/count_grades)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_rate()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Chracter')
            return
        return self.average_rate() < other.average_rate()


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


def average_all_rates(person_list, course):
    total_score = 0
    total_count = 0
    for student in person_list:
        for k, v in student.__dict__['grades'].items():
            if k == course:
                score = sum(v)
                count_grades = len(v)
                total_score += score
                total_count += count_grades
    average = round(total_score/total_count, 2)
    return average


first_student = Student('Максим', 'Попов', 'm')
first_student.courses_in_progress += ['Python']
first_student.finished_courses += ['Введение в программирование']

third_student = Student('Илья', 'Трубачев', 'm')
third_student.courses_in_progress += ['Python']
third_student.finished_courses += ['Введение в программирование']

second_student = Student('Кристина', 'Стрельцова', 'w')
second_student.courses_in_progress += ['Java']
second_student.finished_courses += ['Введение в программирование']

multi_reviewer = Reviewer('Евгений', 'Михайлов')
multi_reviewer.courses_attached += ['Python']
multi_reviewer.courses_attached += ['Java']

multi_reviewer.rate_hw(first_student, 'Python', 10)
multi_reviewer.rate_hw(first_student, 'Python', 3)
multi_reviewer.rate_hw(first_student, 'Python', 6)

multi_reviewer.rate_hw(second_student, 'Java', 10)
multi_reviewer.rate_hw(second_student, 'Java', 7)
multi_reviewer.rate_hw(second_student, 'Java', 4)
multi_reviewer.rate_hw(second_student, 'Java', 9)

multi_reviewer.rate_hw(third_student, 'Python', 8)
multi_reviewer.rate_hw(third_student, 'Python', 4)
multi_reviewer.rate_hw(third_student, 'Python', 9)
multi_reviewer.rate_hw(third_student, 'Python', 7)

first_lecturer = Lecturer('Андрей', 'Кузнецов')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Светлана', 'Белова')
second_lecturer.courses_attached += ['Java']

third_lecturer = Lecturer('Елизавета', 'Севастьянова')
third_lecturer.courses_attached += ['Python']

first_student.rate_lecturer(first_lecturer, 'Python', 10)
third_student.rate_lecturer(first_lecturer, 'Python', 9)
first_student.rate_lecturer(first_lecturer, 'Python', 3)

second_student.rate_lecturer(second_lecturer, 'Java', 9)
second_student.rate_lecturer(second_lecturer, 'Java', 10)
second_student.rate_lecturer(second_lecturer, 'Java', 7)
second_student.rate_lecturer(second_lecturer, 'Java', 5)

first_student.rate_lecturer(third_lecturer, 'Python', 8)
third_student.rate_lecturer(third_lecturer, 'Python', 4)
first_student.rate_lecturer(third_lecturer, 'Python', 9)
third_student.rate_lecturer(third_lecturer, 'Python', 8)
first_student.rate_lecturer(third_lecturer, 'Python', 10)


print(multi_reviewer)

print(first_lecturer)
print(second_lecturer)
print(third_lecturer)

print(first_student)
print(second_student)
print(third_student)

print(first_student > second_student)
print(second_lecturer > first_lecturer)

print(average_all_rates(student_list, 'Python'))
print(average_all_rates(lecturer_list, 'Python'))
