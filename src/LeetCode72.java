public class LeetCode72 {
    public int minDistance(String word1, String word2) {
        int l1 = word1.length();
        int l2 = word2.length();
        int[][] table = new int[l1 + 1][l2 + 1];
        for(int i = 1;i <= l2;i++)
            table[0][i] = i;
        for(int i = 1; i <= l1;i++)
            table[i][0] = i;
        for(int i = 1; i <= l1; i++){
            for(int j = 1; j <= l2; j++){
                if(word1.charAt(i - 1) == word2.charAt(j - 1))
                    table[i][j] = table[i - 1][j -1];
                else
                    table[i][j] = Integer.min(table[i-1][j-1],Integer.min(table[i-1][j],table[i][j-1])) + 1;
            }
        }
        return table[l1][l2];
    }

    public static void main(String[] args){
        System.out.println(new LeetCode72().minDistance("ab","a"));
    }
}
