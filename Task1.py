class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grades(self):
        if not self.grades:
            return 0
        average_grades_list = []
        for grade in self.grades.values():
            average_grades_list.extend(grade)
        return round(sum(average_grades_list) / len(average_grades_list), 2)

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grades()}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_grades() < other.average_grades()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_grades() > other.average_grades()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_grades() == other.average_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grades(self):
        if not self.grades:
            return 0
        average_grades_list = []
        for grade in self.grades.values():
            average_grades_list.extend(grade)
        return round(sum(average_grades_list) / len(average_grades_list), 2)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grades()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_grades() < other.average_grades()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_grades() > other.average_grades()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_grades() == other.average_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_lecturer1 = Lecturer('Стивен', 'Роджерс')
best_lecturer1.courses_attached += ['Python']

best_lecturer2 = Lecturer('Клинтон', 'Бартон')
best_lecturer2.courses_attached += ['C+']

best_lecturer3 = Lecturer('Ванда', 'Максимофф')
best_lecturer3.courses_attached += ['Java']

cool_reviewer1 = Reviewer('Марк', 'Спектор')
cool_reviewer1.courses_attached += ['Python']
cool_reviewer1.courses_attached += ['C+']

cool_reviewer2 = Reviewer('Наташа', 'Романофф')
cool_reviewer2.courses_attached += ['C+']
cool_reviewer2.courses_attached += ['Java']

student1 = Student('Шэрон', 'Картер')
student1.courses_in_progress += ['Python', 'C+']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Генри', 'Маккой')
student2.courses_in_progress += ['Java', 'Python']
student2.finished_courses += ['Введение в программирование']

student3 = Student('Джеймс', 'Роудс')
student3.courses_in_progress += ['C+']
student3.finished_courses += ['Введение в программирование']

student1.rate_hw(best_lecturer1, 'Python', 6)
student1.rate_hw(best_lecturer1, 'Python', 9)
student1.rate_hw(best_lecturer1, 'Python', 1)

student1.rate_hw(best_lecturer2, 'C+', 2)
student1.rate_hw(best_lecturer2, 'C+', 9)
student1.rate_hw(best_lecturer2, 'C+', 9)

student2.rate_hw(best_lecturer2, 'C+', 2)
student2.rate_hw(best_lecturer2, 'C+', 2)
student2.rate_hw(best_lecturer2, 'C+', 3)

student2.rate_hw(best_lecturer3, 'Java', 4)
student2.rate_hw(best_lecturer3, 'Java', 8)
student2.rate_hw(best_lecturer3, 'Java', 9)

cool_reviewer1.rate_hw(student1, 'Python', 8)
cool_reviewer1.rate_hw(student1, 'Python', 4)
cool_reviewer1.rate_hw(student1, 'Python', 3)
cool_reviewer1.rate_hw(student1, 'C+', 2)
cool_reviewer1.rate_hw(student1, 'C+', 3)

cool_reviewer2.rate_hw(student2, 'Java', 8)
cool_reviewer2.rate_hw(student2, 'Java', 5)
cool_reviewer2.rate_hw(student2, 'Java', 2)
cool_reviewer2.rate_hw(student2, 'Python', 9)
cool_reviewer2.rate_hw(student2, 'Python', 8)

cool_reviewer2.rate_hw(student3, 'C+', 5)
cool_reviewer2.rate_hw(student3, 'C+', 7)
cool_reviewer2.rate_hw(student3, 'C+', 3)

print(f'Перечень студентов:\n\n{student1}\n\n{student2}\n\n{student3}')
print()

print(f'Перечень лекторов:\n\n{best_lecturer1}\n\n{best_lecturer2}\n\n{best_lecturer3}')
print()

print(f'Результат сравнения студентов (по средним оценкам за домашние задания): '
      f'{student1.name} {student1.surname} > {student2.name} {student2.surname}'
      f'{student1 > student2}')
print()

print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer1.name} {best_lecturer1.surname} > {best_lecturer2.name} {best_lecturer2.surname}'
      f'{best_lecturer1 > best_lecturer2}')
print()

student_list = [student1, student2, student3]
lecturer_list = [best_lecturer1, best_lecturer2, best_lecturer3]


def student_rating(student_list, course_name):
    count_all = []
    for stud in student_list:
        count_all.extend(stud.grades.get(course_name, []))
    if not count_all:
        return 'По такому курсу нет оценок'
    return round(sum(count_all) / len(count_all), 2)


def lecturer_rating(lecturer_list, course_name):
    count_all = []
    for lectur in lecturer_list:
        count_all.extend(lectur.grades.get(course_name, []))
    if not count_all:
        return 'По такому курсу нет оценок'
    return round(sum(count_all) / len(count_all), 2)


print(f"Средняя оценка для всех студентов по курсу {'Java'}: {student_rating(student_list, 'Java')}")
print()

print(f"Средняя оценка для всех студентов по курсу {'C+'}: {student_rating(student_list, 'C+')}")
print()

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'Java'}: {lecturer_rating(lecturer_list, 'Java')}")
print()

print(f"Средняя оценка для всех лекторов по курсу {'C+'}: {lecturer_rating(lecturer_list, 'C+')}")
print()

print(f'Средняя оценка за ДЗ:\n'
      f'{student1.name} {student1.surname} < {student2.name} {student2.surname}\n'
      'Верно' if student1 < student2 else 'Неверно')
print()

print(student1.__lt__(student2))
print()

print(student1 < student2)
print()

print('Средняя оценка за лекции:')
print(f'{best_lecturer1.name} {best_lecturer1.surname} > {best_lecturer3.name} {best_lecturer3.surname}')
print('Верно' if best_lecturer1 > best_lecturer3 else 'Неверно')
print()

print(best_lecturer1 > best_lecturer3)
print()

print(best_lecturer1.__le__(best_lecturer3))