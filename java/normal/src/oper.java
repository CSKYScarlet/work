import java.util.*;

public class oper {
    public static void main(String args[]) {
        // 키보드로부터 정수를 입력받아 아래 조건을 만족하면 "참" 출력,
        // 아니면 거짓
        // 입력값 참 조건 : 4이상 10미만

        Scanner scan = new Scanner(System.in);

        int input = scan.nextInt();
        if (100 >= input && 90 <= input) {
            System.out.println("A");
        } else if (90 > input && 80 <= input) {
            System.out.println("B");
        } else if (80 > input && 70 <= input) {
            System.out.println("C");
        } else if (70 > input && 60 <= input) {
            System.out.println("D");
        } else if (60 > input) {
            System.out.println("F");
        } else {
            System.out.println("잘못된 입력 값");
        }
    }
}