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
