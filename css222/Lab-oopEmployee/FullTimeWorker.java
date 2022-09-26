public class FullTimeWorker extends Worker{ 
    
    private int hours_worked ;
    FullTimeWorker(String name, double salary_rate, int hours_worked){
        super(name, salary_rate);
        this.hours_worked = hours_worked;
    } 


    @Override
    public double computePay(){
        return hours_worked*100; 
    }
}