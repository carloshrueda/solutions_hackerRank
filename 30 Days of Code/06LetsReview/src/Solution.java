import java.util.Scanner;

/**
 *
 * @author crueda
 */
public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        sc.nextLine();

        if ((T >= 1) && (T <= 10)) {
            String S = "";
            for (int i = 1; i <= T; ++i) {
                S = sc.nextLine();
                if ((S.length() >= 2) && (S.length() <= 10000)) {
                    char[] vstr = S.toCharArray();
                    for (int j = 0; j < S.length(); j += 2) {
                        System.out.print(vstr[j]);
                    }
                    System.out.print(" ");
                    for (int j = 1; j < S.length(); j += 2) {
                        System.out.print(vstr[j]);
                    }
                    System.out.println();
                }
            }
        }
    }
}
