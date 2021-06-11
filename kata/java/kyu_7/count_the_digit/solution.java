public class CountDig {
    public static int nbDig(int n, int d) {
        int count = 0;
        for (int i = 0; i <= n; i++)
          count += Integer.toString(i*i).chars().filter(ch -> ch == Character.forDigit(d, 10)).count();
        return count;
    }
}