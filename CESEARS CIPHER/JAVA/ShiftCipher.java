public class ShiftCipher {

public static String encryptCaesar(String message, int shift) {

String lowerAlphabet = "abcdefghijklmnopqrstuvwxyz";
String upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
String encrypted = "";

for (int count = 0; count < message.length(); count++) {
    char letter = message.charAt(count);

    if (Character.isLowerCase(letter)) {
        int position = lowerAlphabet.indexOf(letter);

        int newPosition = (position + shift) % 26;
        encrypted = encrypted + lowerAlphabet.charAt(newPosition);
    

    } 
    else if(Character.isUpperCase(letter)) {
        int position = upperAlphabet.indexOf(letter);

        int newPosition = (position + shift) % 26;
        encrypted = encrypted + upperAlphabet.charAt(newPosition);
    } 
    else {

        encrypted = encrypted + letter;
    }
    }

    return encrypted;
}

public static void main(String[] args) {

String result = encryptCaesar("the weather is so cold", 20);

System.out.println(result);
}
}
