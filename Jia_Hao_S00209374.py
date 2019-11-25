def menu():
    allStudentsMarks = {}
    while True:
        kbinput = input ("Enter 1 to store student details\n" +
                    "Enter 2 to display student report\n" +
                    "Enter any other key to exit\n")
        if kbinput == '1':
            allStudentsMarks = StudentsMarks(allStudentsMarks)
        elif kbinput == '2':
            displayAllReports (allStudentsMarks)
        elif kbinput != '1' and kbinput != '2':
            break

def StudentsMarks(allStudentsMarks):
    while True:
        while True:
            StudentName = input('What is the student name?')
            if searchStudentMarks(StudentName,allStudentsMarks):
                print(StudentName,"already exist in system.\n")
            else:
                break

        while True:
             # Df valid mark range : 0 - 20
            dfReportMarks = input("Enter student's DF report marks\n")
            dfReportMarks = float(dfReportMarks)
            if dfReportMarks >= 0 and dfReportMarks <= 20:
                break

             # Project valid marks range : 0 - 30
        while True:
            projectMarks = input ("Enter student's project marks\n")
            projectMarks = float(projectMarks)
            if projectMarks >=0 and projectMarks<=30:
                break

              # Final exam valid marks range : 0 - 50
        while True:
            finalExamMarks = input("Enter student's Final Exam marks\n")
            finalExamMarks = float(finalExamMarks)
            if finalExamMarks >= 0 and finalExamMarks <= 50:
                break
        studentMarks = [dfReportMarks, projectMarks, finalExamMarks]
        allStudentsMarks[StudentName] = studentMarks
        #for k, v in allStudentsMarks.items():
           # print ("Student ", k, "'s marks are \n")
            #for m in v:
             #   print(m, "\t")

        print(StudentName,"\t","DF=",dfReportMarks,"\t","Project=",projectMarks,"\t","Final Exam=",finalExamMarks,"\t""Total=",sum([dfReportMarks,projectMarks,finalExamMarks]))
        kbinput = input("Do you want to add another student's details (y/n)")
        if kbinput == "n":
            break

    return allStudentsMarks



def displayAllReports (allStudentsMarks):
    sumDF = 0
    sumProj = 0
    sumFinal = 0
    count = len(allStudentsMarks.keys())

#average of each reports
    for key in allStudentsMarks:
        sumDF += allStudentsMarks[key][0]
        sumProj += allStudentsMarks[key][1]
        sumFinal += allStudentsMarks[key][2]
    averageDf = sumDF/count
    averageproject = sumProj/count
    averagefinal = sumFinal/count
    averagetotal = (sumDF + sumProj + sumFinal)/count


    kbinput = input("Enter 1 for students who's below average DF Marks\n" +
                    "Enter 2 for students who's below average Project Marks\n" +
                    "Enter 3 for students who's below average Final Exam Marks\n" +
                    "Enter 4 for students who's below average Overall Marks\n" +
                    "Enter 5 for All student's marks")
    if kbinput =="1":
       # print(sumDF/count)
        for key in allStudentsMarks:
            student = allStudentsMarks[key]
            if student [0] < averageDf:

                printReport(key,student[0],student[1],student[2])


    elif kbinput =="2":
        for key in allStudentsMarks:
            student = allStudentsMarks[key]
            if student[0] < averageproject:
                printReport(key, student[0], student[1], student[2])


    elif kbinput =="3":
        for key in allStudentsMarks:
            student = allStudentsMarks[key]
            if student[0] < averagefinal:
                printReport(key, student[0], student[1], student[2])

    elif kbinput =="4":
        for key in allStudentsMarks:
            student = allStudentsMarks[key]
            if student[0] < averagetotal:
                printReport(key, student[0], student[1], student[2])

    elif kbinput =="5":
        for key in allStudentsMarks:
            student = allStudentsMarks[key]
            printReport(key, student[0], student[1], student[2])


#
def printReport(studentName,dfReportMarks,projectMarks,finalExamMarks):
    print(studentName, "\t", "DF=", dfReportMarks, "\t", "Project=", projectMarks, "\t", "Final Exam=", finalExamMarks,
          "\t""Total=", sum([dfReportMarks, projectMarks, finalExamMarks]))

def AnotherStudent(allStudentsMarks):

    while True:
        kbinput = input ("Do you want to add another student's details (y/n)")
        if kbinput =="y":
            allStudentsMarks = StudentsMarks(allStudentsMarks)
        elif kbinput =="n":
            break
    while kbinput =="y":
        kbinput = input ("Do you want to add another student's details (y/n)")

    while kbinput =="n":
            break
    return allStudentsMarks

def searchStudentMarks(newNameofStudent,allStudentStorage):
    return newNameofStudent in allStudentStorage

menu()