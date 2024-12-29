import java.util.*;

public class Main {
    static String[] command = new String[10000];
    static boolean[] visited = new boolean[10000];
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        while (T-- > 0) {
            int A = sc.nextInt();
            int B = sc.nextInt();
            
            Arrays.fill(command, "");
            Arrays.fill(visited, false);
            
            Queue<Integer> queue = new LinkedList<>();
            queue.offer(A);
            visited[A] = true;
            
            while (!queue.isEmpty()) {
                int current = queue.poll();
                
                if (current == B) {
                    System.out.println(command[current]);
                    break;
                }
                
                int D = (current * 2) % 10000;
                int S = (current == 0) ? 9999 : current - 1;
                int L = (current % 1000) * 10 + current / 1000;
                int R = (current % 10) * 1000 + current / 10;
                
                if (!visited[D]) {
                    queue.offer(D);
                    visited[D] = true;
                    command[D] = command[current] + "D";
                }
                if (!visited[S]) {
                    queue.offer(S);
                    visited[S] = true;
                    command[S] = command[current] + "S";
                }
                if (!visited[L]) {
                    queue.offer(L);
                    visited[L] = true;
                    command[L] = command[current] + "L";
                }
                if (!visited[R]) {
                    queue.offer(R);
                    visited[R] = true;
                    command[R] = command[current] + "R";
                }
            }
        }
        sc.close();
    }
}
