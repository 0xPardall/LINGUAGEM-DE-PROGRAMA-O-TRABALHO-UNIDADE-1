"""Funções relacionadas ao gerenciamento das notas dos alunos."""


def adicionar_nota(notas: list[float], nota: float) -> None:
    """Adiciona uma nota à lista de notas.

    Args:
        notas: Lista onde a nota será armazenada.
        nota: Nota que será adicionada.
    """
    notas.append(nota)


def calcular_media(notas: list[float]) -> float:
    """Calcula a média aritmética das notas.

    Args:
        notas: Lista contendo as notas do aluno.

    Returns:
        A média das notas.

    Raises:
        ValueError: Caso a lista de notas esteja vazia.
    """
    if not notas:
        raise ValueError("Não é possível calcular a média sem notas.")

    return sum(notas) / len(notas)


def verificar_situacao(media: float) -> str:
    """Determina a situação do aluno com base na média.

    A regra definida pela atividade é:
        - Média maior ou igual a 7: aprovado.
        - Média menor que 7: reprovado.

    Args:
        media: Média final do aluno.

    Returns:
        "Aprovado" ou "Reprovado".
    """
    if media >= 7:
        return "Aprovado"

    return "Reprovado"

