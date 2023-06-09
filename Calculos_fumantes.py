# Escreva um programa para calcular a redução do tempo de vida de um fumante.

def calcular_reducao_tempo_de_vida(cigarros_por_dia, anos_fumando):
    # Número médio de minutos perdidos por cigarro fumado
    minutos_perdidos_por_cigarro = 11

    # Cálculo do número total de cigarros fumados
    cigarros_totais = cigarros_por_dia * 365 * anos_fumando

    # Cálculo do tempo total perdido em minutos
    tempo_perdido_minutos = cigarros_totais * minutos_perdidos_por_cigarro

    # Conversão do tempo perdido para dias
    tempo_perdido_dias = tempo_perdido_minutos / (60 * 24)

    return tempo_perdido_dias

# Exemplo de uso do programa
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Há quantos anos você fuma? "))

reducao_tempo_de_vida = calcular_reducao_tempo_de_vida(cigarros_por_dia, anos_fumando)
print("A estimativa de redução do tempo de vida é de aproximadamente", reducao_tempo_de_vida, "dias.")