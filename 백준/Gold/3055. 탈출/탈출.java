import java.util.*;

public class Main {
    static int R, C;
    static char[][] map;
    static int[][] dist;
    static Queue<int[]> water = new LinkedList<>();
    static Queue<int[]> hedgehog = new LinkedList<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        R = sc.nextInt();
        C = sc.nextInt();
        map = new char[R][C];
        dist = new int[R][C];

        for (int i = 0; i < R; i++) {
            String line = sc.next();
            for (int j = 0; j < C; j++) {
                map[i][j] = line.charAt(j);
                if (map[i][j] == '*') water.offer(new int[]{i, j});
                if (map[i][j] == 'S') hedgehog.offer(new int[]{i, j});
            }
        }

        System.out.println(bfs());
    }

    static String bfs() {
        while (!hedgehog.isEmpty()) {
            int size = water.size();
            while (size-- > 0) {
                int[] cur = water.poll();
                for (int i = 0; i < 4; i++) {
                    int nx = cur[0] + dx[i];
                    int ny = cur[1] + dy[i];
                    if (nx < 0 || ny < 0 || nx >= R || ny >= C) continue;
                    if (map[nx][ny] == '.' || map[nx][ny] == 'S') {
                        map[nx][ny] = '*';
                        water.offer(new int[]{nx, ny});
                    }
                }
            }

            size = hedgehog.size();
            while (size-- > 0) {
                int[] cur = hedgehog.poll();
                for (int i = 0; i < 4; i++) {
                    int nx = cur[0] + dx[i];
                    int ny = cur[1] + dy[i];
                    if (nx < 0 || ny < 0 || nx >= R || ny >= C) continue;
                    if (map[nx][ny] == 'D') return String.valueOf(dist[cur[0]][cur[1]] + 1);
                    if (map[nx][ny] == '.') {
                        map[nx][ny] = 'S';
                        dist[nx][ny] = dist[cur[0]][cur[1]] + 1;
                        hedgehog.offer(new int[]{nx, ny});
                    }
                }
            }
        }
        return "KAKTUS";
    }
}