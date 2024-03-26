
classroom ={
    "Nischal": 90,
    "Swarna" : 95,
    "Namratha" : 93
}

#Append more students in Classroom

classroom["Julie"] = 92
classroom["Kate"] = 91
print(classroom)

#Iterate Students in classroom

for names,marks in classroom.items():
    print("The student is %s and grade is %d" % (names,marks))

#Delete Kate and Instead add "Jack" with 92 marks

del classroom["Kate"] 
classroom["Jack"] = 92
print(classroom)
