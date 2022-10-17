import java.util.HashSet;
import java.util.Scanner;

public class 나머지_3052 {
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);
        HashSet<Integer> remain = new HashSet<Integer>(); // set 선언

        for (int i=0; i < 10; i++){
            n = sc.nextInt();

            remain.add(n % 42); // set은 중복을 허용하지 않는다.
        }
        System.out.println(remain.size());
    }
}
