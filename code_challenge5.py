print("----- FINAL GRADE CALCULATOR -----\n")
print("Please input the following grades: \n")

prelimg=eval(input("Prelim grade: "))
midtermg=eval(input("Midterm grade: "))
semifinalg=eval(input("Semi-final grade: "))
finalsg=eval(input("Finals grade: "))
quizg=eval(input("Quiz grade: "))
projectg=eval(input("Project grade: "))

prelimgc=prelimg * 0.166666667
midtermgc=midtermg * 0.166666667
semifinalgc=semifinalg * 0.166666667
finalsgc=finalsg * 0.166666667
quizgc=quizg * 0.166666667
projectgc=projectg * 0.166666667

fg=prelimgc + midtermgc + semifinalgc + finalsgc + quizgc + projectgc

print(f"The calculated grade from prelim, midterm, semi-finals, finals, quiz, and project is: {round(fg,2)}")
if (fg>=75) :
    print("Congratulations, you have passed the subject!")
    
else :
    print("Sorry, you have failed the subject.")    
