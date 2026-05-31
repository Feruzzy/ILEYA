import java.util.Scanner;

public class CheckOutApp {
    
public static void main(String[] args) {
        
Scanner input = new Scanner(System.in);

        
System.out.print("What is the customer's Name: ");
String customerName = input.nextLine();

        
String[] items = new String[100];

int[] quantities = new int[100];
double[] prices = new double[100];
int itemCount = 0;

       
while (true) {
    System.out.print("What did the user buy? ");
    items[itemCount] = input.nextLine();

    System.out.print("How many pieces? ");
    quantities[itemCount] = input.nextInt();

    System.out.print("How much per unit? ");
    prices[itemCount] = input.nextDouble();
    input.nextLine();
    itemCount++;

    System.out.print("Add more Items? (yes/no): ");
    String choice = input.nextLine();
    if (choice.equalsIgnoreCase("no")) {
    break;
    }
    }

    System.out.print("What is your name? ");
    String cashierName = input.nextLine();

    System.out.print("How much discount will he get (in %)? ");
    double discountPercent = input.nextDouble();

        
    System.out.println("\n--- INVOICE ---");
    System.out.println("Customer: " + customerName);
    System.out.println("Cashier: " + cashierName);
       
    double subTotal = 0;
    for (int item = 0; item < itemCount; item++) {
        double itemTotal = quantities[item] * prices[item];
        subTotal = subTotal + itemTotal;
        System.out.println(items[item] + " x " + quantities[item] + " = " + itemTotal);
    }

        
    double discountAmount = (discountPercent / 100) * subTotal;
    double vatAmount = (17.5 / 100) * subTotal;
    double billTotal = subTotal - discountAmount + vatAmount;

    System.out.println("Sub Total: " + subTotal);
    System.out.println("Discount: " + discountAmount);
    System.out.println("VAT: " + vatAmount);
    System.out.println("Bill Total: " + billTotal);
    System.out.println("KINDLY PAY: " + billTotal);

        
    System.out.print("\nHow much did the customer give to you? ");
    double amountPaid = input.nextDouble();
    double balance = amountPaid - billTotal;

    System.out.println("\n--- FINAL RECEIPT ---");
    System.out.println("Bill Total: " + billTotal);
    System.out.println("Amount Paid: " + amountPaid);
    System.out.println("Balance: " + balance);
    System.out.println("THANK YOU!");
       
       
}
}
