'''
Neste programa, criamos duas tabelas: categorias e tarefas. A tabela categorias possui um campo id (chave primária) e um campo nome. 
A tabela tarefas possui um campo id (chave primária), um campo nome, um campo data, um campo status (que indica se a tarefa foi realizada ou não)
e um campo id_categoria (chave estrangeira que referencia a tabela categorias).

O relacionamento entre as tabelas é One-to-Many (Um-para-Muitos), já que uma categoria pode ter várias tarefas, mas cada tarefa pertence a apenas uma categoria.
Este programa criará um arquivo chamado tarefas.db, onde as tabelas serão armazenadas. Se o arquivo já existir, ele apenas se conectará a ele. 
O código utiliza a biblioteca sqlite3 do Python para interagir com o banco de dados SQLite.
'''
# Biblioteca responsavel por interagir com o banco de dados
import sqlite3

# Conectar (ou criar) o banco de dados
conn = sqlite3.connect('tarefas.db')

# Criar um objeto cursor para executar comandos SQL
c = conn.cursor()

# Criar a tabela de categorias
c.execute('''
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);
''')

# Criar a tabela de tarefas
c.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    data TEXT,
    status INTEGER CHECK (status IN (0, 1)),
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);
''')

# Salvar as alterações e fechar a conexão
conn.commit()
conn.close()
