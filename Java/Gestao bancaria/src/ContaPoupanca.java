public class ContaPoupanca extends Conta{
    private double taxaRendimentoMensal;

    public ContaPoupanca(String numero, String titular, double saldo, double taxaRendimentoMensal) {
        super(numero, titular, saldo);
        this.taxaRendimentoMensal = taxaRendimentoMensal;
    }

    public double getTaxaRendimentoMensal() {
        return taxaRendimentoMensal;
    }
    public void setTaxaRendimentoMensal(double taxaRendimentoMensal) {
        this.taxaRendimentoMensal = taxaRendimentoMensal;
    }

    @Override
    public void mostrarDados(){
        super.mostrarDados();
        System.out.println("Taxa de rendimento mensal: " + getTaxaRendimentoMensal());

    }
    public void mostrarDados(boolean taxaAnual){
        double taxaEstimada = getTaxaRendimentoMensal()*12;

        if (taxaAnual){
            mostrarDados();
            System.out.println("Taxa de rendimento anual estimada: " + taxaEstimada);
        }else{
            mostrarDados();
        }
    }
}
