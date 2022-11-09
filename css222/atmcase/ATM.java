import java.util.Scanner;

class User {

    private int accountNumber;
    private int pin;
    private double availableBalance;
    private double totalBalance;

    // Constructor

    public User(int accountNumber, int pin, double availableBalance, double totalBalance) {
        this.accountNumber = accountNumber;
        this.pin = pin;
        this.availableBalance = availableBalance;
        this.totalBalance = totalBalance;
    }

    // Getters

    public int getAccountNumber() {
        return accountNumber;
    }

    public int getPin() {
        return pin;
    }

    public double getAvailableBalance() {
        return availableBalance;
    }

    public double getTotalBalance() {
        return totalBalance;
    }

    // Setters

    public void setAccountNumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void setPin(int pin) {
        this.pin = pin;
    }

    public void setAvailableBalance(double availableBalance) {
        this.availableBalance = availableBalance;
    }

    public void setTotalBalance(double totalBalance) {
        this.totalBalance = totalBalance;
    }

    // Methods

    public void depositBalance(double amount) {
        availableBalance += amount;
        totalBalance += amount;
    }

    public void withdrawBalance(double amount) {
        availableBalance -= amount;
        totalBalance -= amount;
    }

    public boolean validatePin(int pin) {
        if (this.pin == pin) {
            return true;
        } else {
            return false;
        }
    }

    public String toString() {
        return ("User :[ AccountNumber : " + accountNumber + ", pin : " + pin + ", availableBalance :"
                + availableBalance + ", totalBalance :" + totalBalance + " ]");
    }

}

public class ATM {
    public static void main(String[] args) {

        User user = new User(12345, 54321, 500.00, 1000.00);

        System.out.println("Welcome");
        Scanner accountNumber = new Scanner(System.in);
        System.out.print("Please enter your account number: ");
        int accountNumberInput = accountNumber.nextInt();
        if (accountNumberInput == user.getAccountNumber()) {
            Scanner pin = new Scanner(System.in);
            System.out.print("Enter your PIN: ");
            int pinInput = pin.nextInt();
            if (user.validatePin(pinInput)) {
                System.out.println("Main Menu");
                System.out.println("    1 - View my Balance");
                System.out.println("    2 - Withdraw cash");
                System.out.println("    3 - Deposit funds");
                System.out.println("    4 - Exit");
                Scanner choice = new Scanner(System.in);
                System.out.print("Enter your choice: ");
                int choiceInput = choice.nextInt();
                switch (choiceInput) {
                    case 1:
                        System.out.println("Your balance is " + user.getTotalBalance());
                        break;
                    case 2:
                        System.out.println("Withdrawal Menu");
                        System.out.println("    1 - $20     4 - $100");
                        System.out.println("    2 - $40     5 - $200");
                        System.out.println("    3 - $60     6 - $Cancel Transaction");
                        System.out.print("Choose a withdrawal amount: ");
                        Scanner withdraw = new Scanner(System.in);
                        double withdrawInput = withdraw.nextDouble();
                        if (withdrawInput > user.getTotalBalance()) {
                            System.out.println("Insufficient balance");
                            break;
                        } else {
                            switch ((int) withdrawInput) {
                                case 1:
                                    user.withdrawBalance(20);
                                    System.out.println("Please take your cash");
                                    break;
                                case 2:
                                    user.withdrawBalance(40);
                                    System.out.println("Please take your cash");
                                    break;
                                case 3:
                                    user.withdrawBalance(60);
                                    System.out.println("Please take your cash");
                                    break;
                                case 4:
                                    user.withdrawBalance(100);
                                    System.out.println("Please take your cash");
                                    break;
                                case 5:
                                    user.withdrawBalance(200);
                                    System.out.println("Please take your cash");
                                    break;
                                case 6:
                                    System.out.println("Transaction cancelled");
                                    break;
                                default:
                                    System.out.println("Invalid choice");
                                    break;
                            }
                            break;
                        }
                    case 3:
                        System.out.println("Enter the amount to deposit");
                        Scanner deposit = new Scanner(System.in);
                        double depositInput = deposit.nextDouble();
                        user.depositBalance(depositInput);
                        System.out.println("Your balance is " + user.getTotalBalance());
                        break;
                    case 4:
                        System.out.println("Thank you for using our ATM");
                        break;
                    default:
                        System.out.println("Invalid choice");
                        break;
                }
            } else {
                System.out.println("Invalid pin");
            }
        } else {
            System.out.println("Invalid account number");
        }
    }
}
