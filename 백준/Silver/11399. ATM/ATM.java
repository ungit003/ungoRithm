import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int[] times = new int[N];
        
        for (int i = 0; i < N; i++) {
            times[i] = sc.nextInt();
        }
        
        // 버블 정렬
        for (int i = 0; i < N - 1; i++) {
            for (int j = 0; j < N - i - 1; j++) {
                if (times[j] > times[j + 1]) {
                    int temp = times[j];
                    times[j] = times[j + 1];
                    times[j + 1] = temp;
                }
            }
        }
        
        int total = 0;
        int wait = 0;
        
        for (int time : times) {
            wait += time;
            total += wait;
        }
        
        System.out.println(total);
        
        sc.close();
    }
}
