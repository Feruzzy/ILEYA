import java.util.Scanner;

public class GradeCalculations {

    
public static void getScores(double[][] allScores, int numStudents, int numSubjects) {
       
Scanner input = new Scanner(System.in);

for (int count = 0; count < numStudents; count++) {
    System.out.println("Entering score for student " + (count + 1));
            
    for (int counter = 0; counter < numSubjects; counter++) {
    while (true) {
        System.out.print("  Enter score for subject " + (counter + 1) + ": ");
        double score = input.nextDouble();

        if (score >= 0 && score <= 100) {
            allScores[count][counter] = score;
            break;
         } 
        else {
            System.out.println("  Constraint: Score must be between 0 and 100. Try again.");
         }
     }
}
}

System.out.println("Saving...\nSaved successfully\n");
        
        
}

public static void printTableHeader(int numSubjects) {
        System.out.println("=========================================================");
        System.out.print("STUDENT\t\t");
        for (int counter = 0; counter < numSubjects; counter++) {
            System.out.print("SUB" + (counter + 1) + "\t");
        }
        System.out.println("TOT\tAVE\tPOS");
        System.out.println("=========================================================");
    }

public static void printStudentResults(double[][] allScores, int numStudents, int numSubjects) {
double[] totals = new double[numStudents];
double[] averages = new double[numStudents];

for (int count = 0; count < numStudents; count++) {
    double totalScore = 0;
    for (int counter = 0; counter < numSubjects; counter++) {
        totalScore += allScores[count][counter];
     }
     totals[count] = totalScore;
     averages[count] = totalScore / numSubjects;
     }

for (int count = 0; count < numStudents; count++) {
    System.out.print("Student " + (count + 1) + "\t");

    for (int counter = 0; counter < numSubjects; counter++) {
    System.out.print(allScores[count][counter] + "\t");
    }

    int position = 1;
    for (int k = 0; k < numStudents; k++) {
        if (totals[k] > totals[count]) {
            position++;
        }
     }

System.out.printf("%.0f\t%.2f\t%d\n", totals[count], averages[count], position);
}
        System.out.println("=========================================================\n");
}

public static void printSubjectSummary(double[][] allScores, int numStudents, int numSubjects) {
        System.out.println("=========================================================");
        System.out.println("                    SUBJECT SUMMARY                      ");
        System.out.println("=========================================================");

for (int counter = 0; counter < numSubjects; counter++) {
    double highestScore = -1;
    int highestStudent = 0;
    boolean highestTie = false;

    double lowestScore = 101;
    int lowestStudent = 0;
    double totalSubjectScore = 0;
    int passes = 0;
    int fails = 0;

    for (int count = 0; count < numStudents; count++) {
        double currentScore = allScores[count][counter];
        totalSubjectScore += currentScore;

        if (currentScore >= 50) {
            passes++;
        } 
        else {
            fails++;
        }

        if (currentScore > highestScore) {
            highestScore = currentScore;
            highestStudent = count + 1;
            highestTie = false;
        } 
        else if (currentScore == highestScore) {
            highestTie = true;
        }

        if (currentScore < lowestScore) {
            lowestScore = currentScore;
            lowestStudent = count + 1;
        }
        }

    double subjectAvg = totalSubjectScore / numStudents;

    System.out.println("Subject " + (counter + 1));
    if (highestTie) {
        System.out.printf("  Highest scoring student: Same score, no highest scoring student (Score: %.0f)\n", highestScore);
    } 
    else {
        System.out.printf("  Highest scoring student is: Student %d scoring %.0f\n", highestStudent, highestScore);
    }

    System.out.printf("  Lowest scoring student is:  Student %d scoring %.0f\n", lowestStudent, lowestScore);
    System.out.printf("  Total Score is: %.0f\n", totalSubjectScore);
    System.out.printf("  Average score is: %.2f\n", subjectAvg);
    System.out.println("  Number of passes: " + passes);
    System.out.println("  Number of Fails: " + fails);
            System.out.println("---------------------------------------------");
}
}

public static void printClassSummary(double[][] allScores, int numStudents, int numSubjects) {
    int hardestSubject = 1;
    int maxFailures = -1;
    int easiestSubject = 1;
    int maxPasses = -1;

    double overallHighest = -1;
    int highestStudent = 0;
    int highestSubjectNum = 0;

    double overallLowest = 101;
    int lowestStudent = 0;
    int lowestSubjectNum = 0;

    for (int counter = 0; counter < numSubjects; counter++) {
        int passes = 0;
        int failures = 0;
            
        for (int count = 0; count < numStudents; count++) {
            double score = allScores[count][counter];

            if (score > overallHighest) {
                overallHighest = score;
                highestStudent = count + 1;
                highestSubjectNum = counter + 1;
            }
            if (score < overallLowest) {
                overallLowest = score;
                lowestStudent = count + 1;
                lowestSubjectNum = counter + 1;
            }

            if (score >= 50) {
                passes++;
            }
            else {
                failures++;
            }
         }

         if (failures > maxFailures) {
            maxFailures = failures;
            hardestSubject = counter + 1;
         }
         if (passes > maxPasses) {
            maxPasses = passes;
            easiestSubject = counter + 1;
         }
       }

       System.out.println("The hardest subject is Subject " + hardestSubject + " with " + maxFailures + " failures");
        System.out.println("The easiest subject is Subject " + easiestSubject + " with " + maxPasses + " passes");
        System.out.printf("The overall Highest score is scored by Student %d in subject %d scoring %.0f\n", highestStudent, highestSubjectNum, overallHighest);
        System.out.printf("The overall Lowest score is scored by Student %d in subject %d scoring %.0f\n", lowestStudent, lowestSubjectNum, overallLowest);
        System.out.println("=========================================================");

        System.out.println("\nCLASS SUMMARY");
        System.out.println("=========================================================");

    int bestStudent = 0;
    double bestTotal = -1;
    int worstStudent = 0;
    double worstTotal = 999999;
    double classTotalScore = 0;

    for (int count = 0; count < numStudents; count++) {
        double studentTotal = 0;
        for (int counter = 0; counter < numSubjects; counter++) {
            studentTotal += allScores[count][counter];
        }
        classTotalScore += studentTotal;

        if (studentTotal > bestTotal) {
            bestTotal = studentTotal;
            bestStudent = count + 1;
        }

        if (studentTotal < worstTotal) {
            worstTotal = studentTotal;
            worstStudent = count + 1;
        }
     }

        System.out.printf("Best Graduating Student is: Student %d scoring %.0f\n", bestStudent, bestTotal);
        System.out.println("=========================================================");
        System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!I");
        System.out.printf("Worst Graduating Student is: Student %d scoring %.0f\n", worstStudent, worstTotal);
        System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!I\n");

        double classAverageScore = classTotalScore / numStudents;

        System.out.println("=========================================================");
        System.out.printf("Class total score is: %.0f\n", classTotalScore);
        System.out.printf("Class Average score is: %.2f\n", classAverageScore);
        System.out.println("=========================================================");
    }
}
