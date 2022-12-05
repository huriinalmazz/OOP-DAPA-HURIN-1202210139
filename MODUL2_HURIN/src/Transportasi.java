public class Transportasi {
    protected int jumlahKursi; int biaya;
    
    //variable constructor
    public Transportasi(int jumlahKursi, int biaya){
        this.jumlahKursi = jumlahKursi;
        this.biaya = biaya;
        
    }
    //method void informasi 
    public void Informasi(){
        System.out.println("Transportasi Air jenis tidak diketahui dengan kursi berjumlah " + jumlahKursi + " ditetapkan dengan biaya sebesar Rp. " + biaya);
    }

    public void Berlayar(){
        System.out.println("Transportasi Air jenis tidak diketahui sedang berlayar");
    }

    public void Berlabuh(){
        System.out.println("Transportasi Air jenis tidak diketahui berlabuh di pantai");
    }
}
