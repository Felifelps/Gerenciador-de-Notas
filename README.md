# Gerenciador de Notas

## Descrição do Projeto
Gerenciador de Notas é um sistema simples e prático para controle de tarefas. Esse aplicativo permite que os usuários cuidem de suas atividades organizando-as de maneira eficiente. Cada atividade pode ser categorizada conforme seu status - 'Concluída', 'Pendente', 'Iniciada', 'Cancelada'. Ademais, cada tarefa contém um prazo de conclusão para auxiliar no gerenciamento do tempo.

## Estrutura dos Arquivos
O projeto consiste nos seguintes arquivos:

1. [constants.py](constants.py): Armazena as constantes usadas no projeto, como opções de status para as tarefas.
2. [crud_task.py](crud_task.py): Contém funções para criação, busca, atualização e remoção de tarefas.
3. [dashboard.py](dashboard.py): Possui uma função para gerar um relatório com os dados de todas as tarefas.
4. [data.py](data.py): Contém funções para carregamento e modificação do arquivo CSV que armazena as tarefas.
5. [list_tasks.py](list_tasks.py): Contém funções para listagem e filtragem das tarefas.
6. [main.py](main.py): É o arquivo principal que coordena todas as funcionalidades do projeto.
7. [utils.py](utils.py): Inclui funções diversas auxiliares para o projeto.

## Instruções de Configuração e Execução
Siga os passos a seguir para configurar e iniciar o programa:

1. Clone o repositório com o comando: ```git clone https://github.com/Felifelps/Gerenciador-de-Notas```
2. Vá para o diretório do projeto: ```cd Gerenciador-de-Notas```
3. Para executar o programa, use o comando: ```python main.py```

## Exemplos de Uso:
Com o Gerenciador de Notas, você poderá:

- Listar todas as tarefas
- Buscar uma tarefa específica por ID
- Inserir uma nova tarefa
- Atualizar os detalhes de uma tarefa existente
- Remover uma tarefa
- Gerar um relatório com a situação atual das suas tarefas

## Requisitos
Para rodar este aplicativo, é necessário:

- Python 3.8 ou superior
- Um terminal para execução (como cmd, Powershell, Terminal etc.) 

## Contribuição
Qualquer contribuição para esta aplicação será grandemente apreciada. Se você tiver uma característica que gostaria de adicionar ou um bug que gostaria de corrigir, o melhor método é fazer um Pull Request.

## Licença
Este projeto é licenciado sob a licença MIT.