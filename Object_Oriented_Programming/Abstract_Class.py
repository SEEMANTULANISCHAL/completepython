from abc import ABC, abstractmethod

class School(ABC):
    @abstractmethod
    def students(self):
        pass      #Abstract Method

class Classroom(School):
    def students(self):
        print("Students in Classroom")



class Staff:
    def teachers(self,teach):
        print("Teach students")
        teach.students()
        



c1 = Classroom()

s1 = Staff()
s1.teachers(c1)