import sqlite3

# Conectar (ou criar) o banco de dados
conn = sqlite3.connect('eventos.db')

# Criar um objeto cursor para executar comandos SQL
c = conn.cursor()

# Criar a tabela de eventos
c.execute('''
CREATE TABLE IF NOT EXISTS eventos (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL UNIQUE,
    data TEXT NOT NULL,
    local TEXT NOT NULL
);
''')

# Criar a tabela de organizador
c.execute('''
CREATE TABLE IF NOT EXISTS organizador (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    cpf TEXT, 
    id_eventos INTEGER,
    FOREIGN KEY (id_eventos) REFERENCES eventos(id)
);
''')

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()