#Problem 8
n=int(input())
student_mark ={}
for i in range(n):
    name, *line = input().split()
    mark = list(map(float,line))
    student_mark[name] = mark
selected_name = input()
l1 = list(student_mark[selected_name])
avg = sum(l1)/3
print("%0.2f" %(avg))
