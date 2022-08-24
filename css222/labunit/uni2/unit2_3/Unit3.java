import java.util.Scanner; 
public class Unit3 {
    public static void main(String[] args) {
        //celsius to fahrenheit
        Scanner celsius = new Scanner(System.in);
        System.out.println("Enter temperature in celsius: ");

        Double c = celsius.nextDouble();
        double f = (c * 9 / 5) + 32;
        System.out.println("Temperature in fahrenheit is: " + f);
    }}
