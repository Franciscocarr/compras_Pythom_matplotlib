import matplotlib.pyplot as plt

# Dados de compras trimestrais
meses = ['Janeiro', 'Fevereiro', 'Março']
compras = [500000, 223000, 180000]
pesos = [31, 28, 31]  # dias em cada mês

# Cálculos das médias
media_simples = sum(compras) / 3
media_harmonica = 3 / (1/compras[0] + 1/compras[1] + 1/compras[2])
media_ponderada = sum(peso * compra for peso, compra in zip(pesos, compras)) / sum(pesos)

# Criando o gráfico
plt.figure(figsize=(12, 6))

# Gráfico de barras das compras por mês
plt.subplot(1, 2, 1)
bars = plt.bar(meses, compras, color=['blue', 'green', 'red'])
plt.title('Compras Trimestrais por Mês')
plt.ylabel('Valor (R$)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionando valores nas barras
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'R${height:,.0f}',
             ha='center', va='bottom')

# Gráfico de barras das médias
plt.subplot(1, 2, 2)
medias = [media_simples, media_harmonica, media_ponderada]
nomes_medias = ['Média Simples', 'Média Harmônica', 'Média Ponderada']
colors = ['purple', 'orange', 'brown']
bars_medias = plt.bar(nomes_medias, medias, color=colors)
plt.title('Comparação das Médias Trimestrais')
plt.ylabel('Valor (R$)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionando valores nas barras
for bar in bars_medias:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'R${height:,.0f}',
             ha='center', va='bottom')

# Ajustando layout e mostrando o gráfico
plt.tight_layout()
plt.show()

# Imprimindo os resultados no console
print("\nCompras trimestrais:")
for mes, valor in zip(meses, compras):
    print(f"{mes}: R${valor:,.2f}")

print("\nMédias calculadas:")
print(f"Média Simples: R${media_simples:,.2f}")
print(f"Média Harmônica: R${media_harmonica:,.2f}")
print(f"Média Ponderada: R${media_ponderada:,.2f}")