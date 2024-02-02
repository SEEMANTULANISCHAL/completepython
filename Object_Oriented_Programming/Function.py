class Nischal:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def details(self):
        return self.m1, self.m2
d1 = Nischal(20,30)
d2 = Nischal(30,40)
print(d1.details())

