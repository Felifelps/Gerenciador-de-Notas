"""Contém funções para carregamento e modificação do arquivo csv."""

from constants import ATTRS, CSV_FILE, HEADERS


def save_data(data):
    """Converte uma lista de tarefas em csv e salva em arquivo externo."""
    result = [",".join(HEADERS)]
    for task in data:
        line = [task[attr] for attr in ATTRS]
        result.append(",".join(line))

    with open(CSV_FILE, 'w', encoding='utf-8') as file:
        file.write("\n".join(result))


def load_data():
    """
    Carrega os dados do arquivo csv e os converte para uma lista de dicionários.\n
    Cria o arquivo caso ele não exista.
    """
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as file:
            lines = file.read().split('\n')
            lines.pop(0) # Headers  

        data = []
        for line in lines:
            try:
                values = line.split(',')
                data.append({HEADERS[i]: values[i] for i in range(len(HEADERS))})
            except Exception as e:
                pass
        return data

    except FileNotFoundError:
        save_data([])
        return []
