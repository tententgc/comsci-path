public class PriceFactory {
    public static Price getPriceByClass(String className) throws Exception {
        if (className.equalsIgnoreCase("Economy")) {
            return new Economy();
        } else if (className.equalsIgnoreCase("Business")) {
            return new Business();
        } else if (className.equalsIgnoreCase("First")) {
            return new Firstclass();
        } else if (className.equalsIgnoreCase("Premium")) {
            return new Premium();
        } else {
            throw new Exception("Invalid Class");
        }
    }

public static Opt getOptionByOption(String option) throws Exception { if(option.equalsIgnoreCase("WiFi")){
return new WiFi();
} else if(option.equalsIgnoreCase("LiveTV")){ return new LiveTV();
} else if(option.equalsIgnoreCase("Wine")){ return new Wine();
} else {
throw new Exception("Invalid Option");
} }

public static void main(String a[]) {
try {
    Price p = PriceFactory.getPriceByClass("Economy");
    System.out.println(p.getPrice());
    Opt o = PriceFactory.getOptionByOption("WiFi");
    System.out.println(o.getOption());
    int i = 0;
    i = p.getPriceint();
    i += o.getOptionint();
    System.out.println("Total Price: $" + i);
} catch (Exception e) {
    e.printStackTrace();
}
}
}