import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Produto> produtos = new ArrayList<>();

        while (true) {

            System.out.println("Olá, este é um Sistema de Gestão de Produtos.\n");
            System.out.println("O que você deseja fazer?\n" +
                    "0 - Sair\n" +
                    "1 - Criar novo produto\n" +
                    "2 - Alterar preço\n" +
                    "3 - Alterar quantidade\n" +
                    "4 - Listar produtos\n");
            int operacaoUser = input.nextInt();
            switch (operacaoUser) {
                case 0:
                    System.out.println("Saindo...👋");
                    input.close();
                    return;
                case 1:
                    input.nextLine();
                    System.out.println("Digite o nome do produto: ");
                    String nomeProduto = input.nextLine();
                    System.out.println("Digite o preço:");
                    double precoProduto = input.nextDouble();
                    System.out.println("Digite o quantidade:");
                    int quantidadeProduto = input.nextInt();
                    input.nextLine(); // limpa o buffer
                    Produto produto = new Produto(nomeProduto, precoProduto, quantidadeProduto);
                    produtos.add(produto);
                    break;

                case 2:
                    System.out.println("Digite o indice do produto");
                    int indiceProduto2 = input.nextInt();

                    System.out.println("Digite o preço:");
                    double alterarPreco = input.nextDouble();
                    produtos.get(indiceProduto2).setPreco(alterarPreco);
                    break;

                case 3:
                    System.out.println("Digite o indice do produto");
                    int indiceProduto3= input.nextInt();
                    input.nextLine();
                    System.out.println("Digite o quantidade:");
                    int alterarQuantidade = input.nextInt();
                    produtos.get(indiceProduto3).setQuantidadeEmEstoque(alterarQuantidade);
                    break;

                case 4:
                    System.out.println("Listar todos os itens(0) ----- Apenas um(1)");
                    int opcao = input.nextInt();
                    switch ()
                    System.out.println("Digite o indice do produto");
                    int indiceProduto4 = input.nextInt();
                    produtos.get(indiceProduto4).exibirDetalhes();
                    break;

                default:
                    System.out.println("Opção inválida");
            }
        }
    }
}