import java.util.Scanner;

public class EmekaQuizGradingSystem {

public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);

        
System.out.print("Enter number of students: ");
int numStudents = scanner.nextInt();
        
System.out.print("Enter number of quizzes: ");
int numQuizzes = scanner.nextInt();
System.out.println();

        
double[][] scores = new double[numStudents][numQuizzes];

        
for (int count = 0; count < numStudents; count++) {
    System.out.println("--- Student " + (count + 1) + " ---");
for (int counter = 0; counter < numQuizzes; counter++) {
                
    System.out.print("Score for Quiz " + (counter + 1) + ": ");
    double score = scanner.nextDouble();
                
                
while (score < 0 || score > 100) {
    System.out.println("Invalid score! Must be between 0 and 100.");
    System.out.print("Score for Quiz " + (counter + 1) + ": ");
    score = scanner.nextDouble();
    }
    scores[count][counter] = score;
    }
    System.out.println();
    }


System.out.println("============= QUIZ GRADE REPORT =============");
        
        
for (int count = 0; count < numStudents; count++) {
    System.out.print("Student " + (count + 1) + ": \t");
    double studentSum = 0;
            

for (int counter = 0; counter < numQuizzes; counter++) {
    System.out.print(scores[count][counter] + "\t");
    studentSum += scores[count][counter];
    }
            
    double studentAvg = studentSum / numQuizzes;
    System.out.println(" | Avg: " + studentAvg);
    }

System.out.println("---------------------------------------------");

      
int bestQuizNum = 1;
double highestQuizAvg = 0.0;

System.out.print("Quiz averages: ");
        
for (int counter = 0; counter < numQuizzes; counter++) {
    double quizSum = 0;
            

for (int count = 0; count < numStudents; count++) {
    quizSum += scores[count][counter];
    }
            
    double quizAvg = quizSum / numStudents;
    System.out.print("QZ" + (counter + 1) + ": " + quizAvg + "   ");
            
    if (quizAvg > highestQuizAvg) {
    highestQuizAvg = quizAvg;
    bestQuizNum = counter + 1;
    }
    }
        
    System.out.println();
    System.out.println("Best quiz: Quiz " + bestQuizNum + " (avg " + highestQuizAvg + ")");
        
      
    }
}
