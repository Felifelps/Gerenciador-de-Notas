"""
Arquivo principal do projeto.
Felipe dos Santos Ferreira
Turma CC2
"""

from constants import *
from crud_task import (
    search_task,
    insert_task,
    update_task,
    remove_task
)
from dashboard import show_dashboard
from data import load_data, save_data
from list_tasks import list_tasks
from utils import clear, get_option


def main():
    """Função principal do programa."""

    try:
        # Carrega os dados do csv
        DATA = load_data()
    except Exception as e:
        return print("Erro ao carregar os dados!", e)

    while True:
        try:
            clear()
            print("Gerenciamento de Tarefas\n")
            option = get_option({
                1: "Listar tarefas",
                2: "Buscar tarefa",
                3: "Inserir tarefa",
                4: "Atualizar tarefa",
                5: "Remover tarefa",
                6: "Relatório",
                0: "Sair",
            })

            match option:
                case "1":
                    list_tasks(DATA)
                case "2":
                    search_task(DATA)
                case "3":
                    insert_task(DATA)
                case "4":
                    update_task(DATA)
                case "5":
                    remove_task(DATA)
                case "6":
                    show_dashboard(DATA)
                case "0":
                    break
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("Um erro ocorreu!", e)
            break
    # Salva os dados ao fim do programa
    save_data(DATA)

    print("Até a próxima! ;)")


if __name__ == '__main__':
    main()
