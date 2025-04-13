public class PlaceFlower {

    public static boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        for (int i = 0; i< flowerbed.length; i++){
            boolean left = (i == 0 || flowerbed[i - 1] == 0);
            boolean right = (i == flowerbed.length - 1 || flowerbed[i + 1] == 0);

            if (left && right)
                if (flowerbed[i] == 0)
                    count++;
                    if (count >= n)
                        return true;


        }
        return false;
    }

    public static void main(String[] args) {
        int arr[] = {1, 0 ,0, 0, 1};
        canPlaceFlowers(arr, 1);

    }
}
