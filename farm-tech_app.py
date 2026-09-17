"""
FarmTech Solutions - Aplicacao de Agricultura Digital
======================================================
Suporta 2 culturas: Cafe e Cana-de-acucar.

- Cafe: area de plantio em forma de RETANGULO (talhao).
        Insumo: Fosfato, aplicado via pulverizacao no trator,
        na taxa de 500 mL por metro de rua (linha de plantio).
- Cana-de-acucar: area de plantio em forma de TRAPEZIO (talhao
        que acompanha a margem de uma estrada/curva de nivel).
        Insumo: Herbicida, aplicado na taxa de X litros por hectare.

Os dados sao armazenados em vetores (listas) paralelos, um vetor
por atributo, conforme pedido no enunciado do estudo de caso.
"""

import os

# ---------------------------------------------------------------------------
# VETORES DE DADOS (armazenamento paralelo por posicao)
# ---------------------------------------------------------------------------
# Cada posicao "i" nesses vetores representa UM registro de plantio.
vetor_cultura = []        # str: "Cafe" ou "Cana-de-acucar"
vetor_formato = []        # str: "Retangulo" ou "Trapezio"
vetor_dimensoes = []      # tuple: dimensoes usadas no calculo da area (em metros)
vetor_area_m2 = []        # float: area calculada em m2
vetor_insumo = []         # str: nome do insumo aplicado
vetor_taxa_insumo = []    # float: taxa do insumo (mL/metro ou L/ha, conforme cultura)
vetor_qtd_total_l = []    # float: quantidade TOTAL de insumo necessaria, em litros


# ---------------------------------------------------------------------------
# FUNCOES DE CALCULO DE AREA
# ---------------------------------------------------------------------------
def calcular_area_retangulo(comprimento, largura):
    """Area do talhao de Cafe: retangulo simples (comprimento x largura)."""
    return comprimento * largura


def calcular_area_trapezio(base_maior, base_menor, altura):
    """Area do talhao de Cana-de-acucar: trapezio ((B+b)/2 * h)."""
    return ((base_maior + base_menor) / 2) * altura


# ---------------------------------------------------------------------------
# FUNCOES DE CALCULO DE MANEJO DE INSUMOS
# ---------------------------------------------------------------------------
def calcular_insumo_cafe(num_ruas, comprimento_rua_m, taxa_ml_por_metro):
    """
    Cafe: pulverizacao de fosfato com o trator.
    Taxa informada em mL/metro de rua.
    Total (litros) = num_ruas * comprimento_da_rua(m) * taxa(mL/m) / 1000
    """
    total_ml = num_ruas * comprimento_rua_m * taxa_ml_por_metro
    total_litros = total_ml / 1000
    return total_litros


def calcular_insumo_cana(area_m2, taxa_l_por_hectare):
    """
    Cana-de-acucar: aplicacao de herbicida por hectare.
    1 hectare = 10.000 m2
    Total (litros) = (area_m2 / 10000) * taxa(L/ha)
    """
    area_ha = area_m2 / 10000
    total_litros = area_ha * taxa_l_por_hectare
    return total_litros


# ---------------------------------------------------------------------------
# FUNCOES AUXILIARES DE ENTRADA (com validacao via loop)
# ---------------------------------------------------------------------------
def ler_float(mensagem):
    """Le um numero float do usuario, repetindo (loop) ate ser valido."""
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(valor)
            if numero <= 0:
                print(">> O valor deve ser maior que zero. Tente novamente.")
                continue
            return numero
        except ValueError:
            print(">> Entrada invalida. Digite um numero (ex: 12.5).")


def ler_int(mensagem):
    """Le um numero inteiro do usuario, repetindo (loop) ate ser valido."""
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print(">> Entrada invalida. Digite um numero inteiro maior que zero.")


def pausar():
    input("\nPressione ENTER para continuar...")


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


