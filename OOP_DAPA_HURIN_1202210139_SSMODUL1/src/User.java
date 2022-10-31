public class User {
    private String nama;
    private int no_handphone;

    public void setNama(String nama) {
        this.nama = nama;
    }
    public void setNomor(int no_handphone) {
        this.no_handphone = no_handphone; 
    }
    public String getNama() {
        return nama;
    }
    public int getNomor() {
        return no_handphone;
    }
    System.out.println("Nama    : " + nama);
    String nama = nextLine();
    System.out.println("No. Handphone : " + no_handphone);
    int no_handphone = nextInt();



    
}
