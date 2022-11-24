public class Untitled1 {
    public static void main(String[] args) {
        for (int i = 20; i <= 30; i++) {
            if (i % 7 == 0) {
                System.out.println(i);
                break; // 이후 명령문 실행 X
                // 특정조건에 반복문이 중단할때
                // continue; 특정 조건일때만 명령문을 건너뛸때
            }
            System.out.println("i 값 : " + i);
        }
    }
}
