#Importações e Configurações Iniciais
import json
from random import choice
import os

#Boas-vindas
print(
'''
Bem-vindo(a) ao jogo da forca!

Informações:

Acertar uma letra = +10 pontos
Se a letra aparecer mais de uma vez, você ganha 10 pontos por cada aparição.

Errar uma letra = -5 pontos
Uma pequena penalidade para desencorajar chutes aleatórios.

Vencer o jogo = +50 pontos

Perder o jogo = Zera a pontuação

Se o boneco for completado (6 tentativas), o jogador perde todos os pontos acumulados naquela rodada.

Vamos começar!''')

#Listas principais
palavras_faceis = ['carro', 'casa', 'moto', 'gato', 'livro', 'nuvem', 'praia', 'solto', 'rato', 'pedra', 'leão', 'corda', 'tinta']
palavras_medias = ['janela', 'caderno', 'amarelo', 'escova', 'jornal', 'laranja', 'mochila', 'natalia', 'penteado', 'risquei', 'travesa', 'sabendo', 'meninas']
palavras_dificeis = ['abacateiro', 'telefonema', 'caminhadas', 'adormecido', 'criatividade', 'esquecendo', 'formigueiro', 'lembranças', 'aviamentos', 'moderadora', 'esperança', 'enxurradas','brincadeira']

lista_partes_do_corpo = [
    '''



    ''',
    '''
        O


    ''',
    '''
        O
        |

    ''',
    '''
        O
       /|

    ''',
    '''
        O
       /|\\

    ''',
    '''
        O
       /|\\
       /
    ''',
    '''
        O
       /|\\
       / \\
    '''
]

ARQUIVO_DADOS_USUARIOS = 'dados_jogadores.json'
usuarios = {}

def carregar_dados_usuarios():
    if os.path.exists(ARQUIVO_DADOS_USUARIOS):
        try:
            with open(ARQUIVO_DADOS_USUARIOS, 'r', encoding='utf-8') as f:
                if os.fstat(f.fileno()).st_size == 0:
                    return {}
                return json.load(f)
        except json.JSONDecodeError:
            print("\nAviso: Arquivo de dados de usuários corrompido ou vazio. Criando novo.")
            return {}
    return {}

def salvar_dados_usuarios():
    with open(ARQUIVO_DADOS_USUARIOS, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4)

def mostrar_forca(qtd_erros):
    print(lista_partes_do_corpo[qtd_erros])

def exibir_status_jogo(letras_acertadas, letras_utilizadas, erros, pontuacao_atual):
    print('='*50)
    print('Jogo da Forca'.center(50))
    print('='*50)
    mostrar_forca(erros)
    print('\n' + ' '.join(letras_acertadas).center(50))
    print(f'Letras utilizadas: {", ".join(sorted(list(letras_utilizadas)))}')
    print(f'Pontuação da rodada: {pontuacao_atual} pontos')
    print('='*50)

def jogar_forca(usuario_atual):
    dificuldades = ['F', 'M', 'D']
    dificuldade_selecionada = ''

    while not dificuldade_selecionada:
        try:
            dificuldade_selecionada = str(input('Dificuldade [F, M, D]: ')).upper()[0]
            if dificuldade_selecionada not in dificuldades:
                print('Opção inválida. Tente novamente.')
                dificuldade_selecionada = ''
        except IndexError:
            print('Entrada vazia. Tente novamente.')

    if dificuldade_selecionada == dificuldades[0]:
        palavra_selecionada = choice(palavras_faceis)
    elif dificuldade_selecionada == dificuldades[1]:
        palavra_selecionada = choice(palavras_medias)
    elif dificuldade_selecionada == dificuldades[2]:
        palavra_selecionada = choice(palavras_dificeis)

    letras_acertadas = ['_' for _ in palavra_selecionada]
    letras_utilizadas = set()
    erros = 0
    pontuacao_rodada = 0

    print('\nVamos começar a adivinhar a palavra!')
    exibir_status_jogo(letras_acertadas, letras_utilizadas, erros, pontuacao_rodada)

    while True:
        letra_jogador = str(input('Insira uma letra: ')).lower()

        if not letra_jogador.isalpha() or len(letra_jogador) != 1:
            print('Por favor, insira apenas uma única letra do alfabeto.')
            continue

        if letra_jogador in letras_utilizadas:
            print('Letra já utilizada, tente novamente!')
            continue

        letras_utilizadas.add(letra_jogador)

        if letra_jogador in palavra_selecionada:
            acertos_na_rodada = 0
            for i in range(len(palavra_selecionada)):
                if letra_jogador == palavra_selecionada[i]:
                    if letras_acertadas[i] == '_':
                        letras_acertadas[i] = letra_jogador
                        pontuacao_rodada += 10
                        acertos_na_rodada += 1
            if acertos_na_rodada > 0:
                print(f'\nAcertou! A letra "{letra_jogador}" apareceu {acertos_na_rodada} vez(es).')
            else:
                print(f'\nA letra "{letra_jogador}" já foi revelada!')
        else:
            print(f'\nErrou! A letra "{letra_jogador}" não está na palavra.')
            erros += 1
            pontuacao_rodada -= 5

        if pontuacao_rodada < 0:
            pontuacao_rodada = 0

        exibir_status_jogo(letras_acertadas, letras_utilizadas, erros, pontuacao_rodada)

        if '_' not in letras_acertadas:
            print(f'\n🎉 Parabéns, você acertou! A palavra era: "{palavra_selecionada.upper()}" 🎉')
            pontuacao_rodada += 50
            print(f'Você ganhou 50 pontos por vencer! Pontuação final da rodada: {pontuacao_rodada}')
            usuarios[usuario_atual] += pontuacao_rodada
            salvar_dados_usuarios()
            break
        elif erros == 6:
            print(f'\nVocê perdeu! 💀 O boneco foi completado. A palavra era: "{palavra_selecionada.upper()}"')
            pontuacao_rodada = 0
            print(f'Sua pontuação nesta rodada foi zerada.')
            salvar_dados_usuarios()
            break

