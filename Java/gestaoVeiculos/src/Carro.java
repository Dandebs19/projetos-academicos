public class Carro extends Veiculo {
    private int numPortas;

    public Carro (String placa, String marca, double preco, int numPortas){
        super(placa, marca, preco);
        this.numPortas = numPortas;

    }
    //sobrescrita
    @Override
    public void mostrarDados() {
        super.mostrarDados();
        System.out.println("Número de portas: "+numPortas);
    }
    //sobrecarga
    public void mostrarDados(boolean mostrarPortas) {
        super.mostrarDados();
        if (mostrarPortas){
            System.out.println("Número de portas: "+numPortas);;
        }
    }
    public int getNumPortas() {
        return numPortas;
    }
}
