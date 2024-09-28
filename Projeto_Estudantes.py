# O projeto consiste em analisar o desempenho de alunos e ver se a influência dos antecedentes dos pais.


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Lendo a base de dados csv

Base_de_dados = pd.read_csv('StudentsPerformance.csv')


print(Base_de_dados)



Base_de_dados.rename ( columns ={'Unnamed: 0': 'Id',
                                 'gender':'genero',
                                 'race/ethnicity':'Raça/etnia',
                                 'parental level of education':'educação dos pais',
                                 'lunch':'Almoço',
                                 'test preparation course':'curso de preparação',
                                 'math score':'matematica',
                                 'reading score':'leitura',
                                 'writing score':'escrita',
                                  },inplace= True )

# Campos Nulos

Nulos = Base_de_dados.isnull()
plt.title("Campos Nulos")
plt.figure(figsize=(16,8))
plt.title("Analise  de Campos Nulos")
sns.heatmap(Nulos,cbar=False)
plt.show()
#print(Nulos.sum())

# Campos Únicos

Unicos = Base_de_dados.nunique()
plt.title("Campos Unicos")
plt.figure(figsize=(15,8))
plt.title("Analise de Campos Únicos")
sns.barplot(Unicos)
plt.show()

#print(Base_de_dados.nunique())

# Duplicados
print('Dados duplicados',Base_de_dados.duplicated().sum)

# Estatistica descritiva
print(Base_de_dados.describe())

# Info

print(Base_de_dados.info())

# Separando em porcentagem os valores da base_de_dados para categorizar melhor
print("Genero")
print(Base_de_dados['genero'].value_counts(normalize=True)*100)
print("Raça/etnia")
print(Base_de_dados['Raça/etnia'].value_counts(normalize=True)*100)
print("Educação parental")
print(Base_de_dados['educação dos pais'].value_counts(normalize=True)*100)
print("Almoço")
print(Base_de_dados['Almoço'].value_counts(normalize=True)*100)
print("Curso de preparação")
print(Base_de_dados['curso de preparação'].value_counts(normalize=True)*100)
print('\n')

# renomeando linhas

Base_de_dados['genero'] = Base_de_dados['genero'].replace({'male':'masculino','female':'feminino'})

plt.title("Matemática/Gênero")
sns.boxplot( data= Base_de_dados,x='matematica',y='genero', palette= {'masculino':'lightblue', 'feminino':'lightpink'})
plt.show()
plt.savefig("Matemática/Gênero")
print('\n')

plt.title("Escrita/Gênero")
sns.boxplot( data= Base_de_dados,x='escrita',y='genero',hue='genero',palette= {'masculino':'lightblue', 'feminino':'lightpink'},legend=False)
plt.show()
plt.savefig("Escrita/Gênero")
print('\n')


print(Base_de_dados.groupby(by=['genero']).describe()['matematica'].reset_index(),'\n')

plt.title("Raça/etnia em geral")
sns.pairplot(Base_de_dados,hue='Raça/etnia')
plt.show()
plt.savefig("Raça/etnia em geral")
print('\n')
print(Base_de_dados.groupby(by=['Raça/etnia']).describe()['leitura'].reset_index())

plt.title("Matemática/ Raça/etnia")
sns.boxplot(data=Base_de_dados,x='matematica',y='Raça/etnia')
plt.show()
plt.savefig("Matemática/ Raça/etnia")


plt.title("Matemática/educação dos pais")
sns.boxplot(data= Base_de_dados,x='matematica',y='educação dos pais')
plt.show()
plt.savefig("Matemática/educação dos pais")
print(Base_de_dados.groupby(by=['educação dos pais']).describe()['matematica'].reset_index())

plt.title("Matemática / Leitura")
sns.scatterplot(data= Base_de_dados,x= 'matematica',y= 'leitura')
plt.show()
plt.savefig("Matemática / Leitura")