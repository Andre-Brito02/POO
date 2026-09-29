class Student:
    def __init__(self, name:str, grade1:float, grade2:float, grade3:float):
        self._name = name
        self._grade1 = grade1
        self._grade2 = grade2
        self._grade3 = grade3

    def final_grade(self):
        return self._grade1+ self._grade2+ self._grade3

    def result(self):
        return 'PASS' if self.final_grade() >= 60.0 else f'FAILED\nMISSING {60.0-self.final_grade():.2f} POINTS'

    def __str__(self):
        return f'FINAL GRADE = {self.final_grade():.2f}\n{self.result()}'

name = input("Name: ")
grade1 = float(input("Grade 1: "))
grade2 = float(input("Grade 2: "))
grade3 = float(input("Grade 3: "))
std = Student(name, grade1, grade2, grade3)

print(std)