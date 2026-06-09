import grade_function

def main():

    num_students = int(input("How many students do you have? "))
    num_subjects = int(input("How many subjects do they offer? "))

   
    grade_database = grade_function.get_scores(num_students, num_subjects)

    
    grade_function.print_table_header(num_subjects)

    
    student_totals, student_averages = grade_function.calculate_totals_and_averages(
        grade_database, num_students, num_subjects
    )

    
    grade_function.student_results(
        grade_database, student_totals, student_averages, num_students, num_subjects
    )

    
    grade_function.subject_summary(grade_database, num_students, num_subjects)

    grade_function.class_summary(grade_database, num_students, num_subjects)




main()
