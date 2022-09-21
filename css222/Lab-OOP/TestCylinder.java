public class TestCylinder {
   public static void main(String[] args) { 
    Cylinder c1 = new Cylinder();
    System.out.println("Cylinder:"
        + " radius=" + c1.getRadius()
        + " height=" + c1.getHeight()
        + "color=" + c1.getColor()
        + " base area=" + c1.getArea()
        + " volume=" + c1.getVolume());

    Cylinder c2 = new Cylinder(5.0, 2.0);
    System.out.println("Cylinder:"
        + " radius= " + c2.getRadius()
        + " height= " + c2.getHeight()
        + " color= " + c2.getColor()
        + " base area= " + c2.getArea()
        + " volume= " + c2.getVolume());
   }

   

}
