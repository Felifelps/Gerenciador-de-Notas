# Gestão de Tarefas

Este é um projeto de gerenciamento de tarefas desenvolvido em Python. Ele permite criar, listar, buscar, atualizar, remover e gerar relatórios de tarefas armazenadas em um arquivo CSV.

## Funcionalidades

- **Listar Tarefas**: Exibe todas as tarefas com opções de filtragem (por descrição, prazo ou status).
- **Buscar Tarefa**: Permite buscar uma tarefa específica pelo ID.
- **Inserir Tarefa**: Adiciona uma nova tarefa ao sistema com validações para descrição e prazo.
- **Atualizar Tarefa**: Edita os dados de uma tarefa existente.
- **Remover Tarefa**: Exclui uma tarefa do sistema com confirmação antes da remoção.
- **Relatório**: Gera um relatório com o status das tarefas (Pendentes, Iniciadas, Concluídas, Canceladas), exibindo categorias vazias de forma clara.

## Como Usar

1. Certifique-se de ter o Python 3 instalado.
2. Clone ou baixe este repositório.
3. Execute o arquivo `main.py` para iniciar o programa:
   ```bash
   python main.py
   ```
4. Siga as instruções no terminal para gerenciar suas tarefas.

## Estrutura do Projeto

- **`main.py`**: Arquivo principal que inicializa o programa.
- **`constants.py`**: Contém constantes usadas em todo o projeto.
- **`crud_task.py`**: Funções para criar, buscar, atualizar e remover tarefas.
- **`list_tasks.py`**: Funções para listar e filtrar tarefas.
- **`dashboard.py`**: Funções para gerar relatórios.
- **`data.py`**: Funções para carregar e salvar dados no arquivo CSV.
- **`utils.py`**: Funções auxiliares como validações, exibição de tabelas e limpeza do terminal.
- **`data.csv`**: Arquivo que armazena as tarefas.

## Formato do Arquivo CSV

O arquivo `data.csv` armazena as tarefas no seguinte formato:

```
id,description,status,deadline
1,Estudar conceitos básicos de Python,Concluída,06/04/2025
2,Resolver exercícios de lógica de programação,Iniciada,08/04/2025
...
```

- **`id`**: Identificador único da tarefa.
- **`description`**: Descrição da tarefa.
- **`status`**: Status da tarefa (Pendente, Iniciada, Concluída, Cancelada).
- **`deadline`**: Prazo da tarefa no formato `DD/MM/AAAA`.

## Requisitos

- Python 3.6 ou superior.

## Melhorias Implementadas

- Adicionada confirmação antes de remover uma tarefa.
- Mensagens de erro mais claras para entradas inválidas.
- Relatórios exibem categorias vazias com mensagens apropriadas.
- Validação aprimorada para prazos no formato correto (`DD/MM/AAAA`).
- Mensagem amigável exibida ao sair do programa.

## Autor

- **Felipe dos Santos Ferreira**
- Turma: CC2

## Licença

Este projeto é apenas para fins educacionais e não possui uma licença específica.