public class Bicycle {
    private String ownerName ,tagNo; 

    public Bicycle(){ 
        ownerName = "Unknown";
        tagNo = "Unknown"; 
    }

    public String getOwnerName() {
        return ownerName;
    }

    public void setOwnerName(String name) {
        ownerName = name; 
    }

    public String getTagNo() {
        return tagNo;
    } 

    public void setTagNo(String tag) {
        tagNo = tag; 
    } 
}
