import java.util.*;

public class ijunhwa_middle1 {
    public static void main(String[] args) {
        // scanner 클래스 정의
        Scanner scan = new Scanner(System.in);
        
        // 메인루프
        boolean flag = true;
        while (flag) {
            String msg = "";

            // 값 입력받기
            int input_value = scan.nextInt();

            if (input_value < 0 || input_value > 100) { // 범위 제한
                msg = "잘못된 입력 값 입니다. 다시 입력 하세요";
            } else { // 등급 분류
                if (input_value >= 90) {
                    msg = "A";
                } else if (input_value >= 80) {
                    msg = "B";
                } else if (input_value >= 70) {
                    msg = "C";
                } else if (input_value >= 60) {
                    msg = "D";
                } else {
                    msg = "F";
                }

                // 출력 메시지 설정
                msg = input_value + "의 등급은 " + msg + " 입니다";
                // 반복 종료설정
                flag = false;
            }
            
            System.out.println(msg);
        }
    }
}