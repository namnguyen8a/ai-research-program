class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = list()
    
    def add_grade(self, grade):
        self.__grades.append(grade)
        return None
    
    def get_average_grade(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

student = Student("Jane Smith")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
print(student.get_average_grade())