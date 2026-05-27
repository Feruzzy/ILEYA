import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class PerfectSquareTest{

    @Test
    public void TestThatThereIsPerfectSquares() {
        int [] numbers = {4, 7, 9, 10, 16, 18};

        int [] expected = {4, 9, 16};

        
        int [] actual = PerfectSquare.getPerfectSquares(numbers);

        
        assertArrayEquals(expected, actual, "The perfect squares is seperated");
    }

    @Test
    public void TestThatThereIsNoPerfectSqares() {
        int [] numbers = {5, 7, 13, 10, 19, 18};

        int [] expected = {};

        
        int [] actual = PerfectSquare.getPerfectSquares(numbers);

        
        assertArrayEquals(expected, actual, "There is no perfect square");
    }


}
