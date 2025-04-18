package python;

import java.util.Arrays;
import java.util.List;

public class ReverseVowel {
    public String reverseVowel(String test){
        List<Character> strVowel = Arrays.asList('u', 'e', 'o', 'a', 'i', 'U', 'E', 'O', 'A', 'I');
        char[] chars = test.toCharArray();
        
        int i = 0;
        int j = chars.length - 1;
        while (i < j) {
            if (!strVowel.contains(chars[i]))
                i++;
            else if (!strVowel.contains(chars[j]))
                j--;
            else {
                char temp = chars[i];
                chars[i] = chars[j];
                chars[j] = temp;
                i++;
                j--;
            }
        }
        return new String(chars);
    }
}
