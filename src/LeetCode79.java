public class LeetCode79 {
    boolean[][] visited;
    char[][] board;

    public boolean exist(char[][] board, String word) {
        if(word.length() == 0)
            return true;
        this.board = board;
        for(int i = 0; i < board.length;i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] == word.charAt(0)){
                    visited = new boolean[board.length][board[0].length];
                    boolean c = search(word.substring(1), i, j);
                    if(c)
                        return true;
                }
            }
        }
        return false;
    }

    public boolean search(String word, int i, int j){
        visited[i][j] = true;
        if(word.length() == 0)
            return true;
        char next = word.charAt(0);
        boolean left = j - 1 >= 0 && board[i][j - 1] == next && !visited[i][j - 1] && search(word.substring(1),i,j-1);
        boolean right = !left && j + 1 < board[0].length && board[i][j + 1] == next && !visited[i][j + 1] && search(word.substring(1),i,j+1);
        boolean up = !right && i - 1 >= 0 && board[i - 1][j] == next && !visited[i - 1][j] && search(word.substring(1),i - 1, j);
        boolean down = !up && i + 1 < board.length && board[i + 1][j] == next && !visited[i + 1][j] && search(word.substring(1),i+1,j);
        boolean cons = left || right || up || down;
        if(!cons)
            visited[i][j] = false;
        return cons;
    }

    public static void main(String[] args){
        char[][] board = {
                {'A','B','C','E'},
                {'S','F','C','S'},
                {'A','D','E','E'}
        };
        System.out.println(new LeetCode79().exist(board,"CEESECBAS"));

    }

}
