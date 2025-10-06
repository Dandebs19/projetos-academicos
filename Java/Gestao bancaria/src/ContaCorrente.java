public class ContaCorrente extends Conta{
    private double limiteChequeEspecial;

    public ContaCorrente(String numero, String titular, double saldo, double limiteChequeEspecial) {
        super(numero, titular, saldo);
        this.limiteChequeEspecial= limiteChequeEspecial;
    }

    public double getLimiteChequeEspecial() {
        return limiteChequeEspecial;
    }

    public void setLimiteChequeEspecial(double chequeEspecial) {
        limiteChequeEspecial = chequeEspecial;
    }

    @Override
    public void mostrarDados() {
        super.mostrarDados();
        System.out.println("Limite do cheque especial: "+ getLimiteChequeEspecial());
    }

    public void mostrarDados(boolean detalharLimite) {
        if(detalharLimite){
            mostrarDados();
            System.out.println("Saldo total(com limite): "+ (getSaldo()+getLimiteChequeEspecial()));
        }else{
            super.mostrarDados();
        }
    }
}
