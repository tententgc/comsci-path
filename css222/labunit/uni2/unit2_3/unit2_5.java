public class unit2_5 {
    public static void main(String[] args) {
        int a[][] = {{4,7,9,8,3},{2,4,7,8,1},{1,1,8,1,2},{0,0,1,0,4}};
        int b[][] = { { 1, 2, 8, 4, 3 }, { 4, 1, 8, 3, 1 }, { 2, 1, 0, 0, 5 }, { 1, 2, 1, 1, 7 } };
        //addition mattrick a+b 
        for(int i=0; i<a.length; i++) {
            for(int j=0; j<a.length; j++) {
                a[i][j] = a[i][j] + b[i][j];
            }
        }
        //print addition mattrick
        System.out.println("Addition mattrick is: ");
        for(int i=0; i<a.length; i++) {
            for(int j=0; j<a.length; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.out.println();
        }

    
        int x[][] = { { 1, 2, 3 }, { 4, 5, 6 }, { 2, 3, 4 } };
        int y[][] = { { 1, 2, 3 }, { 4, 5, 6 }, { 2, 3, 4 } };

        //multiplication mattrick x*y
        for(int i=0; i<x.length; i++) {
            for(int j=0; j<x.length; j++) {
                for(int k=0; k<x.length; k++) {
                    x[i][j] = x[i][j] * y[i][k];
                }
            }
        }
        //print multiplication mattrick
        System.out.println("Multiplication mattrick is: ");
        for(int i=0; i<x.length; i++) {
            for(int j=0; j<x.length; j++) {
                System.out.print(x[i][j] + " ");
            }
            System.out.println();
        }

        
    }
}
