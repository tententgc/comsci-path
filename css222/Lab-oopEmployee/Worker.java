public abstract class Worker {
    private String name; 
    private double salary_rate; 
    Worker(String name, double salary_rate){ 
        this.name = name; 
        this.salary_rate = salary_rate; 
    }

    public String getName(){
         return name; 
    }

    public double getSalary_rate(){
         return salary_rate; 
    }


    public abstract double computePay();
}
