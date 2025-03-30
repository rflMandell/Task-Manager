import database
import cli


def adicionar_tarefa(descricao):
    with database.conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
        conn.commit()

def listar_tarefas():
    with database.conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tarefas")
        return cursor.fetchall()

def concluir_tarefa(tarefa_id):
    with database.conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tarefas SET status = 'concluída' WHERE id = ?", (tarefa_id,))
        conn.commit()

def remover_tarefa(tarefa_id):
    with database.conectar() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
        conn.commit()