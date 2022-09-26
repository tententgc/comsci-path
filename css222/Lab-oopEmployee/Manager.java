public class Manager extends Employee {
    private String department;

    Manager(String name, double salary, String department) {
        super(name, salary);
        this.department = department;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    @Override
    public String toString() {
        return getName() + " have salary = " + getSalary() + " and department = " + department;
    }

}
