public class Conta {
   private String numero, titular;
   private Double saldo;

    public Conta(String numero, String titular, Double saldo) {
        this.numero = numero;
        this.titular = titular;
        this.saldo = saldo;
    }

    public Conta() {
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public String getTitular() {
        return titular;
    }

    public void setTitular(String titular) {
        this.titular = titular;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(Double saldo) {
        this.saldo = saldo;
    }

public void mostrarDados(){
    System.out.println("----- DADOS DA CONTA -----\n");
    System.out.println("Número: "+ getNumero());
    System.out.println("Titular: "+getTitular());
    System.out.println("Saldo: R$ "+getSaldo());

}
public void mostrarDados(double projecaoMensal){
     mostrarDados();
     double saldoProjecao = getSaldo() + (getSaldo() * projecaoMensal / 100);
     System.out.println("Projeção Mensal: " + projecaoMensal + "%");
     System.out.println("Saldo Projetado: R$ " + saldoProjecao);

}

}
