def calculateGrade(students_marks):
    grade = []
    for x in range(0,len(students_marks)):
        avg = (sum(students_marks[x]))//len(students_marks[x])
        print(avg)
        if(avg >= 90):
            grade.append('A+')
        elif avg in range(80,90):
            grade.append('A')
        elif avg in range(70,80):
            grade.append('B')
        elif avg in range(60,70):
            grade.append('C')
        elif avg in range(50,60):
            grade.append('D')
        elif (avg < 50):
            grade.append('F')
    return grade