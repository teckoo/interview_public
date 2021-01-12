import java.util.*;


class Solution {
    public boolean isValid(String s) {
        Set<String> left = new HashSet<String>(Arrays.asList(new String[]{"(", "[", "{"}));
        Set<String> right = new HashSet<String>(Arrays.asList(new String[]{")", "]", "}"}));
        Map<String, String> map = new HashMap<String, String>();
        map.put("(", ")");
        map.put("[", "]");
        map.put("{", "}");

        Stack<String> stack = new Stack<String>();
        try{
            for (int i=0; i<s.length(); i++){
                String c = String.valueOf(s.charAt(i));
                if (left.contains(c)){
                    stack.push(String.valueOf(s.charAt(i)));
                } else if(right.contains(c)){
                    String top = stack.pop();
                    if (!(String.valueOf(s.charAt(i)).equals(map.get(top))))
                    return false;
                }
            }
            if (stack.isEmpty()) return true;
        } catch (Exception e){
            
        }
        return false;
    }

    public static void main(String[] args){
        Solution s = new Solution();

        System.out.println("convert array to set: " + s.isValid("()"));
    }
}
