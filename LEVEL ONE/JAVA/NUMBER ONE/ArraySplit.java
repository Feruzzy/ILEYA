import java.util.Arrays;


public class ArraySplit {

public static void main(String[] args) {


int [] numbers = {45, 60, 3, 10, 9, 22};

int evenCount = 0;
int oddCount = 0;



for(int number : numbers){
    if(number % 2 == 0){
        evenCount++;
    }
    else{
        oddCount++;
    }
}


int [] even = new int[evenCount];
int [] odd = new int[oddCount];

int evenIndex = 0;
int oddIndex = 0;

for(int number : numbers){
    if(number % 2 == 0){
        even[evenIndex++] = number;
    }
    else{
        odd[oddIndex++] = number;
    }
}

System.out.println("Even Array: " + Arrays.toString(even));
System.out.println("Odd Array: " + Arrays.toString(odd));

}
}
