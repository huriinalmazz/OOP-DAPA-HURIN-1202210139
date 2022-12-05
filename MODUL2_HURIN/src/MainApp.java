public class MainApp {
    public static void main(String[] args) throws Exception {
    
        //objek transportasi 
        Transportasi transportasi = new Transportasi (4, 20000);
        transportasi.Informasi();
        transportasi.Berlayar();
        transportasi.Berlabuh();
        System.out.println("");
        System.out.println("");

        //objek sampan dari class Sampan
        Sampan sampan = new Sampan (20, 5000, 2);
        sampan.Informasi();
        sampan.Berlayar();
        sampan.Berlabuh();
        sampan.Berlabuh(2);
        System.out.println("");
        System.out.println("");

        //objek kapal dari class Kapal
        
        Kapal kapal = new Kapal (50, 10000, "Diesel");
        kapal.Informasi();
        kapal.Berlabuh();
        kapal.Berlayar();
        kapal.Berlayar(20);
        System.out.println("");
        
        
    } 
}
