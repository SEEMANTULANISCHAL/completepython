class A:
    def __init__(self):
        print("In A __init__")
    def feature1(self):
        print("feature1")
    def feature2(self):
        print("feature2")
        
class B:
    def __init__(self): 
        super().__init__()
        print("In B __init__")
    def feature3(self):
        print("feature3")
    def feature2(self):
        print("feature4")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C __init__")
    def feat(self):
        super().feature2()

a1 = C() 
a1.feat()

        