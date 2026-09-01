"""Sistema de Gestão de Notas de Alunos.

Programa desenvolvido para a aula prática de Funções em Python.

Funcionalidades:
    - Cadastro de notas;
    - Armazenamento das notas em uma lista;
    - Cálculo da média;
    - Determinação da situação do aluno;
    - Exibição do relatório final.
"""

from notas import adicionar_nota, calcular_media, verificar_situacao
from relatorio import gerar_relatorio


def solicitar_quantidade_notas() -> int:
    """Solicita ao usuário a quantidade de notas que serão cadastradas.

    Returns:
        Quantidade de notas a serem cadastradas.
    """
    while True:
        try:
            quantidade = int(input("Quantas notas deseja cadastrar? "))

            if quantidade > 0:
                return quantidade

            print("A quantidade deve ser maior que zero.")

        except ValueError:
            print("Digite um número inteiro válido.")


def solicitar_nota(numero: int) -> float:
    """Solicita uma nota válida ao usuário.

    Args:
        numero: Número da nota que está sendo solicitada.

    Returns:
        Nota informada pelo usuário, entre 0 e 10.
    """
    while True:
        try:
            nota = float(input(f"Digite a {numero}ª nota (0 a 10): "))

            if 0 <= nota <= 10:
                return nota

            print("A nota deve estar entre 0 e 10.")

        except ValueError:
            print("Digite uma nota numérica válida.")


def main() -> None:
    """Executa o fluxo principal do sistema."""
    print("=" * 40)
    print("   SISTEMA DE GESTÃO DE NOTAS")
    print("=" * 40)

    notas: list[float] = []

    quantidade = solicitar_quantidade_notas()

    for numero in range(1, quantidade + 1):
        nota = solicitar_nota(numero)
        adicionar_nota(notas, nota)

    media = calcular_media(notas)
    situacao = verificar_situacao(media)

    gerar_relatorio(notas, media, situacao)


if __name__ == "__main__":
    main()

