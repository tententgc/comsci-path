public class CurrencyFactory {
    public static Currency getCurrencyByCountry(String cnty) throws Exception {
        if (cnty.equalsIgnoreCase("India")) {
            return new India();
        } else if (cnty.equalsIgnoreCase("USA")) {
            return new USA();
        } else if (cnty.equalsIgnoreCase("Thailand")) {
            return new Thailand();
        } else {
            throw new Exception("Invalid Country");
        }
    }

    public static void main(String a[]) {
        try {
            Currency c = CurrencyFactory.getCurrencyByCountry("Thailand");
            System.out.println(c.getCurrency());
            System.out.println(c.getSymbol());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}