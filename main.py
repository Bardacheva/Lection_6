class Student:
    items = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = 0
        Student.items.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        '''
        Реализует возможность выставления оценок лекторам у класса Student (оценки по 10-балльной шкале, хранятся
        в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок).
        Лектор при этом должен быть закреплен за тем курсом, на который записан студент.
        '''
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in \
                self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def middle_student(self):
        '''На основании оценок, выставленных преподавателями, рассчитывает среднюю оценку студента за
        домашние задания.'''
        # list_values_st = []
        # for self.value in self.grades.values():
        #     list_values_st.append(self.value)
        # for i in list_values_st:
        #     result = sum(i) / len(i)
        #     self.average = result + self.average
        # return self.average
        list_values_st = []
        for cours in self.grades:
            for grade in self.grades[cours]:
                list_values_st += [grade]
        if not list_values_st:
            return 'Ошибка!'
        else:
            average = sum(list_values_st) / len(list_values_st)
        return average


    def __lt__(self, other):
        '''Сравнивает среднюю оценку студента: меньше ли она средней оценки другого студента'''
        return self.average < other.average

    def __le__(self, other):
        '''Сравнивает среднюю оценку студента: меньше ли она или равна средней оценке другого студента'''
        return self.average <= other.average

    def __eq__(self, other):
        '''Сравнивает среднюю оценку студента: равна ли она средней оценке другого студента'''
        return self.average == other.average

    def __str__(self):
        '''
        Выводит информацию о студенте в формате:
        print(some_student)
        Имя: Ruoy
        Фамилия: Eman
        Средняя оценка за  домашние  задания: 9.9
        Курсы в процессе изучения: Python, Git
        Завершенные курсы: Введение в программирование
        '''
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: ' \
               f'{round(self.middle_student(), 2)}\nКурсы в процессе изучения:{self.courses_in_progress}\n' \
               f'Завершенные курсы:{self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    items = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.average = 0
        Lecturer.items.append(self)

    def middle_lecturer(self):
        '''На основании оценок, выставленных студентами, рассчитывает среднюю оценку лектора за
        лекции.'''
        # list_values_lec = []
        # for self.value in self.grades.values():
        #     list_values_lec.append(self.value)
        # for i in list_values_lec:
        #     result = sum(i) / len(i)
        #     self.average = result + self.average
        # return self.average

        list_values_lec = []
        for cours in self.grades:
            for grade in self.grades[cours]:
                list_values_lec += [grade]
        if not list_values_lec:
            return 'Ошибка!'
        else:
            average = sum(list_values_lec) / len(list_values_lec)
        return average

    def __lt__(self, other):
        '''Сравнивает среднюю оценку лектора: меньше ли она средней оценки другого лектора'''
        return self.average < other.average

    def __le__(self, other):
        '''Сравнивает среднюю оценку лектора: меньше ли она или равна средней оценке другого лектора'''
        return self.average <= other.average

    def __eq__(self, other):
        '''Сравнивает среднюю оценку лектора: равна ли она средней оценке другого лектора'''
        return self.average == other.average

    def __str__(self):
        '''
        Выводит информацию о лекторе в формате:
        Имя: Some
        Фамилия: Buddy
        Средняя оценка за лекции: 9.9
        '''
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:' \
               f' {round(self.middle_lecturer(), 2)}'

class Reviewer(Mentor):
    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        '''
        Выводит информацию о проверяющих в формате:
        Имя: Some
        Фамилия: Buddy
        '''
        return f'Имя: {self.name}\nФамилия: {self.surname}'


'''Создаем по два экземпляра каждого класса'''

student1 = Student('Ruoy', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Kotlin']

student2 = Student('Tom', 'Colman', 'male')
student2.courses_in_progress += ['Python']

mentor1 = Reviewer('David', 'Jordan')
mentor1.courses_attached += ['Python']
mentor1.courses_attached += ['Kotlin']

mentor2 = Reviewer('Ann', 'Jackson')
mentor2.courses_attached += ['Python']

mentor3 = Lecturer('Nic', 'Peters')
mentor3.courses_attached += ['Python']

mentor4 = Lecturer('Sofia', 'Williams')
mentor4.courses_attached += ['Python']


''' Реализуем методы проставления оценок.'''

mentor1.rate_st(student1, 'Python', 10)
mentor1.rate_st(student1, 'Kotlin', 9)
mentor1.rate_st(student2, 'Python', 8)
mentor1.rate_st(student2, 'Python', 3)

mentor2.rate_st(student1, 'Python', 3)
mentor2.rate_st(student2, 'Python', 6)

student1.rate_lecturer(mentor3, 'Python', 10)
student1.rate_lecturer(mentor4, 'Python', 5)

student2.rate_lecturer(mentor3, 'Python', 9)
student2.rate_lecturer(mentor4, 'Python', 4)

print(student1)
print(student1.__lt__(student2))
print(student1.__le__(student2))
print(student1.__eq__(student2))
print('---------')
print(student2)
print(student2.__lt__(student1))
print(student2.__le__(student1))
print(student2.__eq__(student1))
print('---------')
print(mentor1)
print('---------')
print(mentor2)
print('---------')
print(mentor3)
print(mentor3.__lt__(mentor4))
print(mentor3.__le__(mentor4))
print(mentor3.__eq__(mentor4))
print('---------')
print(mentor4)
print(mentor4.__lt__(mentor3))
print(mentor4.__le__(mentor3))
print(mentor4.__eq__(mentor3))
print('---------')

list_students = Student.items
def average_rating_st(list_students, course):
    '''
    Рассчитывает среднюю оценку за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов
    принимает список студентов и название курса).
    '''
    list_grades = []
    for student in list_students:
        if course in student.grades:
            list_grades += student.grades[course]
    if not list_grades:
        return 'Ошибка!'
    else:
        result = sum(list_grades) / len(list_grades)
        return result
print(average_rating_st(list_students, 'Python'))
print(average_rating_st(list_students, 'Kotlin'))


list_lecturers = Lecturer.items
def average_rating_lec(list_lecturers, course):
    '''
    Рассчитывает среднюю оценку за лекции всех лекторов в рамках курса (в качестве аргумента принимает список лекторов и
    название курса).
    '''
    list_grades = []
    for lecturer in list_lecturers:
        if course in lecturer.grades:
            list_grades += lecturer.grades[course]
    if not list_grades:
        return 'Ошибка!'
    else:
        result = sum(list_grades) / len(list_grades)
        return result
print(average_rating_lec(list_lecturers, 'Python'))
print(average_rating_lec(list_lecturers, 'Kotlin'))