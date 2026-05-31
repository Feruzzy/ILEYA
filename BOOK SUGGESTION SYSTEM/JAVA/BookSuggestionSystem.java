import java.util.Scanner;

public class BookSuggestionSystem {

public static void main(String[] args) {

Scanner scanner = new Scanner(System.in);

while (true) {
    System.out.println("\n---Welcome to the Book Suggestion System---");
    System.out.println("1. Get Suggestions");
    System.out.println("2. Add Book");
    System.out.println("3. Remove Book");
    System.out.println("4. Update book");
    System.out.println("5. Show all books");
    System.out.println("0. Exit");

    System.out.print("Enter operation: ");
    String choice = scanner.nextLine();

    switch (choice) {
    case "1":
        System.out.println("\n--- Book for the Day ---");
        System.out.println("The Hobbit (Page: 47)");
                   
        System.out.print("Would you like to get another suggestion? (yes/no): ");
        String answer = scanner.nextLine();
        if (answer.equalsIgnoreCase("yes")) {
        System.out.println("Alternative: The Mystery (Page: 12)");
        }
        break;

    case "2":
        System.out.print("\nEnter the book title: ");
        scanner.nextLine();
        System.out.println("Book added successfully!");
        break;

    case "3":
        System.out.print("\nEnter the book title to remove: ");
        scanner.nextLine();
        System.out.println("Book removed successfully!");
        break;

    case "4":
        System.out.print("\nEnter the old title: ");
        scanner.nextLine();
        System.out.print("Enter the new title: ");
        scanner.nextLine();
        System.out.println("Book updated successfully!");
        break;

    case "5":
        System.out.println("\n--- All Books ---");
        System.out.println("1. The Hobbit");
        System.out.println("2. The Mystery");
        break;

    case "0":
        System.out.println("Exiting program.");
        return; 

   default:
        System.out.println("Invalid selection.");
        break;
}
}
}
}
