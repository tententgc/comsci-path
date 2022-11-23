public class Firstclass implements Price {
    @Override
    public String getPrice() {
        return "First Class price: $5500";
    }

    @Override
    public int getPriceint() {
        return 5500;
    }
}