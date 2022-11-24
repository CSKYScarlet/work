import java.util.*;

public class test1 {
    public static void main(String arg[]) {
        // 3개의 int 정수를 입력 받아 평균 값을 실수로 출력하라.
        // scan
        Scanner scan = new Scanner(System.in);

        int a = 0;
        int b = 0;
        int c = 0;

        a = scan.nextInt();
        b = scan.nextInt();
        c = scan.nextInt();

        float avg = (a + b + c) / 3.0f;

        // println
        System.out.println(avg);
    }
}
