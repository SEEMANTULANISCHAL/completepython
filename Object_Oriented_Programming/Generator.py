


def odd_numbers():
    n = 1
    while n <= 10:
        odd = n%2 != 0
        yield odd
        n+=1
o1 = odd_numbers()
for i in o1:
    print(i)
