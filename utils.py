"""Arquivo com funções diversas."""

import os
from constants import (
    MAX_TABLE_VALUE_LENGTH,
    DATE_FORMAT,
    DATE_FORMAT_LABEL
)
from datetime import datetime


def clear():
    """Limpa o terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def multiline_input(prompt):
    """Implementa um prompt multilinha no terminal."""
    print(prompt)
    result = []
    while line := input():
        result.append(line)
    return "\n".join(result)


def press_enter_to_continue(message=""):
    """Mostra uma mensagem e pede para o usuário pressionar enter."""
    print(message)
    input("Aperte enter para continuar...")


def get_option(options, prompt="Digite o número da opção: "):
    """Lista um conjunto de opções e retorna a escolhida 
    pelo usuário. Também lida com opções inválidas."""
    for number, option in options.items():
        print(f"{number}.{option}")

    option = input(prompt)
    if option.isdigit() and int(option) in options:
        return option

    press_enter_to_continue("Opção inválida!")


def is_description_valid(description):
    """Checa se uma descrição é válida."""
    if not description:
        return False, "A descrição não pode ser vazia"
    return True, None


def is_deadline_valid(deadline):
    """Checa se um prazo é válido."""
    if not deadline:
        return False, "O prazo não pode ser vazio"
    try:
        datetime_obj = datetime.strptime(deadline, DATE_FORMAT)
    except ValueError:
        return False, f"O prazo deve ser no formato {DATE_FORMAT_LABEL}"
    if datetime_obj < datetime.today():
        return False, f"O prazo não pode ser anterior à data atual"
    return True, None

def show_table(DATA, headers, filter_func=lambda _: True, show_n_of_results=True):
    """
    Exibe uma lista de dicionários como uma tabela, e mapeia atributos como headers.
    Permite adicionar uma função de filtragem.
    """
    n_of_results = 0

    table = {attr: [label] for attr, label in headers.items()}
    format_sizes = {attr: len(label) for attr, label in headers.items()}

    # Armazena os dados por coluna, filtra e pega dados de formatação
    for object in DATA:
        if not filter_func(object):
            continue

        for key in headers:
            value = object[key]
            size = len(value)
            if size > MAX_TABLE_VALUE_LENGTH:
                format_sizes[key] = MAX_TABLE_VALUE_LENGTH
            elif size > format_sizes[key]:
                format_sizes[key] = size
            table[key].append(value)
        
        n_of_results += 1

    # Exibe os elementos da tabela formatados
    if show_n_of_results:
        print(f"{n_of_results} resultado(s).")

    if n_of_results > 0:
        for row in range(n_of_results + 1):
            for attr, column in table.items():
                cell = format_table_value(column[row], format_sizes[attr])
                print(cell, end=" ")
            print()


def format_table_value(value, column_size):
    """Formata uma célula da tabela de acordo com o tamanho da coluna."""
    value = value.replace('\\n', ' ').replace('\n', ' ')
    if len(value) > MAX_TABLE_VALUE_LENGTH:
        value = value[:MAX_TABLE_VALUE_LENGTH - 3] + '...'
    return value + (" " * (column_size - len(value)))
