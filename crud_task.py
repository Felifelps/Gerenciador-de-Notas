"""Contém funções relacionadas à execução de ações em uma única tarefa."""

from constants import ATTRS, ATTRS_OPTIONS
from data import save_data
from utils import (
    clear,
    get_option,
    press_enter_to_continue,
    is_description_valid,
    is_deadline_valid
)


def get_task(action, DATA):
    """Pede um ID válido ao usuário e retorna a tarefa correspondente."""
    tasks_by_id = {task['id']: task for task in DATA}

    while True:
        clear()
        print(f"{action} Tarefa\n")

        task_id = input(
            f"Insira o ID da tarefa que deseja {action.lower()} (ou '0' para sair): ")
        if task_id == '0':
            return

        if task := tasks_by_id.get(task_id):
            return task

        press_enter_to_continue("Id não existente ou inválido!")


def search_task(DATA):
    """Pede um ID válido ao usuário e exibe os dados da tarefa correspondente."""
    task = get_task("Buscar", DATA)

    if task:
        print()
        for attr, label in ATTRS.items():
            print(f"{label}: {task[attr]}")
        press_enter_to_continue()


def insert_task(DATA):
    """Permite que o usuário crie uma tarefa."""
    while True:
        clear()
        print("Inserir Tarefa\n")

        print("Digite '0' para cancelar.")
        description = input("Descreva sua tarefa: ")
        if description == '0':
            return

        is_valid, error = is_description_valid(description)
        if not is_valid:
            press_enter_to_continue(error)
            continue

        deadline = input(
            "Informe o prazo para concluí-la (formato DD/MM/AAAA): ")
        if deadline == '0':
            return

        is_valid, error = is_deadline_valid(deadline)
        if not is_valid:
            press_enter_to_continue(error)
            continue

        max_task_id = 1

        if DATA:
            max_task_id += max((int(task['id']) for task in DATA))

        DATA.append({
            'id': str(max_task_id),
            'description': description,
            'status': 'Pendente',
            'deadline': deadline
        })

        save_data(DATA)

        return press_enter_to_continue("Tarefa inserida com sucesso!")


def update_task(DATA):
    """Pede um ID válido ao usuário e o permite editar os dados da tarefa correspondente."""
    task = get_task("Atualizar", DATA)
    if not task:
        return

    task_index = DATA.index(task)
    while True:
        clear()
        print(f"Atualizar tarefa {task.get('id')}\n")

        option = get_option({
            1: "Descrição: " + task.get('description'),
            2: "Status: " + task.get('status'),
            3: "Prazo: " + task.get('deadline'),
            0: "Cancelar"
        })

        match option:
            case "1":
                description = input("Digite a nova descrição: ")
                is_valid, error = is_description_valid(description)
                if not is_valid:
                    press_enter_to_continue(error)
                    continue
                DATA[task_index]['description'] = description
            case "2":
                status_options = {i + 1: value for i,
                                  value in enumerate(ATTRS_OPTIONS['status'])}
                option = get_option({
                    **status_options,
                    0: "Cancelar"
                })
                if option == "0" or not option:
                    continue
                DATA[task_index]['status'] = status_options[int(option)]
            case "3":
                deadline = input("Digite o novo prazo: ")
                is_valid, error = is_deadline_valid(deadline)
                if not is_valid:
                    press_enter_to_continue(error)
                    continue
                DATA[task_index]['deadline'] = deadline
            case "0":
                break

        save_data(DATA)

        press_enter_to_continue("Tarefa atualizada com sucesso!")


def remove_task(DATA):
    """Pede um ID válido ao usuário e remove a tarefa correspondente."""
    task = get_task("Remover", DATA)
    if task:

        if input("Quer mesmo deletar? (s/n)").lower() != 's':
            return press_enter_to_continue("Remoção cancelada")

        DATA.remove(task)
        save_data(DATA)
        press_enter_to_continue("Tarefa excluída com sucesso!")
