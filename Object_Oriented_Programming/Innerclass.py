class Robot:
    def __init__(self,n,c,w):
        self.name = n
        self.color = c
        self.weight = w
    def introduce_self(self):
        print(self.name, self.color, self.weight) 
    class Person:
        def __init__(self,name,personality,issitting,robotowned):
            self.name = name
            self.personality = personality
            self.issitting = issitting
            self.robotowned = robotowned
        def sitdown(self):
            self.issitting = True 
        
        def standup(self):
            self.issitting = False
            
        def robot_owned(self):
            return self.robotowned 

            



r1 =Robot("Tom","Red",30)
r2 =Robot("Jerry","Blue",40)

p1 = Robot.Person("Allice", "Agressive", False,r2)
p2 = Robot.Person("Becky","Talkative",True,r1)

print(p1.robot_owned())

r1.introduce_self()
r2.introduce_self()
