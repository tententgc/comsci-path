class Outer {
    Inner i1 = new Inner();
    private String s = "outer string";

    void getInnerS() {
        System.out.println(i1.s);
    }

    void gets() {
        System.out.println(s);
    }

    class Inner {
        private String s = "Inner string";

        void gets() {
            System.out.println(s);
        }

        void getOuterS() {
            System.out.println(Outer.this.s);
        }
    }

    public static void main(String[] args) {
        Outer o = new Outer();
        o.gets();
        o.getInnerS();
        Outer.Inner oi = new Outer().new Inner();
        oi.getOuterS();
        oi.gets();

    }
}