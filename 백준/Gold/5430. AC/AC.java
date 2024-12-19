import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        sc.nextLine(); // 개행문자 제거

        for (int t = 0; t < T; t++) {
            String p = sc.nextLine();
            int n = Integer.parseInt(sc.nextLine());
            String arrStr = sc.nextLine();

            Deque<String> deque = new ArrayDeque<>();
            if (n > 0) {
                String[] arr = arrStr.substring(1, arrStr.length() - 1).split(",");
                deque.addAll(Arrays.asList(arr));
            }

            boolean isReversed = false;
            boolean hasError = false;

            for (char cmd : p.toCharArray()) {
                if (cmd == 'R') {
                    isReversed = !isReversed;
                } else if (cmd == 'D') {
                    if (deque.isEmpty()) {
                        hasError = true;
                        break;
                    }
                    if (isReversed) {
                        deque.removeLast();
                    } else {
                        deque.removeFirst();
                    }
                }
            }

            if (hasError) {
                System.out.println("error");
            } else {
                StringBuilder sb = new StringBuilder("[");
                while (!deque.isEmpty()) {
                    sb.append(isReversed ? deque.removeLast() : deque.removeFirst());
                    if (!deque.isEmpty()) {
                        sb.append(",");
                    }
                }
                sb.append("]");
                System.out.println(sb.toString());
            }
        }
        sc.close();
    }
}
