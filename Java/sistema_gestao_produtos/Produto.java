public class Produto {

    private String nome;
    private double preco;
    private int quantidadeEmEstoque;

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }
    public void setPreco(double preco) {
        if(preco > 0) {
            this.preco = preco;
        }
        else{
            System.out.println("Preço Inválido");
        }
    }

    public int getQuantidadeEmEstoque() {
        return quantidadeEmEstoque;
    }
    public void setQuantidadeEmEstoque(int quantidadeEmEstoque) {
        if(quantidadeEmEstoque >= 0) {
            this.quantidadeEmEstoque = quantidadeEmEstoque;
        }
        else{
            System.out.println("Quantidade Inválida");
        }
    }


    public Produto(String nome, double preco, int quantidadeEmEstoque) {
        this.nome = nome;
        this.preco = preco;
        this.quantidadeEmEstoque = quantidadeEmEstoque;

    }

    public void exibirDetalhes(){
        System.out.println("NOME: " + nome);
        System.out.println("PRECO: " + preco);
        System.out.println("QUANTIDADE EM ESTOQUE: " + quantidadeEmEstoque);

    }
}