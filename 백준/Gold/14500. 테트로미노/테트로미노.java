import java.util.Scanner;

public class Main {
    static int N, M;
    static int[][] board;
    static int max = 0;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static boolean[][] visited;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();
        board = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                board[i][j] = sc.nextInt();
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                visited[i][j] = true;
                dfs(i, j, 1, board[i][j]);
                visited[i][j] = false;
                checkSpecial(i, j);
            }
        }

        System.out.println(max);
        sc.close();
    }

    static void dfs(int x, int y, int depth, int sum) {
        if (depth == 4) {
            max = Math.max(max, sum);
            return;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M || visited[nx][ny]) continue;

            visited[nx][ny] = true;
            dfs(nx, ny, depth + 1, sum + board[nx][ny]);
            visited[nx][ny] = false;
        }
    }

    static void checkSpecial(int x, int y) {
        // ㅗ 모양
        if (x > 0 && y > 0 && y < M - 1) {
            max = Math.max(max, board[x][y] + board[x-1][y] + board[x][y-1] + board[x][y+1]);
        }
        // ㅜ 모양
        if (x < N - 1 && y > 0 && y < M - 1) {
            max = Math.max(max, board[x][y] + board[x+1][y] + board[x][y-1] + board[x][y+1]);
        }
        // ㅏ 모양
        if (x > 0 && x < N - 1 && y < M - 1) {
            max = Math.max(max, board[x][y] + board[x-1][y] + board[x+1][y] + board[x][y+1]);
        }
        // ㅓ 모양
        if (x > 0 && x < N - 1 && y > 0) {
            max = Math.max(max, board[x][y] + board[x-1][y] + board[x+1][y] + board[x][y-1]);
        }
    }
}
