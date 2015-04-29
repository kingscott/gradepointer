"""
-------------------------------------------------------
Author:  Scott King
Version: 2013-12-25
-------------------------------------------------------
"""
print("""This program uses Wilfrid Laurier University's official grading system.
2015 Wilfrid Laurier University""")
print()


courses = []
lettergs = []
numbers = []
gpa = []
gpt = 0
howmany = int(input("How many courses? ")) 
for x in range(howmany):
    course = input("Please enter a course code and name (code - name): ")
    courses.append(course)
    letterg = input("Please enter a letter grade for course: ").upper()
    lettergs.append(letterg)
    l_conv = {"A+":(12, "90-100"), "A":(11, "85-89"), "A-":(10, "80-84"), "B+":(9, "77-79"), "B":(8, "73-76"), "B-":(7, "70-72"), "C+":(6, "67-69"), "C":(5, "63-66"), "C-":(4, "60-62"), "D+":(3, "57-59"), "D":(2, "53-56"), "D-":(1, "50-52"), "F":(0, "0-49"), "XF":(0, "0-49"), "DR":(0, "0-49")}
    gradep = l_conv[letterg][0]
    gpa.append(gradep)
    grader = l_conv[letterg][1]
    numbers.append(grader)

print()
print("{0:^20}{1:^30}{2:^20}{3:^5}".format("Course Name","Letter Grade","Number Grade", "GP"))
for count in range(howmany):
    print("{0:^20}{1:^30}{2:^20}{3:^5}".format(courses[count], lettergs[count], numbers[count], gpa[count]))  
    print()
    gpt += gpa[count]

print("Your GPA is:", (gpt / howmany).__round__(1))