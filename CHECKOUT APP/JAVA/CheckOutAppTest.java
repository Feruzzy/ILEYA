import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class CheckOutAppTest {

    @Test
    public void testBillTotalWithoutDiscount() {

        double subTotal = 10000;
        double discountPercent = 0;

        double discountAmount = (discountPercent / 100) * subTotal;
        double vatAmount = (17.5 / 100) * subTotal;
        double billTotal = subTotal - discountAmount + vatAmount;

        assertEquals(11750.0, billTotal);
    }

    @Test
    public void testBillTotalWithTenPercentDiscount() {

        double subTotal = 10000;
        double discountPercent = 10;

        double discountAmount = (discountPercent / 100) * subTotal;
        double vatAmount = (17.5 / 100) * subTotal;
        double billTotal = subTotal - discountAmount + vatAmount;

        assertEquals(10750.0, billTotal);
    }

    @Test
    public void testBillTotalWithTwentyPercentDiscount() {

        double subTotal = 20000;
        double discountPercent = 20;

        double discountAmount = (discountPercent / 100) * subTotal;
        double vatAmount = (17.5 / 100) * subTotal;
        double billTotal = subTotal - discountAmount + vatAmount;

        assertEquals(19500.0, billTotal);
    }

    @Test
    public void testBalanceWhenCustomerPaysMore() {

        double billTotal = 11750;
        double amountPaid = 15000;
        double balance = amountPaid - billTotal;

        assertEquals(3250.0, balance);
    }

    @Test
    public void testBalanceWhenCustomerPaysExactAmount() {

        double billTotal = 11750;
        double amountPaid = 11750;
        double balance = amountPaid - billTotal;

        assertEquals(0.0, balance);
    }
}
