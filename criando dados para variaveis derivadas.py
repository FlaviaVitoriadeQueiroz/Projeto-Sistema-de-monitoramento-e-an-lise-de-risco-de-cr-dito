import psycopg2 
clientes = []


# conecta ao banco PostgreSQL
conn = psycopg2.connect(
    dbname="Projedo Banco",
    user="user",
    password="123456",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# insere os dados
cursor.execute("""
UPDATE clientes
SET saldo = limite_do_cartao - valor_da_divida;
""")
conn.commit()



print("✅ Dados inseridos com sucesso!")