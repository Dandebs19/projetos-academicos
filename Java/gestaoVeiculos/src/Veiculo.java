import java.util.Scanner;
public class Veiculo {

    private String placa, marca;
    private double preco;

    public Veiculo(String placa, String marca, double preco){
        this.placa = placa;
        this.marca = marca;
        this.preco = preco;

    }

    public void mostrarDados(){
        System.out.println("Placa: "+placa);
        System.out.println("Marca: "+marca);
        System.out.println("Preço: "+preco);
    }
    public void mostrarDados(double desconto){
        double precoFinal = preco -(preco*desconto);
        System.out.println("Preço com desconto: "+precoFinal);

    }

    public String getPlaca() {
        return placa;
    }


    public String getMarca() {
        return marca;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }
}

