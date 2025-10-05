public class Caminhao extends Veiculo  {
    private double capacidadeCarga;

    public Caminhao(String placa, String marca, double preco, double capacidadeCarga){
        super(placa, marca, preco);
        this.capacidadeCarga = capacidadeCarga;

    }

    @Override
    public void mostrarDados(){
        super.mostrarDados();
        System.out.println("Capacidade de carga " + capacidadeCarga);
    }


    public void mostrarDados(boolean medidaTon) {
        super.mostrarDados();
        if(medidaTon){

            System.out.println("Toneladas: "+capacidadeCarga);
        }
        else{
            System.out.println("Quilogramas "+(capacidadeCarga*1000));
        }
    }
    public double getCapacidadeCarga() {
        return capacidadeCarga;
    }

    public void setCapacidadeCarga(double capacidadeCarga) {
        this.capacidadeCarga = capacidadeCarga;
    }


}
