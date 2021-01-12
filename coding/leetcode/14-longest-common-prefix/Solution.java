import java.util.ArrayList; 
import java.util.Collections;


class Solution {
    public String longestCommonPrefix(String[] strs) {
        String result = null;
        return result;
    }

    public static void main(String[] args) {

        for (String s : args) {
            System.out.println(s); 
        }
        ArrayList<String> list = new ArrayList<String>();
        list.add("a");
        list.add("c");
        list.add("b");
        Collections.sort(list);  // Collections.reverseOrder()
        System.out.println("after sort:" + list);
    }
}