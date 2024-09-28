import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Lendo a base de dados csv
Base_de_dados = pd.read_csv('StudentsPerformance.csv')

# Renomeando colunas
Base_de_dados.rename(columns={
    'Unnamed: 0': 'Id',
    'gender': 'genero',
    'race/ethnicity': 'Raça/etnia',
    'parental level of education': 'educação dos pais',
    'lunch': 'Almoço',
    'test preparation course': 'curso de preparação',
    'math score': 'matematica',
    'reading score': 'leitura',
    'writing score': 'escrita',
}, inplace=True)

# Analisando Campos Nulos
Nulos = Base_de_dados.isnull()
plt.figure(figsize=(16, 8))
plt.title("Análise de Campos Nulos")
sns.heatmap(Nulos, cbar=False)
plt.savefig("Analise_Campos_Nulos.png")  # Salvar o gráfico
plt.show()

# Analisando Campos Únicos
Unicos = Base_de_dados.nunique()
plt.figure(figsize=(15, 8))
plt.title("Análise de Campos Únicos")
sns.barplot(x=Unicos.index, y=Unicos.values)
plt.xticks(rotation=90)
plt.savefig("Analise_Campos_Unicos.png")  # Salvar o gráfico
plt.show()

# Dados duplicados
print('Dados duplicados:', Base_de_dados.duplicated().sum())

# Estatística descritiva
print(Base_de_dados.describe())

# Informações da base de dados
print(Base_de_dados.info())

# Análise de porcentagens
print("Gênero")
print(Base_de_dados['genero'].value_counts(normalize=True) * 100)
print("Raça/etnia")
print(Base_de_dados['Raça/etnia'].value_counts(normalize=True) * 100)
print("Educação parental")
print(Base_de_dados['educação dos pais'].value_counts(normalize=True) * 100)
print("Almoço")
print(Base_de_dados['Almoço'].value_counts(normalize=True) * 100)
print("Curso de preparação")
print(Base_de_dados['curso de preparação'].value_counts(normalize=True) * 100)
print('\n')

# Renomeando linhas
Base_de_dados['genero'] = Base_de_dados['genero'].replace({'male': 'masculino', 'female': 'feminino'})

# Gráficos
plt.title("Matemática/Gênero")
sns.boxplot(data=Base_de_dados, x='matematica', y='genero', palette={'masculino': 'lightblue', 'feminino': 'lightpink'})
plt.savefig("Matematica_Genero.png")  # Salvar o gráfico
plt.show()

plt.title("Escrita/Gênero")
sns.boxplot(data=Base_de_dados, x='escrita', y='genero', hue='genero', palette={'masculino': 'lightblue', 'feminino': 'lightpink'}, legend=False)
plt.savefig("Escrita_Genero.png")  # Salvar o gráfico
plt.show()

print(Base_de_dados.groupby(by=['genero']).describe()['matematica'].reset_index(), '\n')

plt.title("Raça/etnia em geral")
sns.pairplot(Base_de_dados, hue='Raça/etnia')
plt.savefig("Raca_Etnia_Geral.png")  # Salvar o gráfico
plt.show()

print(Base_de_dados.groupby(by=['Raça/etnia']).describe()['leitura'].reset_index())

plt.title("Matemática/Raça/etnia")
sns.boxplot(data=Base_de_dados, x='matematica', y='Raça/etnia')
plt.savefig("Matematica_Raca_Etnia.png")  # Salvar o gráfico
plt.show()

plt.title("Matemática/Educação dos pais")
sns.boxplot(data=Base_de_dados, x='matematica', y='educação dos pais')
plt.savefig("Matematica_Educacao_Pais.png")  # Salvar o gráfico
plt.show()

plt.title("Matemática / Leitura")
sns.scatterplot(data=Base_de_dados, x='matematica', y='leitura')
plt.savefig("Matematica_Leitura.png")  # Salvar o gráfico
plt.show()
