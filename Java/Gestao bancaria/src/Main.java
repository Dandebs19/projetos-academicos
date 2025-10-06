import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    ArrayList<Conta> registroContas = new ArrayList<>();

    while(true){
        try {
            System.out.println("\n---- SISTEMA DE GESTÃO BANCÁRIA ----\n");
            System.out.println("Escolha o que deseja fazer:");
            System.out.println("1 - Cadastro de Conta Corrente");
            System.out.println("2 - Cadastro de Conta Poupança");
            System.out.println("3 - Cadastro de Conta de Investimento");
            System.out.println("4 - Visualizar Contas");
            System.out.println("0 - Encerrar \n");

            int acaoUser = input.nextInt();
            input.nextLine();

            if (acaoUser == 0){
                break;
            }else {
                switch (acaoUser) {
                    case 1:
                        System.out.println("Insira o número da conta: ");
                        String numeroCorrente = input.nextLine();
                        System.out.println("Insira o nome do titular: ");
                        String titularCorrente = input.nextLine();
                        System.out.println("Insira o saldo: ");
                        double saldoCorrente = input.nextDouble();
                        System.out.println("Insira o limite do cheque especial: ");
                        double limiteCorrente = input.nextDouble();

                        ContaCorrente newCorrente = new ContaCorrente(numeroCorrente,titularCorrente,saldoCorrente,limiteCorrente);
                        newCorrente.mostrarDados(true);
                        registroContas.add(newCorrente);
                        break;
                    case 2:
                        System.out.println("Insira o número da conta: ");
                        String numeroPoupanca = input.nextLine();
                        System.out.println("Insira o nome do titular: ");
                        String titularPoupanca = input.nextLine();
                        System.out.println("Insira o saldo: ");
                        double saldoPoupanca = input.nextDouble();
                        System.out.println("Insira a taxa de rendimento mensal: ");
                        double rendimentoPoupanca = input.nextDouble();

                        ContaPoupanca newPoupanca = new ContaPoupanca(numeroPoupanca, titularPoupanca, saldoPoupanca, rendimentoPoupanca);
                        newPoupanca.mostrarDados(true);
                        registroContas.add(newPoupanca);
                        break;
                    case 3:
                        System.out.println("Insira o número da conta: ");
                        String numeroInvestimento= input.nextLine();
                        System.out.println("Insira o nome do titular: ");
                        String titularInvestimento = input.nextLine();
                        System.out.println("Insira o saldo: ");
                        double saldoInvestimento = input.nextDouble();
                        System.out.println("Insira a Taxa de administração: ");
                        double taxaAdmin = input.nextDouble();

                        ContaInvestimento newInvestimento = new ContaInvestimento(numeroInvestimento, titularInvestimento, saldoInvestimento, taxaAdmin);
                        newInvestimento.mostrarDados(true);
                        registroContas.add(newInvestimento);
                        break;

                    case 4:
                        if (registroContas.isEmpty()){
                            System.out.println("Não há nenhuma conta cadastrada! ");
                        }else{
                            System.out.println("---- Registro de contas ----");
                            for( Conta conta : registroContas){
                                conta.mostrarDados();
                            }
                        }
                        break;

                    default:
                        System.out.println("Opção inválida, tente novamente.");
                }
            }
            //Tratamento de erro de tipo de dado
        } catch (InputMismatchException e) {
            System.out.println("Insira apenas números");
            input.nextLine();
            continue;
        }
    }
    }
}