def excluir_usuario():
    global usuarios
    print("\n--- Excluir Usuário ---")
    if not usuarios:
        print("Nenhum usuário para excluir.")
        return False

    usuario_para_excluir = input("Digite o nome do usuário que deseja excluir: ").lower()

    if usuario_para_excluir in usuarios:
        confirmacao = input(f"Tem certeza que deseja excluir '{usuario_para_excluir}'? (sim/nao): ").lower()
        if confirmacao == 'sim':
            del usuarios[usuario_para_excluir]
            salvar_dados_usuarios()
            print(f"Usuário '{usuario_para_excluir}' excluído com sucesso!")
            return True
        else:
            print("Exclusão cancelada.")
    else:
        print(f"Usuário '{usuario_para_excluir}' não encontrado.")
    print("-----------------------\n")
    return False

def login_registro():
    while True:
        cadastro = input("Você já tem um usuário? (sim/nao): ").lower()
        print("")
        if cadastro == "sim":
            antigo_user = input("Digite o seu nome de usuário: ").lower()
            if antigo_user in usuarios:
                print(f"Bem-vindo(a) de volta, {antigo_user}!")
                return antigo_user
            else:
                print("Usuário não encontrado. Tente novamente ou crie um novo.")
                print("")
        elif cadastro == "nao":
            novo_user = input("Digite seu novo usuário: ").lower()
            if novo_user in usuarios:
                print("Este usuário já existe. Por favor, faça o login ou escolha outro nome.")
                print("")
            else:
                usuarios[novo_user] = 0
                salvar_dados_usuarios()
                print(f"Novo usuário '{novo_user}' registrado com sucesso!")
                return novo_user
        else:
            print("Por favor, digite 'sim' ou 'nao'.")
            print("")

def exibir_ranking():
    print("\n" + "="*50)
    print("RANKING - TOP 5".center(50))
    print("="*50)

    ranking = sorted(usuarios.items(), key=lambda item: item[1], reverse=True)

    if not ranking:
        print("Nenhum jogador registrado ainda.".center(50))
    else:
        for i, (nome, pontos) in enumerate(ranking[:5]):
            print(f"{i+1}º - {nome.title()} - {pontos} pontos")

    print("="*50 + "\n")

usuarios = carregar_dados_usuarios()
atual_user = login_registro()

while True:
    print(f"\nOlá, {atual_user}! Sua pontuação atual é: {usuarios.get(atual_user, 0)}")
    exibir_ranking()

    jogar_forca(atual_user)

    while True:
        try:
            entrada_usuario = input('''\nO que você deseja fazer agora?
1 - Jogar novamente (mesma conta);
2 - Trocar de conta;
3 - Mostrar ranking;
4 - Excluir um usuário;
5 - Sair do programa.
Digite sua opção: ''')
            print("")

            if not entrada_usuario:
                print('Entrada inválida. Por favor, digite um número.')
                continue

            continuar = int(entrada_usuario)

            if continuar == 1:
                print("Preparando uma nova rodada...")
                break
            elif continuar == 2:
                atual_user = login_registro()
                print("Conta trocada. Preparando uma nova rodada...")
                break
            elif continuar == 3:
                exibir_ranking()
            elif continuar == 4:
                usuario_excluido = excluir_usuario()
                if usuario_excluido and atual_user not in usuarios:
                    print("Seu usuário foi excluído. Por favor, registre-se ou faça login com outra conta.")
                    atual_user = login_registro()
                    break
            elif continuar == 5:
                print("Obrigado por jogar! Até a próxima!")
                exit()
            else:
                print('Opção inválida. Por favor, digite um número entre 1 e 5.')

        except ValueError:
            print('Entrada inválida. Por favor, digite apenas o número da opção.')