public class Premium implements Price {
    @Override
    public String getPrice() {
        return "Premium Class price: $3500";
    }

    @Override
    public int getPriceint() {
        return 3500;
    }
}