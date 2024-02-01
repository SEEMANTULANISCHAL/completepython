#loops
#3. Break Statement Candy machine problem
x = int(input("Enter number of candies:"))
av = 10
c=1
while c<=x:
    if c > av:
        break
    print("candies")
    c+=1

#4. Continue Statement print number of odd number upto 10
for i in range(1,11):
    if i%2==0:
        continue
    print(i)