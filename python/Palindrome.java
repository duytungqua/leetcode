package python;

public class Palindrome {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        
        //reverse the string
        StringBuilder sb = new StringBuilder(s);
        for (int i = s.length() - 1; i>=0; i--) {
            sb.append(String.valueOf(s.charAt(i)));
        }
        return sb.toString().equals(s);
    }

    public static void main(String[] args) {
        Palindrome p = new Palindrome();
        String s = "hello";
        p.isPalindrome(s);
}
