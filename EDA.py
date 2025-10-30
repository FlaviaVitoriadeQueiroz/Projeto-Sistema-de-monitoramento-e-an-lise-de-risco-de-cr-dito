import pandas as pd #estrutura de dados (DataFrame) para agrupar e calcular estatísticas.
import psycopg2 #biblioteca para conectar ao banco de dados PostgreSQL
import matplotlib.pyplot as plt

# conecta ao banco PostgreSQL
conn = psycopg2.connect(
    dbname="Projedo Banco",
    user="user",
    password="123456",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

query = """
SELECT renda, score_interno AS score
FROM clientes
WHERE renda IS NOT NULL AND score_interno IS NOT NULL;
"""
df = pd.read_sql(query, conn) #lê os dados da consulta SQL para um DataFrame do pandas
print(df.head())

# Plotar gráfico de dispersão entre renda e score
plt.figure(figsize=(9,5))
plt.scatter(df['renda'], df['score'], alpha=0.4)
plt.title('Relação entre Renda e Score')
plt.xlabel('Renda')
plt.ylabel('Score')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# Analisar score médio por decil de renda
# Criar decis de renda
df['decil_renda'] = pd.qcut(df['renda'], 10, labels=False) #cria 10 grupos iguais (decis) com base na renda

# Calcular score médio por decil
renda_stats = df.groupby('decil_renda').agg( #agregações por decil
    renda_media=('renda', 'mean'), #média da renda em cada decil
    score_medio=('score', 'mean'), #média do score em cada decil
    quantidade=('score', 'size') #número de clientes em cada decil
).reset_index()

# Plotar gráfico
plt.figure(figsize=(9,5)) #tamanho da figura
x = renda_stats['decil_renda'] + 1 #ajustar índice para exibir de 1 a 10
plt.bar(x, renda_stats['score_medio'], color='teal') #barras verticais

plt.title('Score médio por decil de renda')
plt.xlabel('Decil de Renda (1 = menor renda)')
plt.ylabel('Score médio')
plt.xticks(x) 
plt.grid(alpha=0.3) #adicionar grade
plt.tight_layout() #ajustar layout
plt.show()

#decil 1 com menor renda
#decil 10 com maior renda


