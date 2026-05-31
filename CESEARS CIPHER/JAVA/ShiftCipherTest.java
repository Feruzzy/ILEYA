import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;


public class ShiftCipherTest {

    @Test
    public void TestTheShiftCipherOnUpperCaseMessage() {
        String message = "HELLO HOW ARE YOU DOING";
        
        String expected = "KHOOR KRZ DUH BRX GRLQJ";

        String actual = ShiftCipher.encryptCaesar(message, 3);

        assertEquals(expected, actual); 
    }


    @Test
    public void TestTheShiftCipherOnLowerCaseMessage() {
        String secondMessage = "the weather is so cold";
        
        String expected = "nby qyunbyl cm mi wifx";
        
        String actual = ShiftCipher.encryptCaesar(secondMessage, 20);
    }


    @Test
    public void TestTheShiftCipherOnEmptyMessage() {
        String thirdMessage = "";
        
        String expected = "";
        
        String actual = ShiftCipher.encryptCaesar(thirdMessage, 20);
        
        assertEquals(expected, actual);
    }
}
