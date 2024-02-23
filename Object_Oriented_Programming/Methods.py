#Types of Methods
# 3 types - Instance,class,static
# Instance method - two types 1) Accessor method 2) Mutator Method

class Student:

    School = "ABC"  # Class(Static) Variable
    def __init__(self,ma1,ma2,ma3):   #Instance Method
        self.m1 = ma1
        self.m2 = ma2
        self.m3 = ma3
    def average(self):      # Instance Method
        print("Average: ",(self.m1 + self.m2 + self.m3)/3)   

    # Accessor Method (Fetch or Get Method) 
    def get_m1(self):
        return self.m1     
    
    # Mutator Method (Set or Modify)
    def set_m1(self,value):
        self.m1 = value
        return value
    
    # Class Method
    @classmethod
    def get_schoolname(cls):
        return cls.School 
    
    
    # Static Method
    @staticmethod
    def static_info():
        print("This is an example of static method !!!")




s1 = Student(45,63,70)
s2 = Student(67,79,82)
print(Student.get_schoolname())
print(s2.set_m1(69))
print(s1.get_m1())
Student.static_info()
s1.average()
s2.average()
