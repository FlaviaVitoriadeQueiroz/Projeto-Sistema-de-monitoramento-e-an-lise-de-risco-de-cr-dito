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
SELECT historico_de_atrasos, percentual_utilizacao, score_interno AS score
FROM clientes
WHERE historico_de_atrasos >= 5;
"""

df = pd.read_sql(query, conn) #lê os dados da consulta SQL para um DataFrame do pandas  

#quais variaveis influenciam mais no atraso dos pagamentos?
#quando o uso do credito e totalmente utilizado, o pagamento atrasa mais?
plt.figure(figsize=(9,5)) #tamanho da figura
plt.scatter(df['percentual_utilizacao'], df['historico_de_atrasos'], alpha=0.4) #gráfico de dispersão
plt.title('Relação entre Percentual de Utilização e Atrasos dos Clientes') #título do gráfico
plt.xlabel('Percentual de Utilização') #rótulo do eixo x
plt.ylabel('Atrasos') #rótulo do eixo y
plt.grid(alpha=0.3) #adicionar grade
plt.tight_layout() #ajustar layout
plt.show()

#quando o score é baixo, o pagamento atrasa mais?
plt.figure(figsize=(9,5)) #tamanho da figura   
plt.scatter(df['score'], df['historico_de_atrasos'], alpha=0.4) #gráfico de dispersão
plt.title('Relação entre Score e Atrasos dos Clientes')
plt.xlabel('Score') #rótulo do eixo x
plt.ylabel('Atrasos') #rótulo do eixo y
plt.grid(alpha=0.3) #adicionar grade
plt.tight_layout() #ajustar layout
plt.show()