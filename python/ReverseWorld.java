package python;
public class ReverseWorld {
    
    public String reWor(String s){
        String trimS = s.trim();
        String[] arrString = trimS.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int j = arrString.length - 1; j >= 0; j --) {
            if (arrString[j].isBlank()) {
                continue;
            }
            sb.append(arrString[j]);
            if (j != 0) {
                sb.append(" ");
            }
        }
        return sb.toString();
        
    }

    public static void main(String[] args) {
        ReverseWorld rw = new ReverseWorld();
        String s =  "a good   example";
        System.out.println(rw.reWor(s));
    }
}
