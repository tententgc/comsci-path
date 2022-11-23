public class Business implements Price {
    @Override
    public String getPrice() {
        return "Business Class price: $4500";
    }

    @Override
    public int getPriceint() {
        return 4500;
    }
}