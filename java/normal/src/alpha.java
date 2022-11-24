import java.util.*;

public class alpha {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        while (true) {
            // 정수를 입력받기

            System.out.print("정수를 입력하시오:");
            
            int select = scan.nextInt();
            if (select == 1 || select == 2) {
                System.out.print("출력할 줄 수를 입력하세요:");
                int line = scan.nextInt();

                if (select == 1) {
                    for (int loop = 1; loop <= line; loop++) {
                        String msg = "";
                        for (char word = 'a'; word <= 'z'; word++) {
                            msg += word;
                        }
                        System.out.println(msg);
                    }
                } else {
                    for (int loop = 1; loop <= line; loop++) {
                        String msg = "";
                        for (char word = 'A'; word <= 'Z'; word++) {
                            msg += word;
                        }
                        System.out.println(msg);
                    }
                }
                break;
            }
            
        }

    }
}
