from database import *


def adicionar_tarefa(descricao):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
        conn.commit()

def listar_tarefas():
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas")
        return cursor.fetchall()

def concluir_tarefa(tarefa_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tarefas SET status = 'concluída' WHERE id = ?", (tarefa_id,))
        conn.commit()

def remover_tarefa(tarefa_id):
    with conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
        conn.commit()