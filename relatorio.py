"""Funções responsáveis pela geração do relatório final."""


def gerar_relatorio(
    notas: list[float],
    media: float,
    situacao: str,
) -> None:
    """Exibe o relatório final do aluno.

    Args:
        notas: Lista de notas cadastradas.
        media: Média calculada.
        situacao: Situação final do aluno.
    """
    print()
    print("=" * 40)
    print("          RELATÓRIO FINAL")
    print("=" * 40)

    print("\nNotas cadastradas:")

    for indice, nota in enumerate(notas, start=1):
        print(f"  Nota {indice}: {nota:.2f}")

    print(f"\nMédia final: {media:.2f}")
    print(f"Situação: {situacao}")

    print("=" * 40)

