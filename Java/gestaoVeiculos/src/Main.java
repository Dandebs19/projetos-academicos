import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Veiculo> vehicles = new ArrayList<>();
        Scanner input = new Scanner(System.in);

        while (true) {
            System.out.println("\n---- Sistema de Gestão de veículos ----\n");
            System.out.println("O que você deseja fazer?");
            System.out.println("0 - Sair");
            System.out.println("1 - Cadastrar Veículo" );
            System.out.println("2 - Remover Veículo");
            System.out.println("3 - Listar Veículos");
            int option = input.nextInt();
            input.nextLine();

            switch (option) {
                case 0:
                    System.out.println("Saindo...");
                    input.close();
                    System.exit(0);
                    break;

                case 1:
                    System.out.println("Tipo de veículo:\n");
                    System.out.println("1 - Carro");
                    System.out.println("2 - Moto");
                    System.out.println("3 - Caminhão");
                    int typeVehicle1 = input.nextInt();
                    input.nextLine();

                    switch (typeVehicle1) {
                        case 1:
                            System.out.println("Digite a marca: ");
                            String carMake = input.nextLine();
                            System.out.println("Digite a placa: ");
                            String carLicensePlate = input.nextLine();
                            System.out.println("Digite o preço: ");
                            double carPrice = input.nextDouble();
                            System.out.println("Digite a quantidade de Portas: ");
                            int carDoors = input.nextInt();
                            input.nextLine();
                            Carro newCar = new Carro(carLicensePlate, carMake, carPrice, carDoors);
                            vehicles.add(newCar);
                            System.out.println("Cadastrado com sucesso!");
                            break;

                        case 2:
                            System.out.println("Digite a marca: ");
                            String mcMake = input.nextLine();
                            System.out.println("Digite a placa: ");
                            String mcLicensePlate = input.nextLine();
                            System.out.println("Digite o preço: ");
                            double mcPrice = input.nextDouble();
                            System.out.println("Digite as cilindradas: ");
                            int mcCylindercap = input.nextInt();
                            input.nextLine();
                            Moto newMotorcycle = new Moto(mcLicensePlate, mcMake, mcPrice, mcCylindercap);
                            vehicles.add(newMotorcycle);
                            System.out.println("Cadastrado com sucesso!");
                            break;

                        case 3:
                            System.out.println("Digite a marca: ");
                            String truckMake = input.nextLine();
                            System.out.println("Digite a placa: ");
                            String truckLicensePlate = input.nextLine();
                            System.out.println("Digite o preço: ");
                            double truckPrice = input.nextDouble();
                            System.out.println("Digite a capacidade de carga: ");
                            int truckLoadCap = input.nextInt();
                            input.nextLine();
                            Caminhao newTruck = new Caminhao(truckLicensePlate, truckMake, truckPrice, truckLoadCap);
                            vehicles.add(newTruck);
                            break;

                        default:
                            System.out.println("Opção inválida, tente novamente!");
                    }
                    break;
                case 2:
                    System.out.println("Insira a placa do veículo a ser removida:\n");
                    String licensePlate = input.nextLine();
                    boolean findVehicle = false;

                    for (int i = 0; i < vehicles.size(); i++) {
                        if (vehicles.get(i).getPlaca().equals(licensePlate)) {
                            vehicles.remove(i);
                            findVehicle = true;
                            System.out.println("Veículo removido!");
                            break;
                        }
                        if (!findVehicle) {
                            System.out.println("Não encontrado");
                        }
                    }
                    break;
                case 3:
                    if(vehicles.isEmpty()){
                        System.out.println("Nenhum veículo cadastrado!");

                    } else {
                        System.out.println("---- LISTA DE VEÍCULOS ----\n");
                        for (Veiculo v : vehicles) {
                            v.mostrarDados();
                        }
                    }
                    break;

                default:
                    System.out.println("Opção Inválida, insira um número valido! ");
            }
        }
    }
}

