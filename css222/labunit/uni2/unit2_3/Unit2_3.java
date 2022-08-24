public class Unit2_3 {
    public static void main(String[] args) {
        System.out.println("Find length of array"); 
        int a1[] = new int[10]; 
        int a2[] = {1,2,3,4,5,6,7,8,9,-10};
        int a3[] = {1,2,3,4}; 


        System.out.println("Length of array a1 is " + a1.length);
        System.out.println("Length of array a2 is " + a2.length);
        System.out.println("Length of array a3 is " + a3.length);


        int a[][] = { {4,7,9,8,3},{2,4,6,2,8},{1,2,3,4,5} };

        for(int i=0; i<a.length; i++) {
            for(int j=0; j< a.length; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        } 
    }
}