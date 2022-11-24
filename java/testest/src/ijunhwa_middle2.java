public class ijunhwa_middle2 {
    public static void main(String[] args) {
        // 소문자 조건 루틴
        int Ncount = 0;
        for (char word = 'a'; word <= 'y'; word++, Ncount++) {
            // 특정 횟수 반복 시 마다 해당 문자 출력
            if (Ncount % 3 == 0) {
                System.out.print(word);
            }
        }
        
        // 줄바꿈
        System.out.println();

        // 대문자 역순 루틴
        for (char word = 'Z'; word >= 'A'; word--) {
            System.out.print(word);
        }
    }
}