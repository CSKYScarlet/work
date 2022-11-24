import java.util.*;

public class value {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        String msg = "";
        int count = 1;

        while(true) {
            // 키보드로 부터 정수 값 입력 받기
            int input = scan.nextInt();
            // 입력 값에 따라 짝수 홀수 출력
            if (input >= 1 && input != 20000) {
                System.out.print(count++);
                System.out.print("번째 입력 값은 = ");
                System.out.println(input);
                // 3의 배수 또는 7의 배수일 시 msg 출력
                if (input % 2 == 0) {
                    msg = "\t 짝수 입니다.";
                } else {
                    msg = "\t 홀수 입니다.";
                }
                System.out.println(msg);
                if (input % 3 == 0) {
                    System.out.println("\t 3의 배수 입니다.");
                }
                if (input % 7 == 0) {
                    System.out.println("\t 7의 배수 입니다.");
                }
            } // 20000 입력시 msg출력 후 종료 또는 q 입력
            else if (input == 20000) {
                System.out.println("이용해주셔서 감사합니다");
                break;
            }
            // 0 이하의 값일 시 에러출력 후 재입력
            else {
                msg = "1이상 양수를 입력해주세요";
                System.out.println(msg);
            }
            
        }

        // String num = "3";
        // if (Integer.parseInt(num) % 3 == 0) {
        //     System.out.println("a");
        // }
    }
}
