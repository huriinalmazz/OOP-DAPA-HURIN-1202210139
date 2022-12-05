public class Kapal extends Transportasi{
    protected String mesin;

    //variable constructor
    public Kapal(int jumlahKursi, int biaya, String mesin) {
        super(jumlahKursi, biaya);
        this.mesin = mesin;
    }
    //method void 
    @Override
    public void Informasi() {
        System.out.println("Transportasi Air jenis Kapal dengan kursi berjumlah " + jumlahKursi + " ditetapkan dengan biaya sebesar Rp. " + biaya);
    }

    @Override
    public void Berlayar() {
        System.out.println("Transportasi Air jenis Kapal sedang berlayar menggunakan mesin " + mesin + " dengan kecepatan yang tidak stabil");
    }

    @Override
    public void Berlabuh() {
        System.out.println("Transportasi Air jenis Kapal sedang berlabuh di pantai");
    }

    public void Berlayar(int kecepatan) {
        System.out.println("Transportasi Air jenis Kapal sedang berlayar menggunakan mesin " +  mesin + " dengan kecepatan stabil di kisaran " + kecepatan + " knot");
    }
}
