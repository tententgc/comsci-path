import java.io.File;
import java.io.IOException;

public class ExampleCreateFile {
    public static void main(String[] args){
        try{ 
            File myObj = new File("filename.txt");
            if(myObj.createNewFile()){
                System.out.println("File created: " + myObj.getName());
        }else{
            System.out.println("File already exists.");
        }
    }catch(IOException e){
        System.out.println("An error occurred.");
        e.printStackTrace();
    }

    }
}
