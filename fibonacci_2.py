#Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.


def verifica_fibonacci(numero):
    """
    Verifica se um número pertence à sequência de Fibonacci.

    Args:
      numero: O número a ser verificado.

    Returns:
      Uma string informando se o número pertence ou não à sequência.
    """
    a = 0
    b = 1

    # Casos especiais para 0 e 1
    if numero == a or numero == b:
        return f"O número {numero} pertence à sequência de Fibonacci."

    while b < numero:
        a, b = b, a + b

    if b == numero:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."


# Entrada do usuário
numero_informado = int(input("Digite um número inteiro: "))

# Verificação e exibição do resultado
resultado = verifica_fibonacci(numero_informado)
print(resultado)