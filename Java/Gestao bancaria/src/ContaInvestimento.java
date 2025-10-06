import java.util.Scanner;
public class ContaInvestimento extends Conta {
    private double taxaAdmnistracao;

    public ContaInvestimento(String numero, String titular, double saldo, double taxaAdmnistracao) {
        super(numero, titular, saldo);
        this.taxaAdmnistracao = taxaAdmnistracao;
    }

    public double getTaxaAdmnistracao() {
        return taxaAdmnistracao;
    }
    public void setTaxaAdmnistracao(double taxaAdmnistracao) {
        this.taxaAdmnistracao = taxaAdmnistracao;
    }

    @Override
    public void mostrarDados() {
        super.mostrarDados();
        System.out.println("Taxa de admnistração: " + getTaxaAdmnistracao());
    }

    public void mostrarDados(boolean considerarTaxa) {
        if (considerarTaxa){
            Scanner input = new Scanner(System.in);
            System.out.println("Insira a projeção estimada (%): ");
            double projMensal = input.nextDouble();
            double saldoProj = getSaldo()+(getSaldo()*projMensal/100);
            double saldoFinal = saldoProj - getTaxaAdmnistracao();
            System.out.println("Saldo líquido: " + saldoFinal);

        }else {
            mostrarDados();
        }
    }
}
