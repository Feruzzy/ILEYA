def get_scores(num_students, num_subjects):
  
    all_scores = []
    
    for count in range(num_students):
        print(f"Entering score for student {count + 1}")
        student_scores = [] 
        
        for subject_num in range(1, num_subjects + 1):
            while True:
                score = float(input(f"  Enter score for subject {subject_num}: "))
                if score >= 0 and score <= 100:
                    student_scores.append(score)
                    break
                else:
                    print("  Constraint: Score must be between 0 and 100. Try again.")
                    
        all_scores.append(student_scores)
        
    print("Saving...")
    print("Saved successfully\n")
    return all_scores


def print_table_header(num_subjects):
    
    print("=========================================================")
    print("STUDENT\t\t", end="")
    for counter in range(num_subjects):
        print(f"SUB{counter+1}\t", end="")
    print("TOT\tAVE\tPOS")
    print("=========================================================")


def calculate_totals_and_averages(all_scores, num_students, num_subjects):
   
    totals = []
    averages = []
    for count in range(num_students):
        total_score = sum(all_scores[count])
        totals.append(total_score)
        averages.append(total_score / num_subjects)
    return totals, averages


def student_results(all_scores, totals, averages, num_students, num_subjects):
    
    for count in range(num_students):
        print(f"Student {count+1}\t", end="")
        
        for counter in range(num_subjects):
            print(f"{all_scores[count][counter]}\t", end="")
            
        
        position = 1
        for other_total in totals:
            if other_total > totals[count]:
                position += 1
                
        print(f"{totals[count]:.0f}\t{averages[count]:.2f}\t{position}")
    print("=========================================================\n")


def subject_summary(all_scores, num_students, num_subjects):

    print("=========================================================")
    print("                    SUBJECT SUMMARY                      ")
    print("=========================================================")

    for counter in range(num_subjects):
        highest_score = -1
        highest_student = 0
        highest_tie = False  
        
        lowest_score = 101
        lowest_student = 0
        total_subject_score = 0
        passes = 0
        fails = 0
        
        for count in range(num_students):
            current_score = all_scores[count][counter]
            total_subject_score += current_score
                
            if current_score >= 50:
                passes += 1
            else:
                fails += 1
                    
            if current_score > highest_score:
                highest_score = current_score
                highest_student = count + 1
                highest_tie = False  
            elif current_score == highest_score:
                highest_tie = True   
                    
            if current_score < lowest_score:
                lowest_score = current_score
                lowest_student = count + 1
                    
        subject_avg = total_subject_score / num_students
        
        print(f"Subject {counter+1}")
        if highest_tie:
            print(f"  Highest scoring student: Same score, no highest scoring student (Score: {highest_score:.0f})")
        else:
            print(f"  Highest scoring student is: Student {highest_student} scoring {highest_score:.0f}")
            
        print(f"  Lowest scoring student is:  Student {lowest_student} scoring {lowest_score:.0f}")
        print(f"  Total Score is: {total_subject_score:.0f}")
        print(f"  Average score is: {subject_avg:.2f}")
        print(f"  Number of passes: {passes}")
        print(f"  Number of Fails: {fails}")
        print("---------------------------------------------")
