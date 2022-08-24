public class Unit2_4 {
    public static void main(String[] args) {
        int arr[] = {234,6,85,298,18,1790,76,13, 45,-1 ,5};
        //sort array
        for(int i=0; i<arr.length; i++) {
            for(int j=i+1; j<arr.length; j++) {
                if(arr[i] > arr[j]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        //print array
        System.out.println("Sorted array is: ");
        for(int i=0; i<arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
    } 
