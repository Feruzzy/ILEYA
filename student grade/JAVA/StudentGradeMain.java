import java.util.Scanner;

public class StudentGradeMain {

public static void main(String[] args) {
Scanner input = new Scanner(System.in);

        
        System.out.print("Enter number of students: ");
        int numStudents = mainScanner.nextInt();
        System.out.print("Enter number of subjects: ");
        int numSubjects = mainScanner.nextInt();
        System.out.println();

        
        double[][] allScores = new double[numStudents][numSubjects];

      
        GradeCalculations.getScores(allScores, numStudents, numSubjects);
        GradeCalculations.printTableHeader(numSubjects);
        GradeCalculations.printStudentResults(allScores, numStudents, numSubjects);
        GradeCalculations.printSubjectSummary(allScores, numStudents, numSubjects);
        GradeCalculations.printClassSummary(allScores, numStudents, numSubjects);

       
        input.close();
    }
}
