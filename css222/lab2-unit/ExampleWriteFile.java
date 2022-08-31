import java.io.FileWriter; 
import java.io.IOException; 

public class ExampleWriteFile {
    public static void main(String[] args) {
        try{ 
            FileWriter myWriter = new FileWriter("filename.txt");
            myWriter.write("Files in Java might be tricky, but it can be done.");
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
        }catch(IOException e){
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
