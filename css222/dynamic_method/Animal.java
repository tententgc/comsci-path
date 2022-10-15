class Animals{ 
    public void speak(){
        System.out.println("Animal Speaking");
    } 
}

class Dog extends Animals{
    public void speak(){
        bark();
    }

    public void bark(){
        System.out.println("Woof !");
    } 
} 

class Seal extends Animals{
    public void speak(){
        bark();
    }

    public void bark(){
        System.out.println("Arf !");
    } 
} 

class Bird extends Animals{
    public void speak(){
        bark();
    }

    public void bark(){
        System.out.println("Tweet !");
    } 
}

class Animal{
    public static void main(String[] args)
    {
        Animals[] animals = new Animals[4];
        animals[0] = new Animals(); 
        animals[1] = new Dog();
        animals[2] = new Seal();
        animals[3] = new Bird();

        for(int i=0; i<animals.length; i++){
            animals[i].speak();
        }
    }
}