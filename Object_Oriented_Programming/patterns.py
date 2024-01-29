#Type sof pattern
#1. Print Pattern 4X4 # using while loop
i=1
while i<=4:
    print("# ", end="")
    j = 1
    while j<=3:
        print("# ", end="")
        j+=1
    i+=1
    print()

#2.  Print Pattern 4X4 # using for loop
for j in range(4):
    for i in range(4):
        print("# ", end="")
    print()

#3. print pattern 1X4 # usinf for loop
for i in range(4):
    for j in range(i+1):
        print("# ",end="")
    print()    
#3. print pattern 4X1 # usinf for loop
    
for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()    


#4. print 4x1 using numbers 
for i in range(4):
    for j in range(1,5-i):
        print(j, end="")
    print()
