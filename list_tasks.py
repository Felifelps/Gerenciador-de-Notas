"""Contém funções para listagem e filtragem das tarefas"""

from constants import *
from utils import (
    clear,
    show_table,
    press_enter_to_continue,
    get_option
)


def list_tasks(DATA):
    """Lista as tarefas de acordo com a filtragem escolhida pelo usuário."""
    keep_running, filter_key, filter_attr = get_filter_options()

    if not keep_running:
        return

    clear()
    print("Lista de tarefas\n")

    if filter_attr:
        print(f"Filtrando por {ATTRS[filter_attr]} '{filter_key}'\n")

    show_table(DATA, ATTRS, filter_attr, filter_key)

    press_enter_to_continue()


def get_filter_options():
    """Retorna o tipo de filtro escolhido pelo usuário."""
    while True:
        clear()
        print("Lista de tarefas - Filtragem\n")

        option = get_option({
            1: "Sem filtros",
            2: "Filtrar por descrição",
            3: "Filtrar por prazo",
            4: "Ver Pendentes",
            5: "Ver Iniciadas",
            6: "Ver Concluídas",
            7: "Ver Canceladas",
            0: "Cancelar",
        })
        print()

        if option == '0':
            return False, None, None

        filter_key = ''
        filter_attr = ''

        match option:
            case '2':
                filter_key = input("Digite uma palavra-chave para buscar: ")
                filter_attr = 'description'
            case '3':
                filter_key = input("Digite uma palavra-chave para buscar: ")
                filter_attr = 'deadline'
            case '4' | '5' | '6' | '7':
                status_options = ('Pendente', 'Iniciada', 'Concluída', 'Cancelada')
                filter_key = status_options[int(option) - 4]
                filter_attr = 'status'
            
        return True, filter_key, filter_attr
