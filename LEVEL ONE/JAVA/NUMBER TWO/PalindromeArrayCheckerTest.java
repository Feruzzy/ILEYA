import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class PalindromeArrayCheckerTest{


    @Test
    public void TestThatMyArrayIsPalindrome(){
        int [] myNumbers = {45, 0, 8, 0, 45};
        boolean expected = true;
        boolean actual = PalindromeArrayChecker.checkingPalindrome(myNumbers);
        assertEquals(expected, actual, "The array is palindrome");
    }


    @Test
    public void TestThatTestArrayIsNotPalindrome(){
        int [] testArray = {1, 44, 9, 0};
        boolean expected = false;
        boolean actual = PalindromeArrayChecker.checkingPalindrome(testArray);
        assertEquals(expected, actual, "The array is not palindrome");
    }

    @Test
    public void TestThatNegativeArrayIsPalindrome(){
        int [] negativeArray = {-5, -12, -5};
        boolean expected = true;
        boolean actual = PalindromeArrayChecker.checkingPalindrome(negativeArray);
        assertEquals(expected, actual, "The array is palindrome");
    }
    
}

