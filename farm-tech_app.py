"""
FarmTech Solutions - Aplicacao de apoio a Agricultura Digital
Culturas suportadas: Cafe e Cana-de-acucar
"""

import csv

CAFE = "Café"
CANA = "Cana-de-açúcar"
CULTURAS_VALIDAS = (CAFE, CANA)

CSV_PATH = "dados_talhoes.csv"
CSV_COLUNAS = [
    "cultura", "largura_m", "comprimento_m", "area_m2",
    "num_ruas", "produto", "taxa_ml_por_metro", "volume_litros",
]

talhoes = []


def exportar_csv():
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=CSV_COLUNAS)
        escritor.writeheader()
        for talhao in talhoes:
            escritor.writerow(talhao)


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Valor não pode ser vazio. Tente novamente.")


def ler_float(mensagem, minimo=0):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(valor)
            if numero <= minimo:
                print(f"Informe um número maior que {minimo}.")
                continue
            return numero
        except ValueError:
            print("Valor inválido. Digite um número, ex: 12.5")


def ler_int(mensagem, minimo=1):
    while True:
        valor = input(mensagem).strip()
        try:
            numero = int(valor)
            if numero < minimo:
                print(f"Informe um número inteiro maior ou igual a {minimo}.")
                continue
            return numero
        except ValueError:
            print("Valor inválido. Digite um número inteiro, ex: 10")


def escolher_cultura():
    print("\nCulturas disponíveis:")
    for indice, cultura in enumerate(CULTURAS_VALIDAS, start=1):
        print(f"  {indice} - {cultura}")
    while True:
        opcao = ler_int("Escolha a cultura pelo número: ", minimo=1)
        if opcao <= len(CULTURAS_VALIDAS):
            return CULTURAS_VALIDAS[opcao - 1]
        print("Opção inválida.")


def calcular_area_retangulo(largura_m, comprimento_m):
    return largura_m * comprimento_m


def calcular_volume_insumo_litros(taxa_ml_por_metro, comprimento_m, num_ruas):
    total_ml = taxa_ml_por_metro * comprimento_m * num_ruas
    return total_ml / 1000


def montar_talhao():
    cultura = escolher_cultura()
    largura_m = ler_float("Largura do talhão (m): ")
    comprimento_m = ler_float("Comprimento do talhão / de cada rua (m): ")
    num_ruas = ler_int("Número de ruas da lavoura: ")
    produto = ler_texto("Produto/insumo a aplicar (ex: Fosfato): ")
    taxa_ml_por_metro = ler_float("Taxa de aplicação (mL por metro de rua): ")

    return {
        "cultura": cultura,
        "largura_m": largura_m,
        "comprimento_m": comprimento_m,
        "area_m2": calcular_area_retangulo(largura_m, comprimento_m),
        "num_ruas": num_ruas,
        "produto": produto,
        "taxa_ml_por_metro": taxa_ml_por_metro,
        "volume_litros": calcular_volume_insumo_litros(taxa_ml_por_metro, comprimento_m, num_ruas),
    }


def cadastrar_talhao():
    print("\n--- Cadastro de novo talhão ---")
    talhao = montar_talhao()
    talhoes.append(talhao)
    exportar_csv()
    print(f"\nTalhão cadastrado com sucesso na posição {len(talhoes) - 1}.")
    exibir_talhao(talhao, len(talhoes) - 1)


def exibir_talhao(talhao, posicao):
    print(f"\n[{posicao}] Cultura: {talhao['cultura']}")
    print(f"    Dimensões: {talhao['largura_m']} m x {talhao['comprimento_m']} m")
    print(f"    Área de plantio: {talhao['area_m2']:.2f} m²")
    print(f"    Número de ruas: {talhao['num_ruas']}")
    print(f"    Insumo: {talhao['produto']} - {talhao['taxa_ml_por_metro']} mL/m")
    print(f"    Volume total necessário: {talhao['volume_litros']:.2f} litros")


def listar_talhoes():
    print("\n--- Talhões cadastrados ---")
    if not talhoes:
        print("Nenhum talhão cadastrado ainda.")
        return
    for posicao, talhao in enumerate(talhoes):
        exibir_talhao(talhao, posicao)


def escolher_posicao_existente():
    if not talhoes:
        print("Nenhum talhão cadastrado ainda.")
        return None
    listar_talhoes()
    while True:
        posicao = ler_int("Digite a posição do talhão (vetor começa em 0): ", minimo=0)
        if posicao < len(talhoes):
            return posicao
        print("Posição inválida.")


def atualizar_talhao():
    print("\n--- Atualizar talhão ---")
    posicao = escolher_posicao_existente()
    if posicao is None:
        return
    print("\nDigite os novos dados:")
    talhoes[posicao] = montar_talhao()
    exportar_csv()
    print("\nTalhão atualizado com sucesso.")
    exibir_talhao(talhoes[posicao], posicao)


def deletar_talhao():
    print("\n--- Deletar talhão ---")
    posicao = escolher_posicao_existente()
    if posicao is None:
        return
    removido = talhoes.pop(posicao)
    exportar_csv()
    print(f"\nTalhão da cultura {removido['cultura']} removido da posição {posicao}.")


def exibir_menu():
    print("\n" + "=" * 45)
    print("   FarmTech Solutions - Agricultura Digital")
    print("=" * 45)
    print("1 - Cadastrar talhão (entrada de dados)")
    print("2 - Listar talhões (saída de dados)")
    print("3 - Atualizar talhão")
    print("4 - Deletar talhão")
    print("5 - Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_talhao()
        elif opcao == "2":
            listar_talhoes()
        elif opcao == "3":
            atualizar_talhao()
        elif opcao == "4":
            deletar_talhao()
        elif opcao == "5":
            print("\nEncerrando o programa. Até logo!")
            break
        else:
            print("\nOpção inválida. Escolha um número de 1 a 5.")


if __name__ == "__main__":
    main()