# ---------------------------------------------------------------------------
# 1) ENTRADA DE DADOS (cadastro de um novo registro de plantio)
# ---------------------------------------------------------------------------
def cadastrar_dados():
    print("\n===== CADASTRO DE NOVO PLANTIO =====")
    print("1 - Cafe (area retangular)")
    print("2 - Cana-de-acucar (area trapezoidal)")

    opcao_cultura = input("Escolha a cultura (1/2): ").strip()

    if opcao_cultura == "1":
        # ---------- CAFE ----------
        cultura = "Cafe"
        formato = "Retangulo"

        print("\n-- Dados da area (retangulo) --")
        comprimento = ler_float("Comprimento do talhao (m): ")
        largura = ler_float("Largura do talhao (m): ")
        area = calcular_area_retangulo(comprimento, largura)
        dimensoes = (comprimento, largura)

        print("\n-- Manejo de insumo: Fosfato (pulverizacao com trator) --")
        num_ruas = ler_int("Quantidade de ruas (linhas de plantio): ")
        comprimento_rua = ler_float("Comprimento de cada rua (m): ")
        taxa = ler_float("Taxa de aplicacao (mL por metro de rua): ")

        insumo = "Fosfato"
        total_litros = calcular_insumo_cafe(num_ruas, comprimento_rua, taxa)

    elif opcao_cultura == "2":
        # ---------- CANA-DE-ACUCAR ----------
        cultura = "Cana-de-acucar"
        formato = "Trapezio"

        print("\n-- Dados da area (trapezio) --")
        base_maior = ler_float("Base maior do talhao (m): ")
        base_menor = ler_float("Base menor do talhao (m): ")
        altura = ler_float("Altura (distancia entre as bases, em m): ")
        area = calcular_area_trapezio(base_maior, base_menor, altura)
        dimensoes = (base_maior, base_menor, altura)

        print("\n-- Manejo de insumo: Herbicida (aplicacao por hectare) --")
        taxa = ler_float("Taxa de aplicacao (litros por hectare): ")

        insumo = "Herbicida"
        total_litros = calcular_insumo_cana(area, taxa)

    else:
        print(">> Opcao invalida. Cadastro cancelado.")
        return

    # Grava nos vetores paralelos (mesma posicao em todos os vetores)
    vetor_cultura.append(cultura)
    vetor_formato.append(formato)
    vetor_dimensoes.append(dimensoes)
    vetor_area_m2.append(area)
    vetor_insumo.append(insumo)
    vetor_taxa_insumo.append(taxa)
    vetor_qtd_total_l.append(total_litros)

    print(f"\n>> Registro cadastrado com sucesso na posicao {len(vetor_cultura) - 1}!")
    print(f">> Area calculada: {area:.2f} m2")
    print(f">> Total de {insumo.lower()} necessario: {total_litros:.2f} litros")


# ---------------------------------------------------------------------------
# 2) SAIDA DE DADOS (listagem no terminal)
# ---------------------------------------------------------------------------
def listar_dados():
    print("\n===== DADOS CADASTRADOS =====")
    if len(vetor_cultura) == 0:
        print("Nenhum registro cadastrado ainda.")
        return

    for i in range(len(vetor_cultura)):
        print(f"\n--- Posicao {i} ---")
        print(f"Cultura........: {vetor_cultura[i]}")
        print(f"Formato da area: {vetor_formato[i]}")
        print(f"Dimensoes (m)..: {vetor_dimensoes[i]}")
        print(f"Area calculada.: {vetor_area_m2[i]:.2f} m2")
        print(f"Insumo.........: {vetor_insumo[i]}")
        if vetor_cultura[i] == "Cafe":
            print(f"Taxa...........: {vetor_taxa_insumo[i]:.2f} mL/metro de rua")
        else:
            print(f"Taxa...........: {vetor_taxa_insumo[i]:.2f} L/hectare")
        print(f"Total necessario: {vetor_qtd_total_l[i]:.2f} litros")


