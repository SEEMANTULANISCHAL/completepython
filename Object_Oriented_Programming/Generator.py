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