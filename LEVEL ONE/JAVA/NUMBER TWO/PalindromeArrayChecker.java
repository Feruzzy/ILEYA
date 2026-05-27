public class PalindromeArrayChecker{
 
public static boolean checkingPalindrome(int [] myNumbers){

int start = 0;
int end = myNumbers.length - 1;

while(start < end){
    if(myNumbers[start] != myNumbers[end]){
        return false;
    }
    start++;
    end--;
}

return true;


}

public static void main(String[] args){

int [] myNumbers = {45, 0, 8, 0, 45};

boolean result = checkingPalindrome(myNumbers);

System.out.println("Result: " + result);

}
}



