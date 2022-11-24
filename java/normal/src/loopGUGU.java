public class loopGUGU {
    public static void main(String[] args) {
        String msg = "";

        for (int value = 2; value <= 9; value ++) {
            for (int num = 1; num <= 9; num++) {
                msg += Integer.toString(value);
                msg += " X ";
                msg += Integer.toString(num);
                msg += " = ";
                msg += Integer.toString(value * num);
                msg += "\n";
            }
        }
        System.out.println(msg);
    }
}
