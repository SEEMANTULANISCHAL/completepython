n = int(input("Enter n number: "))
x = list(map(int,input("Enter your list:").split()))
x1 = set(x)
x2 = sorted(x1)
print(x2[-2])