"""Contém funções que geram um relatório com os dados do csv."""

from constants import ATTRS
from utils import (
    clear,
    show_table,
    press_enter_to_continue
)

def show_dashboard(DATA):
    """Pede um ID válido ao usuário e retorna a tarefa correspondente."""

    by_status = {}
    for task in DATA:
        st = task['status']
        if st not in by_status:
            by_status[st] = []
        by_status[st].append(task)

    headers = {attr: label for attr, label in ATTRS.items() if attr != 'status'}

    clear()
    print("Relatório Geral\n")

    print("Total de tarefas cadastradas:", len(DATA))

    print("\nTarefas Pendentes\n")
    show_table(by_status['Pendente'], headers, show_n_of_results=False)

    print("\nTarefas Iniciadas\n")
    show_table(by_status['Iniciada'], headers, show_n_of_results=False)

    print("\nTarefas Concluídas\n")
    show_table(by_status['Concluída'], headers, show_n_of_results=False)

    print("\nTarefas Canceladas\n")
    show_table(by_status['Cancelada'], headers, show_n_of_results=False)

    press_enter_to_continue()