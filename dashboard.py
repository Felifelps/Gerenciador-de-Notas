"""Contém funções que geram um relatório com os dados do csv."""

from constants import ATTRS, ATTRS_OPTIONS
from utils import (
    clear,
    show_table,
    press_enter_to_continue
)


def show_dashboard(DATA):
    """Pede um ID válido ao usuário e retorna a tarefa correspondente."""

    by_status = {status: [] for status in ATTRS_OPTIONS['status']}
    for task in DATA:
        by_status[task['status']].append(task)

    headers = {attr: label for attr, label in ATTRS.items() if attr != 'status'}

    clear()
    print("Relatório Geral\n")

    print("Total de tarefas cadastradas:", len(DATA))

    for status in by_status:
        data = by_status.get(status, [])
        print(f"\nTarefas {status}s\n")
        show_table(data, headers, show_n_of_results=not len(data))

    press_enter_to_continue()
