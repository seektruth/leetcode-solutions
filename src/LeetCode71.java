
import java.util.LinkedList;


public class LeetCode71 {
    public String simplifyPath(String path) {
        String[] tokens = path.split("/");
        LinkedList<String> stack = new LinkedList<>();
        for(String token : tokens){
            switch (token){
                case "..":
                    if(stack.size() > 0)
                        stack.removeLast();
                    break;
                case ".":
                case "":
                    break;
                default:
                    stack.addLast(token);
            }
        }
        return "/" + String.join("/",stack);
    }

    public static void main(String[] args){
        System.out.println(new LeetCode71().simplifyPath("/.."));
    }
}
