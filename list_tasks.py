"""Contém funções para listagem e filtragem das tarefas"""

from datetime import datetime
from constants import *
from utils import (
    clear,
    show_table,
    press_enter_to_continue,
    get_option,
)


def list_tasks(DATA):
    """Lista as tarefas de acordo com a filtragem escolhida pelo usuário."""
    data = get_filter_options()
    filter_func = data.get('filter_func')

    if not filter_func:
        return

    clear()
    print("Lista de tarefas\n")

    if message := data.get('message'):
        print(message)

    show_table(DATA, ATTRS, filter_func)

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

        match option:
            case '0':
                return {}
            case '1':
                return {'filter_func': lambda _: True}
            case '2':
                filter_key = input("Digite uma palavra-chave para buscar: ")
                filter_attr = 'description'
            case '3':
                try:
                    start_date_str = input(
                        "Digite uma data inicial (enter para ignorar): ")
                    start_date = datetime.strptime(
                        start_date_str, DATE_FORMAT) if start_date_str else ''

                    end_date_str = input(
                        "Digite uma data final (enter para ignorar): ")
                    end_date = datetime.strptime(
                        end_date_str, DATE_FORMAT) if end_date_str else ''
                except ValueError:
                    press_enter_to_continue(
                        f'As datas devem ser no formato {DATE_FORMAT_LABEL}')
                    break

                if start_date_str and end_date_str:
                    message = f"Filtrando por prazo entre {start_date_str} e {end_date_str}\n"
                elif start_date_str:
                    message = f"Filtrando por prazo a partir de {start_date_str}\n"
                elif end_date_str:
                    message = f"Filtrando por prazo até {end_date_str}\n"
                else:
                    message = f"Filtrando por todas as datas\n"

                return {
                    'filter_func': lambda task: is_date_on_range(
                        datetime.strptime(task['deadline'], DATE_FORMAT),
                        start_date,
                        end_date
                    ),
                    'message': message
                }
            case '4' | '5' | '6' | '7':
                status_options = ('Pendente', 'Iniciada',
                                  'Concluída', 'Cancelada')
                filter_key = status_options[int(option) - 4]
                filter_attr = 'status'

        return {
            'filter_func': lambda task: filter_key.lower() in task[filter_attr].lower(),
            'message': f"Filtrando por {ATTRS[filter_attr]} '{filter_key}'\n"
        }


def is_date_on_range(date, start_date, end_date):
    """Checa se uma data está dentro de um intervalo."""
    if start_date and date < start_date:
        return False
    if end_date and date > end_date:
        return False
    return True
