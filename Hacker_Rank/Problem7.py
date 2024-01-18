#Nested List
records=[]
list_name=[]
list_grade=[]
for i in range(int(input("Enter the number:"))):
    name = input()
    grade = float(input())
    records.append([name,grade])
    list_grade.append(grade)
set_grade=list(set(list_grade))
set_grade.sort()
second_least = set_grade[1]
#LIST COMPREHENSION
ouput=[i[0] for i in records if i[1] == second_least]
ouput.sort()
for x in ouput:
    print(x)
