package python;

import java.util.Arrays;
import java.util.List;

public class ReverseVowel {
    public String reverseVowel(String test){
       List<Character> lstVowel = Arrays.asList('u','e','o','a','i','U', 'E','O','A','I');
         char[] arr = test.toCharArray();
        int i = 0;
        int j = arr.length - 1;
        while (i < j) {
            if (!lstVowel.contains(arr[i])) {
                i++;
            } else if (!lstVowel.contains(arr[j])) {
                j--;
            } else {
                char temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
        }
        return new String(arr);
    }
}
