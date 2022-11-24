import java.util.Scanner;

public class gugu {
    public static void main(String args[]) {

        Scanner scn = new Scanner(System.in);
        boolean flag = true;

        while (flag) {
            // 메뉴 출력
            {
            System.out.println("--------------------");
            System.out.println("1. 구구단 출력");
            System.out.println("2. 프로그램 종료");
            System.out.println("--------------------");
            }

            // 키보드로부터 정수 값 입력
            int signal = scn.nextInt();

            // "1" 선택 시 구구단 출력
            if (signal == 1) {
                    System.out.println("출력할 구구단의 단을 입력하세요. 구구단의 단은 2~9 사이 입력");
                while (true) {
                    /*
                    출력 할 단을 키보드로부터 입력
                    출력 유효 단은 2 ~ 9
                    2 ~ 9단 이외의 값이 들어올 경우 Error Msg. 출력 후 재입력
                    */
                    int dan = scn.nextInt();

                    if (dan >= 2 && dan <= 9) {
                        for (int num = 2; num < 10; num ++) 
                            System.out.println(dan + " X " + num + " = " + (dan * num));
                        break;
                    }
                    else
                        System.out.println("2~9 사이 정수를 입력해주세요.");
                    
                }
            }

            // "2" 인 경우 Msg. 출력 후 프로그램 종료
            else if (signal == 2) {
                System.out.println("이용해주셔서 감사합니다.");
                flag = false;
            }

            // 이외의 값이 입력될 경우, Error Msg. 출력 후 재입력
            else {
                System.out.println("잘못 입력하셨습니다. 다시 입력하세요.");
            }
        }
    }
}