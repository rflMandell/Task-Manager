# Gerenciador de Tarefas

## Descrição
Este é um gerenciador de tarefas simples baseado em terminal, que permite adicionar, listar, concluir e remover tarefas. O projeto utiliza **Python** e **SQLite3** para armazenar os dados de forma persistente.

## Funcionalidades
- Adicionar novas tarefas
- Listar todas as tarefas
- Marcar tarefas como concluídas
- Remover tarefas
- Persistência de dados com SQLite3

## Estrutura do Projeto
```
gerenciador_tarefas/
│── main.py               # Arquivo principal
│── database.py           # Conexão com o banco de dados
│── models.py             # Operações no banco (CRUD)
│── cli.py                # Interface de linha de comando
```

## Como Rodar o Projeto
1. **Clone o repositório:**
   ```sh
   git clone https://github.com/rflMandell/Task-Manager
   ```

2. **Instale o Python (se ainda não tiver)**
   - Verifique se o Python está instalado:
     ```sh
     python --version
     ```
   - Se não estiver instalado, baixe e instale pelo [site oficial](https://www.python.org/downloads/).

3. **Execute o programa:**
   ```sh
   python main.py
   ```
   Isso criará o banco de dados (`tarefas.db`, caso ainda não exista) e abrirá o menu interativo.

## Uso
Digite o número da opção desejada no menu:
```
1. Adicionar Tarefa  
2. Listar Tarefas  
3. Concluir Tarefa  
4. Remover Tarefa  
5. Sair  
```

- Se escolher **1**, o programa pedirá a descrição da tarefa.
- Se escolher **2**, ele mostrará todas as tarefas salvas no banco.
- Se escolher **3**, digite o **ID da tarefa** que deseja concluir.
- Se escolher **4**, digite o **ID da tarefa** que deseja remover.
- Se escolher **5**, o programa encerra.

## Consultando o Banco de Dados
Caso queira verificar as tarefas diretamente no SQLite, rode:
```sh
sqlite3 tarefas.db
```
E dentro do SQLite, use:
```sql
SELECT * FROM tarefas;
```
Isso listará todas as tarefas armazenadas no banco.

## Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para modificá-lo e utilizá-lo como quiser!

---

*Contribuições são bem-vindas! Se quiser sugerir melhorias, abra uma issue ou faça um pull request.*
