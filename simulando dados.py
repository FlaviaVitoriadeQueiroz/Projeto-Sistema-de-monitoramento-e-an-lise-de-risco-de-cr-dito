import random 
from datetime import datetime, timedelta
import psycopg2 
import pandas as pd

# gera dados simulados para 350 clientes
clientes = []
for i in range(1, 351):
    clientes.append({
        "id": i,
        "renda": random.randint(0, 10000000), #gera um número inteiro aleatório entre dois valores
        "idade": random.uniform(18, 100), #gera um número decimal aleatório entre dois valores
        "valor_da_divida": random.randint(1, 10000000),
        "limite_do_cartao": random.randint(1, 10000000),
        "historico_de_atrasos": random.randint(0, 12), #gera um número inteiro aleatório entre 0 e 12
        "score_interno": random.randint(0, 100)
    })

# conecta ao banco PostgreSQL
conn = psycopg2.connect(
    dbname="Projedo Banco",
    user="user",
    password="123456",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()


# cria a tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    renda NUMERIC,
    idade NUMERIC,
    valor_da_divida NUMERIC,
    limite_do_cartao NUMERIC,
    historico_de_atrasos INT,
    score_interno INT
);
""")
conn.commit()

# insere os dados
for cliente in clientes:
    cursor.execute("""
        INSERT INTO clientes (id, renda, idade, valor_da_divida, limite_do_cartao, historico_de_atrasos, score_interno)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """, (
        cliente["id"],
        cliente["renda"],
        cliente["idade"],
        cliente["valor_da_divida"],
        cliente["limite_do_cartao"],
        cliente["historico_de_atrasos"],
        cliente["score_interno"]
    ))

# salva alterações e fecha conexão
conn.commit()
conn.close()

print("✅ Dados inseridos com sucesso!")