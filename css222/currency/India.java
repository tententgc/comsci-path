public class India implements Currency {
    @Override
    public String getCurrency() {
        return "Rupee";
    }

    @Override
    public String getSymbol() {
        return "Rs";
    }

    public static void main(String a[]) {
        India in = new India();
        System.out.println(in.getCurrency());
        System.out.println(in.getSymbol());
    }
}