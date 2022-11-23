public class Wine implements Opt {
    @Override
    public String getOption() {
        return "Wine price: $30";
    }

    @Override
    public int getOptionint() {
        return 30;
    }
}