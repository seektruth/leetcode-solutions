import java.util.LinkedList;
import java.util.List;

public class LeetCode68 {

    public String build(LinkedList<String> temp, int totalWordsLength, int maxWidth){
        int wordsNum = temp.size();
        StringBuilder builder = new StringBuilder();
        if(wordsNum == 1){
            builder.append(temp.removeLast());
            while (builder.length() < maxWidth)
                builder.append(' ');
        }
        else{
            int inteval = (maxWidth - totalWordsLength) / (wordsNum - 1);
            int remainder = (maxWidth - totalWordsLength) % (wordsNum - 1);
            for (int i = 0; i<wordsNum; i++){
                String word = temp.removeFirst();
                builder.append(word);
                if(i != wordsNum - 1){
                    for(int j = 0; j < (i < remainder? inteval + 1: inteval); j++){
                        builder.append(' ');
                    }
                }
            }
        }
        return builder.toString();
    }

    public String buildLast(LinkedList<String> temp, int totalWordsLength, int maxWidth){
        int wordsNum = temp.size();
        StringBuilder builder = new StringBuilder();
        for(int i = 0; i < wordsNum; i++){
            builder.append(temp.removeFirst());
            if(i != wordsNum - 1)
                builder.append(' ');
        }
        while (builder.length() < maxWidth)
            builder.append(' ');
        return builder.toString();
    }

    public List<String> fullJustify(String[] words, int maxWidth) {
        LinkedList<String> consequence = new LinkedList<>();
        LinkedList<String> temp = new LinkedList<>();
        int totalWordsLength = 0;
        int wordsNum = 0;
        int i = 0;
        while (i < words.length){
            String word = words[i];
            if(totalWordsLength + word.length() + wordsNum <= maxWidth){
                totalWordsLength += word.length();
                wordsNum++;
                temp.addLast(word);
                i++;
            }
            else{
                consequence.addLast(build(temp,totalWordsLength,maxWidth));
                wordsNum = 0;
                totalWordsLength = 0;
            }
        }
        if(wordsNum != 0)
            consequence.addLast(buildLast(temp,totalWordsLength,maxWidth));
        return consequence;
    }

    public static void main(String[] args){
        List<String> list = new LeetCode68().fullJustify(new String[]{"What","must","be","shall","be."}, 12);
        for(String line: list){
            System.out.println(line);
        }
    }

}
