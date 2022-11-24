public class loop {
    public static void main(String[] args) {
        
        // "a" ~ "z" 까지 , For, WHILE, DO WHILE 를 이용 각각 출력하라.

        for (char word = 'a'; word <= 'z'; word++) {
            System.out.print(word);
            System.out.print(" ");
        }

        System.out.println();

        char word = 'a';
        while (word <= 'z') {
            System.out.print(word++);
            System.out.print(" ");
        }

        System.out.println();

        word = 'a';
        do {
            System.out.print(word++);
            System.out.print(" ");
        } while (word <= 'z');

    }
}
