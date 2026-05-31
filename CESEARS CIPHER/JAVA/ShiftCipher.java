public class ShiftCipher {

public static String encryptCaesar(String message, int shift) {

String lowerAlphabet = "abcdefghijklmnopqrstuvwxyz";
String upperAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
String encrypted = "";

for (int i = 0; i < message.length(); i++) {
    char letter = message.charAt(i);

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
