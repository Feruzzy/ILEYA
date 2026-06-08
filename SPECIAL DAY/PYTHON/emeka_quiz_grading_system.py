num_students = int(input("Enter number of students: "))
num_quizzes = int(input("Enter number of quizzes: "))



scores = []


for index in range(num_students):
    print("--- Student", (index + 1), "---")
    student_scores = []
    
    for counter in range(num_quizzes):
        
        score = float(input("Score for Quiz " + str(counter + 1) + ": "))
        while score < 0 or score > 100:
            print("Invalid score! Must be between 0 and 100.")
            score = float(input("Score for Quiz " + str(counter + 1) + ": "))
            
        student_scores.append(score)
    scores.append(student_scores)
    print()

print("============= QUIZ GRADE REPORT =============")
print("STUDENT\t\tSCORES\t\tAVG")

for index in range(num_students):
    total_score = 0
    
    for score in scores[index]:
        total_score += score
        
    student_avg = total_score / num_quizzes
    print("Student", (index + 1), "\t", scores[index], "\t", student_avg)

print("---------------------------------------------")


best_quiz = 0
highest_avg = 0.0

print("Quiz averages: ", end="")

for counter in range(num_quizzes):
    quiz_total = 0
    
    for index in range(num_students):
        quiz_total += scores[index][counter]
        
    quiz_avg = quiz_total / num_students
    print("QZ" + str(counter + 1) + ":", quiz_avg, "  ", end="")
    
    
    if quiz_avg > highest_avg:
        highest_avg = quiz_avg
        best_quiz = counter + 1

print()
print("Best quiz: Quiz", best_quiz, "(avg", highest_avg, ")")