# ---------------------------------------------------------------------------
# 3) ATUALIZACAO DE DADOS (numa posicao qualquer do vetor)
# ---------------------------------------------------------------------------
def atualizar_dados():
    print("\n===== ATUALIZACAO DE DADOS =====")
    if len(vetor_cultura) == 0:
        print("Nenhum registro cadastrado ainda.")
        return

    listar_dados()
    posicao = ler_int("\nDigite a posicao que deseja atualizar: ")

    if posicao < 0 or posicao >= len(vetor_cultura):
        print(">> Posicao invalida.")
        return

    print(f"\nAtualizando registro da cultura: {vetor_cultura[posicao]}")

    if vetor_cultura[posicao] == "Cafe":
        comprimento = ler_float("Novo comprimento do talhao (m): ")
        largura = ler_float("Nova largura do talhao (m): ")
        area = calcular_area_retangulo(comprimento, largura)
        vetor_dimensoes[posicao] = (comprimento, largura)

        num_ruas = ler_int("Nova quantidade de ruas: ")
        comprimento_rua = ler_float("Novo comprimento de cada rua (m): ")
        taxa = ler_float("Nova taxa de aplicacao (mL/metro): ")
        total_litros = calcular_insumo_cafe(num_ruas, comprimento_rua, taxa)

    else:  # Cana-de-acucar
        base_maior = ler_float("Nova base maior (m): ")
        base_menor = ler_float("Nova base menor (m): ")
        altura = ler_float("Nova altura (m): ")
        area = calcular_area_trapezio(base_maior, base_menor, altura)
        vetor_dimensoes[posicao] = (base_maior, base_menor, altura)

        taxa = ler_float("Nova taxa de aplicacao (L/hectare): ")
        total_litros = calcular_insumo_cana(area, taxa)

    vetor_area_m2[posicao] = area
    vetor_taxa_insumo[posicao] = taxa
    vetor_qtd_total_l[posicao] = total_litros

    print(f"\n>> Registro na posicao {posicao} atualizado com sucesso!")


# ---------------------------------------------------------------------------
# 4) DELECAO DE DADOS
# ---------------------------------------------------------------------------
def deletar_dados():
    print("\n===== DELECAO DE DADOS =====")
    if len(vetor_cultura) == 0:
        print("Nenhum registro cadastrado ainda.")
        return

    listar_dados()
    posicao = ler_int("\nDigite a posicao que deseja deletar: ")

    if posicao < 0 or posicao >= len(vetor_cultura):
        print(">> Posicao invalida.")
        return

    confirmacao = input(f"Confirma a delecao do registro {posicao} ({vetor_cultura[posicao]})? (S/N): ").strip().upper()
    if confirmacao == "S":
        vetor_cultura.pop(posicao)
        vetor_formato.pop(posicao)
        vetor_dimensoes.pop(posicao)
        vetor_area_m2.pop(posicao)
        vetor_insumo.pop(posicao)
        vetor_taxa_insumo.pop(posicao)
        vetor_qtd_total_l.pop(posicao)
        print(">> Registro deletado com sucesso!")
    else:
        print(">> Operacao cancelada.")


# ---------------------------------------------------------------------------
# EXTRA: EXPORTAR DADOS PARA CSV (usado depois pelo script em R)
# ---------------------------------------------------------------------------
def exportar_csv(caminho="dados_lavoura.csv"):
    print("\n===== EXPORTAR DADOS PARA CSV =====")
    if len(vetor_cultura) == 0:
        print("Nenhum registro cadastrado ainda. Nada para exportar.")
        return

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write("cultura,formato,area_m2,insumo,taxa,qtd_total_litros\n")
        for i in range(len(vetor_cultura)):
            linha = (
                f"{vetor_cultura[i]},{vetor_formato[i]},"
                f"{vetor_area_m2[i]:.2f},{vetor_insumo[i]},"
                f"{vetor_taxa_insumo[i]:.2f},{vetor_qtd_total_l[i]:.2f}\n"
            )
            arquivo.write(linha)

    print(f">> Dados exportados para '{caminho}' com sucesso!")
    print(">> Esse arquivo pode ser lido pelo script estatisticas.R")


# ---------------------------------------------------------------------------
# MENU PRINCIPAL
# ---------------------------------------------------------------------------
def exibir_menu():
    print("\n" + "=" * 45)
    print("   FARMTECH SOLUTIONS - AGRICULTURA DIGITAL")
    print("=" * 45)
    print("1 - Entrada de dados (cadastrar plantio)")
    print("2 - Saida de dados (listar registros)")
    print("3 - Atualizar dados")
    print("4 - Deletar dados")
    print("5 - Exportar dados para CSV (integracao com R)")
    print("6 - Sair do programa")
    print("=" * 45)


def main():
    opcao = None
    while opcao != "6":
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_dados()
        elif opcao == "2":
            listar_dados()
        elif opcao == "3":
            atualizar_dados()
        elif opcao == "4":
            deletar_dados()
        elif opcao == "5":
            exportar_csv()
        elif opcao == "6":
            print("\nEncerrando o programa. Ate logo!")
        else:
            print(">> Opcao invalida. Escolha um numero de 1 a 6.")

        if opcao != "6":
            pausar()


if __name__ == "__main__":
    main()