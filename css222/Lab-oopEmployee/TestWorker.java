public class TestWorker {
   public static void main(String[] args)
   {
        FullTimeWorker fullw = new FullTimeWorker("tenten", 1000,200);
        HourlyWorker partw= new HourlyWorker("sasuke", 2000,20);
        System.out.println(fullw.getName() + " have salary = " + fullw.computePay());
        System.out.println(partw.getName() + " have salary = " + partw.computePay());

   } 
}
