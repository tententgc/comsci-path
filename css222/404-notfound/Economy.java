public class Economy implements Price {
    @Override
    public String getPrice() {
        return "Economy Class price: $2500";
    }

    @Override
    public int getPriceint() {
        return 2500;
    }
}