import mysql.connector
from config import DB_CONFIG

def registrar_chegada_onibus(info_onibus):
    # Conectar ao banco de dados
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Criar tabela (caso não exista)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chegada_onibus (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_veiculo VARCHAR(20),
            linha VARCHAR(10),
            minutos_restantes INT,
            horario_previsto VARCHAR(50)
        );
    """)
    
    # Inserir os dados na tabela
    cursor.execute("""
        INSERT INTO chegada_onibus (id_veiculo, linha, minutos_restantes, horario_previsto)
        VALUES (%s, %s, %s, %s)
    """, (
        info_onibus["vehicle_id"],
        info_onibus["route"],
        info_onibus["eta_minutes"],
        info_onibus["timestamp"]
    ))

    # Commit e fechar a conexão
    conn.commit()
    cursor.close()
    conn.close()
