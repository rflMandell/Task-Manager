import sqlite3

def conectar():
    return sqlite3.connect("tarefas.db")

def criar_tabela():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                status TEXT CHECK(status IN ('pendente', 'concluída')) NOT NULL DEFAULT 'pendente'
            )
        ''')
        conn.commit()