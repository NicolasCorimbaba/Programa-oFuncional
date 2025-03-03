#Vioria= 3 pontos
#Empate= 1 ponto
#Derrota = 0 ponto
partidas = [
    {"time": "Cruzeiro", "vitorias": 10, "empates": 5, "derrotas": 3},
    {"time": "São Paulo", "vitorias": 15, "empates": 3, "derrotas": 0},
    {"time": "Flamengo", "vitorias": 7, "empates": 8, "derrotas": 3},
    {"time": "Vasco", "vitorias": 3, "empates": 4, "derrotas": 11},
    {"time": "Corinthians", "vitorias": 0, "empates": 0, "derrotas": 18},
]

pontos = []
for time in partidas:
    pontos.append(time["vitorias"] * 3 + time["empates"])

times_acima_30 = []
for time, pontuacao in zip(partidas, pontos):
    if pontuacao > 30:
        times_acima_30.append(time)


total_pontos = 0
for pontuacao in pontos:
    total_pontos += pontuacao
media_pontos = total_pontos / len(pontos)

print("Imperativo:")
print(f"Pontos por time: {[f'{time["time"]}: {pontuacao}' for time, pontuacao in zip(partidas, pontos)]}")
print(f"Times com mais de 30 pontos: {[time["time"] for time in times_acima_30]}")
print(f"Média de pontos: {media_pontos:.2f}")


from functools import reduce


pontos = list(map(lambda time: time["vitorias"] * 3 + time["empates"], partidas))


times_acima_30 = list(filter(lambda time: time["vitorias"] * 3 + time["empates"] > 30, partidas))


media_pontos = reduce(lambda acc, pontuacao: acc + pontuacao, pontos) / len(pontos)

print("\nFuncional:")
print(f"Pontos por time: {[f'{time["time"]}: {pontuacao}' for time, pontuacao in zip(partidas, pontos)]}")
print(f"Times com mais de 30 pontos: {[time["time"] for time in times_acima_30]}")
print(f"Média de pontos: {media_pontos:.2f}")


# Relatório   
# Problema:
# Analisar o desempenho de times de futebol com base em vitórias, empates e derrotas, extraindo insights como
# pontuação total, times destacados com mais de 30 pontos e a média de pontos dos times.
#
# Vantagem da implementação funcional:
# - Redução do código boilerplate: as funções map, filter e reduce encapsulam operações comuns, reduzindo a repetição.
# - Maior legibilidade: o código funcional é mais direto e expressa claramente a lógica de cada transformação.
# - Modularidade: as funções de alta ordem podem ser reutilizadas e combinadas de forma flexível.
# - Potencial para paralelismo: em alguns contextos, o paradigma funcional facilita a execução em paralelo, otimizando o desempenho.
