#GENERATOR PROBLEM
#GENERTOR
def perfect_square():
    num = 1
    while num <= 10:
        sq = num*num 
        yield sq 
        num += 1

val = perfect_square()
for i in val:
    print(i)
#Create with own
def odd_numbers():
    n = 1
    while n <= 10:
        odd = n%2 != 0
        yield odd 
        n+=1
o1 = odd_numbers()
for i in o1:
    print(i)
