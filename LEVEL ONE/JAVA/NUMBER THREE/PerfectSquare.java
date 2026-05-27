import java.util.Arrays; 

public class PerfectSquare{

public static int [] getPerfectSquares(int [] numbers){

int count = 0;

for(int number : numbers){
    if(number >= 0){
        int root = (int) Math.sqrt(number);
        if(root * root == number){
            count++;
        }
    }
}


int [] perfectSquares = new int[count];

int index = 0;

for(int number : numbers){
    if(number >= 0){
        int root = (int) Math.sqrt(number);
        if(root * root == number){
            perfectSquares[index++] = number;
        }
    }
}

return perfectSquares;

}



public static void main(String[] args){

int [] numbers = {4, 7, 9, 10, 16, 18};

int [] result = getPerfectSquares(numbers);

System.out.println("Perfect Squares: " + Arrays.toString(result));
    
}
}

