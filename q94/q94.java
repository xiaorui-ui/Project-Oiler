import java.math.BigDecimal;
import java.math.MathContext;
import java.util.stream.Stream;

// apparently a faster way is to consider the height of the triangle...
// also 

public class q94 {
    public long peri_sum(int i) {
        long count = 0;
            int p1 = 3*i + 1;
            boolean b1 = new BigDecimal(i - 1).multiply(new BigDecimal(p1)).sqrt(new MathContext(25))
            .remainder(new BigDecimal(1)).equals(new BigDecimal(0));
            if (b1) {count += p1;}
            int p2 = 3*i - 1;
            boolean b2 = new BigDecimal(i + 1).multiply(new BigDecimal(p2)).sqrt(new MathContext(25))
            .remainder(new BigDecimal(1)).equals(new BigDecimal(0));
            if (b2) {count += p2;}        
        return count;
    }
    // ~ 420 seconds
    // public static void main(String[] args) {
    //     long start = System.nanoTime();
    //     q94 q = new q94();
    //     // 166_666_666 odd numbers from 3 to 333_333_333
    //     System.out.println(Stream.iterate(3, x -> x + 2).parallel().limit(166_666_666).map(x -> q.peri_sum(x))
    //     .reduce((long) 0, (x, y) -> x + y));
    //     long end = System.nanoTime();
    //     System.out.println((end - start)*Math.pow(10, -9));
    // }

    // also BigDecimal was avoidable :(
    // ~ 2.4s !!!
    public static void main(String[] args) {

        long perimeter_sum = 0;

        long start = System.nanoTime();

        for (long a = 3; 3 * a - 1 <= 1000000000; a+=2) {
            long test1 = 3 * a * a - 2 * a - 1;
            long test2 = test1 + 4 * a;  //a bit faster getting the 2nd polynomial this way
            long test1root = (long) Math.sqrt(test1);
            long test2root = (long) Math.sqrt(test2);
            if (test1root * test1root == test1)
                perimeter_sum += (3 * a + 1);
            if (test2root * test2root == test2)
                perimeter_sum += (3 * a - 1);
        }

        System.out.println("Found this sum, good luck: " + perimeter_sum);
        long end = System.nanoTime();
        System.out.println((end - start)*Math.pow(10, -9));
    }
}



