def get_scores(num_students, num_subjects):
  
    all_scores = []
    
    for count in range(num_students):
        print(f"Entering score for student {count + 1}")
        student_scores = [] 
        
        for subject_num in range(1, num_subjects + 1):
            while True:
                score = float(input(f"  Enter score for subje {subject_num}: "))
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
            print(f"  Highest scoring student: Same score, no highest scoring student (Score: {highest_score})")
        else:
            print(f"  Highest scoring student is: Student {highest_student} scoring {highest_score}")
            
        print(f"  Lowest scoring student is:  Student {lowest_student} scoring {lowest_score:.0f}")
        print(f"  Total Score is: {total_subject_score}")
        print(f"  Average score is: {subject_avg:.2f}")
        print(f"  Number of passes: {passes}")
        print(f"  Number of Fails: {fails}")
        print("---------------------------------------------")



def class_summary(all_scores, num_students, num_subjects):
    hardest_subject = 1
    max_failures = -1
    easiest_subject = 1
    max_passes = -1
    
    overall_highest = -1
    highest_student = 0
    highest_subject_num = 0
    
    overall_lowest = 101
    lowest_student = 0
    lowest_subject_num = 0

    
    for sub_idx in range(num_subjects):
        passes = 0
        failures = 0
        for stud_idx in range(num_students):
            score = all_scores[stud_idx][sub_idx]
            
            
            if score > overall_highest:
                overall_highest = score
                highest_student = stud_idx + 1
                highest_subject_num = sub_idx + 1
            if score < overall_lowest:
                overall_lowest = score
                lowest_student = stud_idx + 1
                lowest_subject_num = sub_idx + 1
                
            if score >= 50:
                passes += 1
            else:
                failures += 1
                
        if failures > max_failures:
            max_failures = failures
            hardest_subject = sub_idx + 1
        if passes > max_passes:
            max_passes = passes
            easiest_subject = sub_idx + 1

    
    print(f"The hardest subject is Subject {hardest_subject} with {max_failures} failures")
    print(f"The easiest subject is Subject {easiest_subject} with {max_passes} passes")
    print(f"The overall Highest score is scored by Student {highest_student} in subject {highest_subject_num} scoring {overall_highest}")
    print(f"The overall Lowest score is scored by Student {lowest_student} in subject {lowest_subject_num} scoring {overall_lowest}")
    print("=========================================================")
    
    print("\nCLASS SUMMARY")
    print("=========================================================")
    
    best_student = 0
    best_total = -1
    worst_student = 0
    worst_total = float('inf')
    class_total_score = 0
    
    
    for stud_idx in range(num_students):
        student_total = sum(all_scores[stud_idx])
        class_total_score += student_total
        
        if student_total > best_total:
            best_total = student_total
            best_student = stud_idx + 1
            
        if student_total < worst_total:
            worst_total = student_total
            worst_student = stud_idx + 1
            
    print(f"Best Graduating Student is: Student {best_student} scoring {best_total}")
    print("=========================================================")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!I")
    print(f"Worst Graduating Student is: Student {worst_student} scoring {worst_total}")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!I\n")
    
    class_average_score = class_total_score / num_students
    
    print("=========================================================")
    print(f"Class total score is: {class_total_score}")
    print(f"Class Average score is: {class_average_score:.2f}")
    print("=========================================================")
