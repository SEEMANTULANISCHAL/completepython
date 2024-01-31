# Types of Variables in OOPS
class Vehicles:
    wheel = 4          # Class Variables
    def __init__(self,):      
        self.mil = 10         #Instance Variables
        self.name = "BMW"
    
    


v1 = Vehicles()
v2 = Vehicles()   
v3 = Vehicles() 
Vehicles.wheel = 6 
v1.mil = 8            #Instance Variables
v1.name ="Audi"
print(v1.mil,v1.name,Vehicles.wheel)
print(v2.mil,v2.name,Vehicles.wheel)

