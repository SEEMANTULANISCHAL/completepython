x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
z=int(input("Enter Third Number: "))
n=int(input("Enter n Number: "))
output=[]
list=[]
for x in range(x+1):
    for y in range(y+1):
        for z in range(z+1):
            if x+y+z != n:
                list=[x,y,z]
                output.append(list)
print(output)
